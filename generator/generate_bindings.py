from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCALAR_TYPES = {
    "bool",
    "char",
    "signed char",
    "unsigned char",
    "int8_t",
    "uint8_t",
    "int16_t",
    "uint16_t",
    "int32_t",
    "uint32_t",
    "int64_t",
    "uint64_t",
    "short",
    "unsigned short",
    "int",
    "unsigned int",
    "long",
    "unsigned long",
    "long long",
    "unsigned long long",
    "float",
    "double",
}
CONTAINER_RE = re.compile(r"^std::(array|vector)<(.+)>$")


@dataclass(frozen=True)
class GeneratedClass:
    qualified_name: str
    python_name: str
    properties: tuple[str, ...]
    skipped_fields: tuple[str, ...]


def normalize_type(type_name: str) -> str:
    """Normalize Clang's spelling enough for safe type matching and emission."""
    normalized = type_name.strip()
    normalized = re.sub(r"\bconst\s+", "", normalized)
    normalized = re.sub(r"\s*&&?$", "", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    normalized = re.sub(r"\s*<\s*", "<", normalized)
    normalized = re.sub(r"\s*>\s*", ">", normalized)
    normalized = re.sub(r"\s*,\s*", ", ", normalized)
    normalized = normalized.lstrip(":")
    return normalized.strip()


def split_template_arguments(arguments: str) -> list[str]:
    result: list[str] = []
    depth = 0
    start = 0
    for index, char in enumerate(arguments):
        if char == "<":
            depth += 1
        elif char == ">":
            depth -= 1
        elif char == "," and depth == 0:
            result.append(arguments[start:index].strip())
            start = index + 1
    result.append(arguments[start:].strip())
    return result


def is_supported_type(type_name: str, known_classes: set[str]) -> bool:
    normalized = normalize_type(type_name)
    if normalized in SCALAR_TYPES or normalized == "std::string":
        return True
    if normalized in known_classes:
        return True
    match = CONTAINER_RE.match(normalized)
    if not match:
        return False
    arguments = split_template_arguments(match.group(2))
    if match.group(1) == "array":
        return len(arguments) == 2 and arguments[1].isdigit() and is_supported_type(
            arguments[0], known_classes
        )
    return len(arguments) == 1 and is_supported_type(arguments[0], known_classes)


def qualified_name(cpp_class: dict[str, Any]) -> str:
    namespace = cpp_class["namespace"]
    return f"{namespace}::{cpp_class['name']}" if namespace else cpp_class["name"]


def python_name(cpp_class: dict[str, Any], overrides: dict[str, Any]) -> str:
    name = qualified_name(cpp_class)
    class_override = overrides.get("classes", {}).get(name, {})
    return class_override.get("python_name", cpp_class["name"].removesuffix("_"))


def public_methods(cpp_class: dict[str, Any], name: str) -> list[dict[str, Any]]:
    return [
        method
        for method in cpp_class["methods"]
        if method["access"] == "public" and method["name"] == name
    ]


def has_property_accessors(cpp_class: dict[str, Any], field_name: str) -> bool:
    methods = public_methods(cpp_class, field_name)
    getter = any(
        not method["parameters"]
        and method["return_type"] != "void"
        and method["is_const"]
        for method in methods
    )
    setter = any(
        len(method["parameters"]) == 1
        and method["return_type"] == "void"
        and "&&" not in method["parameters"][0]["type"]
        for method in methods
    )
    return getter and setter


def default_constructible(cpp_class: dict[str, Any]) -> bool:
    return any(
        constructor["access"] == "public" and not constructor["parameters"]
        for constructor in cpp_class["constructors"]
    )


def has_public_operator(cpp_class: dict[str, Any], operator: str) -> bool:
    return any(
        method["access"] == "public" and method["name"] == operator
        for method in cpp_class["methods"]
    )


def header_include(cpp_class: dict[str, Any], sdk_root: Path) -> str:
    header = Path(cpp_class["location"]["file"])
    if not header.is_absolute():
        header = sdk_root / header
    include_root = sdk_root / "include"
    try:
        return str(header.resolve().relative_to(include_root.resolve()))
    except ValueError as error:
        raise ValueError(f"header is outside SDK include directory: {header}") from error


def dependency_order(
    classes: list[dict[str, Any]], known_classes: set[str]
) -> list[dict[str, Any]]:
    """Emit value-type dependencies before containers that hold them.

    pybind11's STL casters resolve nested class registrations at runtime. A
    stable dependency-first order keeps nested message properties usable even
    when the IDL generator's input headers are alphabetically ordered.
    """
    by_name = {normalize_type(qualified_name(item)): item for item in classes}
    order = {normalize_type(qualified_name(item)): index for index, item in enumerate(classes)}
    dependencies: dict[str, set[str]] = {}
    for item in classes:
        item_name = normalize_type(qualified_name(item))
        text = " ".join(
            [field["type"] for field in item["fields"]]
            + [parameter["type"] for method in item["methods"] for parameter in method["parameters"]]
        )
        dependencies[item_name] = {
            name for name in known_classes if name in text and name != item_name and name in by_name
        }

    visiting: set[str] = set()
    visited: set[str] = set()
    result: list[dict[str, Any]] = []

    def visit(name: str) -> None:
        if name in visited:
            return
        if name in visiting:
            # Cyclic value types cannot be represented directly in C++ anyway;
            # retain deterministic input order rather than recursing forever.
            return
        visiting.add(name)
        for dependency in sorted(dependencies.get(name, ()), key=order.__getitem__):
            visit(dependency)
        visiting.remove(name)
        visited.add(name)
        result.append(by_name[name])

    for item in classes:
        visit(normalize_type(qualified_name(item)))
    return result


def render_class(
    cpp_class: dict[str, Any],
    overrides: dict[str, Any],
    known_classes: set[str],
) -> tuple[list[str], GeneratedClass]:
    cpp_name = qualified_name(cpp_class)
    py_name = python_name(cpp_class, overrides)
    variable = re.sub(r"[^A-Za-z0-9_]", "_", py_name).lower() + "_class"
    lines = [f'  py::class_<{cpp_name}> {variable}(module, "{py_name}");']
    if default_constructible(cpp_class):
        lines.append(f"  {variable}.def(py::init<>());")

    properties: list[str] = []
    skipped_fields: list[str] = []
    for field in cpp_class["fields"]:
        field_name = field["name"]
        property_name = field_name.removesuffix("_")
        if not is_supported_type(field["type"], known_classes) or not has_property_accessors(
            cpp_class, property_name
        ):
            skipped_fields.append(field_name)
            continue
        field_type = normalize_type(field["type"])
        lines.extend(
            [
                f"  {variable}.def_property(",
                f'      "{property_name}",',
                f"      [](const {cpp_name}& self) {{ return self.{property_name}(); }},",
                f"      []({cpp_name}& self, const {field_type}& value) {{",
                f"        self.{property_name}(value);",
                "      });",
            ]
        )
        properties.append(property_name)

    if has_public_operator(cpp_class, "operator=="):
        lines.append(
            f'  {variable}.def("__eq__", &{cpp_name}::operator==, py::is_operator());'
        )
    if has_public_operator(cpp_class, "operator!="):
        lines.append(
            f'  {variable}.def("__ne__", &{cpp_name}::operator!=, py::is_operator());'
        )
    return lines, GeneratedClass(
        qualified_name=cpp_name,
        python_name=py_name,
        properties=tuple(properties),
        skipped_fields=tuple(skipped_fields),
    )


def generate(
    inventory: dict[str, Any],
    overrides: dict[str, Any],
    namespace_prefix: str | list[str],
    function_name: str,
    module_path: list[str],
) -> tuple[str, dict[str, Any]]:
    sdk_root = Path(inventory["sdk_root"])
    prefixes = [namespace_prefix] if isinstance(namespace_prefix, str) else namespace_prefix
    selected_classes = [
        cpp_class
        for cpp_class in inventory["classes"]
        if any(cpp_class["namespace"].startswith(prefix) for prefix in prefixes)
        and not overrides.get("classes", {})
        .get(qualified_name(cpp_class), {})
        .get("manual", False)
    ]
    known_classes = {
        normalize_type(qualified_name(cpp_class)) for cpp_class in inventory["classes"]
    }
    selected_classes = dependency_order(selected_classes, known_classes)
    includes = sorted(
        {header_include(cpp_class, sdk_root) for cpp_class in selected_classes}
    )
    lines = [
        '// Generated by generator/generate_bindings.py. Do not edit manually.',
        '#include "bindings.hpp"',
        "",
        "#include <pybind11/stl.h>",
        "",
    ]
    lines.extend(f"#include <{header}>" for header in includes)
    lines.extend(["", "namespace py = pybind11;", "", f"void {function_name}(py::module_& root) {{"])

    parent = "root"
    for index, name in enumerate(module_path):
        variable = "module" if index == len(module_path) - 1 else f"module_{index}"
        lines.append(f'  py::module_ {variable} = EnsureSubmodule({parent}, "{name}");')
        parent = variable
    if not module_path:
        parent = "root"
    lines.append("")

    generated_classes: list[GeneratedClass] = []
    for cpp_class in selected_classes:
        class_lines, generated = render_class(cpp_class, overrides, known_classes)
        class_lines = [line.replace("(module,", f"({parent},") for line in class_lines]
        lines.extend(class_lines)
        lines.append("")
        generated_classes.append(generated)
    lines.append("}")
    lines.append("")

    report = {
        "schema_version": 1,
        "function": function_name,
        "namespace_prefix": prefixes,
        "classes": [
            {
                "qualified_name": item.qualified_name,
                "python_name": item.python_name,
                "properties": list(item.properties),
                "skipped_fields": list(item.skipped_fields),
            }
            for item in generated_classes
        ],
    }
    return "\n".join(lines), report


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate simple pybind11 bindings")
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--overrides", type=Path, required=True)
    parser.add_argument("--namespace-prefix", action="append", required=True)
    parser.add_argument("--function", required=True)
    parser.add_argument("--module", action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    arguments = parser.parse_args()

    inventory = json.loads(arguments.inventory.read_text(encoding="utf-8"))
    overrides = json.loads(arguments.overrides.read_text(encoding="utf-8"))
    source, report = generate(
        inventory=inventory,
        overrides=overrides,
        namespace_prefix=arguments.namespace_prefix,
        function_name=arguments.function,
        module_path=arguments.module,
    )
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(source, encoding="utf-8")
    arguments.report.parent.mkdir(parents=True, exist_ok=True)
    arguments.report.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"Generated {len(report['classes'])} classes in {arguments.output}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
