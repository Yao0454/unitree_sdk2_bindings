from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    from .model import (
        ApiInventory,
        CppBase,
        CppClass,
        CppEnum,
        CppEnumerator,
        CppField,
        CppMethod,
        CppParameter,
        ScanDiagnostic,
        SourceLocation,
    )
except ImportError:  # Support direct execution: python generator/scan_headers.py
    from model import (
        ApiInventory,
        CppBase,
        CppClass,
        CppEnum,
        CppEnumerator,
        CppField,
        CppMethod,
        CppParameter,
        ScanDiagnostic,
        SourceLocation,
    )


# A function can legally return ``struct Foo``. Requiring a declaration
# delimiter after the name avoids treating those return types as declarations
# while still allowing one-line and multi-line class/enum definitions.
DECLARATION_RE = re.compile(
    r"^\s*(class|struct|enum(?:\s+class)?)\s+([A-Za-z_]\w*)\b" r"(?=\s*(?::|\{|;|$))"
)
NAMESPACE_RE = re.compile(r"^\s*namespace\s+([A-Za-z_]\w*(?:::[A-Za-z_]\w*)*)\s*(\{)?")
INTERNAL_NAMESPACE_PREFIXES = ("dds::", "org::eclipse::cyclonedds::")


@dataclass(frozen=True)
class DeclarationCandidate:
    header: Path
    namespace: str
    name: str
    kind: str
    line: int

    @property
    def qualified_name(self) -> str:
        if not self.namespace:
            return self.name
        return f"{self.namespace}::{self.name}"


def _strip_comments_and_literals(source: str) -> str:
    result: list[str] = []
    index = 0
    state = "code"
    quote = ""
    while index < len(source):
        char = source[index]
        next_char = source[index + 1] if index + 1 < len(source) else ""
        if state == "code":
            if char == "/" and next_char == "/":
                result.extend("  ")
                index += 2
                state = "line_comment"
                continue
            if char == "/" and next_char == "*":
                result.extend("  ")
                index += 2
                state = "block_comment"
                continue
            if char in {'"', "'"}:
                quote = char
                result.append(" ")
                index += 1
                state = "literal"
                continue
            result.append(char)
            index += 1
            continue
        if state == "line_comment":
            if char == "\n":
                result.append("\n")
                state = "code"
            else:
                result.append(" ")
            index += 1
            continue
        if state == "block_comment":
            if char == "*" and next_char == "/":
                result.extend("  ")
                index += 2
                state = "code"
            else:
                result.append("\n" if char == "\n" else " ")
                index += 1
            continue
        if char == "\\":
            result.append(" ")
            if next_char:
                result.append("\n" if next_char == "\n" else " ")
                index += 2
            else:
                index += 1
            continue
        if char == quote:
            result.append(" ")
            index += 1
            state = "code"
            continue
        result.append("\n" if char == "\n" else " ")
        index += 1
    return "".join(result)


def discover_declarations(header: Path) -> list[DeclarationCandidate]:
    source = _strip_comments_and_literals(header.read_text(encoding="utf-8"))
    namespace_stack: list[tuple[str, int]] = []
    pending_namespaces: list[str] = []
    brace_depth = 0
    candidates: list[DeclarationCandidate] = []

    for line_number, line in enumerate(source.splitlines(), start=1):
        namespace = "::".join(item[0] for item in namespace_stack)
        declaration_match = DECLARATION_RE.match(line)
        if (
            declaration_match
            and not line.lstrip().startswith("#")
            and not namespace.startswith(INTERNAL_NAMESPACE_PREFIXES)
        ):
            candidates.append(
                DeclarationCandidate(
                    header=header,
                    namespace=namespace,
                    name=declaration_match.group(2),
                    kind=declaration_match.group(1).replace(" ", "_"),
                    line=line_number,
                )
            )

        depth_before = brace_depth
        namespace_match = NAMESPACE_RE.match(line)
        if namespace_match:
            pending_namespaces.extend(namespace_match.group(1).split("::"))

        opening_braces = line.count("{")
        if pending_namespaces and opening_braces:
            namespace_depth = depth_before + 1
            for name in pending_namespaces:
                namespace_stack.append((name, namespace_depth))
                namespace_depth += 1
            pending_namespaces.clear()

        brace_depth += line.count("{") - line.count("}")
        while namespace_stack and namespace_stack[-1][1] > brace_depth:
            namespace_stack.pop()

    return candidates


def _location(node: dict[str, Any], fallback: DeclarationCandidate) -> SourceLocation:
    loc = node.get("loc", {})
    return SourceLocation(
        file=str(loc.get("file", fallback.header)),
        line=int(loc.get("line", fallback.line) or 0),
        column=int(loc.get("col", 0) or 0),
    )


def _qual_type(node: dict[str, Any]) -> str:
    return str(node.get("type", {}).get("qualType", ""))


def _return_type(function_type: str) -> str:
    marker = function_type.find("(")
    return function_type[:marker].rstrip() if marker >= 0 else function_type


DEFAULT_WRAPPER_KINDS = {
    "ConstantExpr",
    "CXXBindTemporaryExpr",
    "ExprWithCleanups",
    "FullExpr",
    "ImplicitCastExpr",
    "MaterializeTemporaryExpr",
    "ParenExpr",
}


def _default_expression(node: dict[str, Any]) -> str | None:
    """Return a safe C++ spelling for a Clang default-argument expression.

    Only context-free literals and named enum constants are accepted. Keeping
    this deliberately small prevents generated bindings from evaluating an
    arbitrary constructor or function call while the Python module imports.
    """
    kind = node.get("kind")
    inner = [item for item in node.get("inner", []) if isinstance(item, dict)]
    if kind in DEFAULT_WRAPPER_KINDS:
        return _default_expression(inner[0]) if len(inner) == 1 else None
    if kind == "CXXConstructExpr":
        constructed_type = _qual_type(node)
        if len(inner) == 1 and (
            constructed_type.startswith(("std::string", "const std::string"))
            or "basic_string<char" in constructed_type
        ):
            return _default_expression(inner[0])
        return None
    if kind == "CXXBoolLiteralExpr":
        value = node.get("value")
        return str(value).lower() if isinstance(value, bool) else None
    if kind == "IntegerLiteral":
        value = str(node.get("value", ""))
        return value if re.fullmatch(r"[0-9]+", value) else None
    if kind == "FloatingLiteral":
        value = str(node.get("value", ""))
        if not re.fullmatch(
            r"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?", value
        ):
            return None
        return value if any(char in value for char in ".eE") else value + ".0"
    if kind == "StringLiteral":
        value = node.get("value")
        if not isinstance(value, str):
            return None
        # Clang normally includes the C++ quotes. Quote defensively for AST
        # variants that expose only the decoded contents.
        return (
            value
            if value.startswith(('"', 'u8"', 'u"', 'U"', 'L"'))
            else json.dumps(value)
        )
    if kind == "CharacterLiteral":
        value = str(node.get("value", ""))
        return f"static_cast<char>({value})" if value.isdigit() else None
    if kind in {"CXXNullPtrLiteralExpr", "GNUNullExpr"}:
        return "nullptr"
    if kind == "DeclRefExpr":
        referenced = node.get("referencedDecl", {})
        if referenced.get("kind") != "EnumConstantDecl":
            return None
        name = str(referenced.get("name", ""))
        enum_type = _qual_type(node).strip().lstrip(":")
        if not re.fullmatch(r"[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*", name):
            return None
        if not re.fullmatch(r"[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*", enum_type):
            return None
        return f"{enum_type}::{name}"
    if kind == "UnaryOperator" and node.get("opcode") in {"+", "-"} and len(inner) == 1:
        operand = _default_expression(inner[0])
        if operand is None or not re.fullmatch(
            r"[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?", operand
        ):
            return None
        return str(node["opcode"]) + operand
    return None


def _parameter_default(node: dict[str, Any]) -> str | None:
    if "init" not in node:
        return None
    expressions = [
        child
        for child in node.get("inner", [])
        if isinstance(child, dict) and child.get("kind") != "FullComment"
    ]
    return _default_expression(expressions[0]) if len(expressions) == 1 else None


def _parameters(node: dict[str, Any]) -> tuple[CppParameter, ...]:
    parameters: list[CppParameter] = []
    for child in node.get("inner", []):
        if child.get("kind") != "ParmVarDecl":
            continue
        parameters.append(
            CppParameter(
                name=str(child.get("name", "")),
                type=_qual_type(child),
                has_default="init" in child,
                default_value=_parameter_default(child),
            )
        )
    return tuple(parameters)


def _method(
    node: dict[str, Any], access: str, candidate: DeclarationCandidate
) -> CppMethod:
    function_type = _qual_type(node)
    kind = node.get("kind")
    return CppMethod(
        name=str(node.get("name", candidate.name)),
        return_type="" if kind == "CXXConstructorDecl" else _return_type(function_type),
        parameters=_parameters(node),
        access=access,
        is_const=function_type.rstrip().endswith(" const"),
        is_static=node.get("storageClass") == "static",
        is_virtual=bool(node.get("virtual", False)),
        is_pure_virtual=bool(node.get("pure", False)),
        is_noexcept="noexcept" in function_type,
        is_constructor=kind == "CXXConstructorDecl",
        location=_location(node, candidate),
    )


def parse_class(node: dict[str, Any], candidate: DeclarationCandidate) -> CppClass:
    default_access = "private" if candidate.kind == "class" else "public"
    access = default_access
    constructors: list[CppMethod] = []
    methods: list[CppMethod] = []
    fields: list[CppField] = []

    for child in node.get("inner", []):
        if child.get("isImplicit"):
            continue
        kind = child.get("kind")
        if kind == "AccessSpecDecl":
            access = str(child.get("access", access))
        elif kind == "FieldDecl":
            fields.append(
                CppField(
                    name=str(child.get("name", "")),
                    type=_qual_type(child),
                    access=access,
                    location=_location(child, candidate),
                )
            )
        elif kind == "CXXConstructorDecl":
            constructors.append(_method(child, access, candidate))
        elif kind in {"CXXMethodDecl", "CXXConversionDecl"}:
            methods.append(_method(child, access, candidate))

    bases = tuple(
        CppBase(
            type=str(base.get("type", {}).get("qualType", "")),
            access=str(base.get("access", default_access)),
            is_virtual=bool(base.get("isVirtual", False)),
        )
        for base in node.get("bases", [])
    )
    definition = node.get("definitionData", {})
    return CppClass(
        namespace=candidate.namespace,
        name=candidate.name,
        kind=candidate.kind,
        location=_location(node, candidate),
        constructors=tuple(constructors),
        methods=tuple(methods),
        fields=tuple(fields),
        bases=bases,
        is_abstract=bool(definition.get("isAbstract", False)),
        is_polymorphic=bool(definition.get("isPolymorphic", False)),
        is_trivially_copyable=bool(definition.get("isTriviallyCopyable", False)),
    )


def _enum_value(node: dict[str, Any]) -> str | None:
    stack = list(node.get("inner", []))
    while stack:
        child = stack.pop()
        if child.get("kind") in {"IntegerLiteral", "ConstantExpr"} and "value" in child:
            return str(child["value"])
        stack.extend(child.get("inner", []))
    return None


def parse_enum(node: dict[str, Any], candidate: DeclarationCandidate) -> CppEnum:
    values = tuple(
        CppEnumerator(name=str(child.get("name", "")), value=_enum_value(child))
        for child in node.get("inner", [])
        if child.get("kind") == "EnumConstantDecl"
    )
    return CppEnum(
        namespace=candidate.namespace,
        name=candidate.name,
        location=_location(node, candidate),
        values=values,
        is_scoped=bool(node.get("scopedEnumTag")),
        underlying_type=node.get("fixedUnderlyingType", {}).get("qualType"),
    )


def decode_clang_ast_stream(output: str) -> list[dict[str, Any]]:
    decoder = json.JSONDecoder()
    nodes: list[dict[str, Any]] = []
    offset = 0
    while offset < len(output):
        while offset < len(output) and output[offset].isspace():
            offset += 1
        if offset >= len(output):
            break
        # Clang 10 prefixes every filtered JSON object with a human-readable
        # ``Dumping qualified::name:`` line. Newer Clang versions omit it.
        if output.startswith("Dumping ", offset):
            newline = output.find("\n", offset)
            if newline < 0:
                break
            offset = newline + 1
            continue
        node, offset = decoder.raw_decode(output, offset)
        if isinstance(node, dict):
            nodes.append(node)
    return nodes


def _clang_ast(
    candidate: DeclarationCandidate,
    clang: str,
    include_dirs: Iterable[Path],
    compile_args: Iterable[str],
) -> tuple[dict[str, Any] | None, str]:
    command = [clang, "-std=c++17"]
    for include_dir in include_dirs:
        command.extend(["-I", str(include_dir)])
    command.extend(compile_args)
    command.extend(
        [
            "-Xclang",
            "-ast-dump=json",
            "-Xclang",
            "-ast-dump-filter",
            "-Xclang",
            candidate.qualified_name,
            "-fsyntax-only",
            str(candidate.header),
        ]
    )
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return None, result.stderr.strip()
    try:
        nodes = decode_clang_ast_stream(result.stdout)
    except json.JSONDecodeError as error:
        return None, f"invalid Clang JSON AST stream: {error}"

    expected_kind = "EnumDecl" if candidate.kind.startswith("enum") else "CXXRecordDecl"
    for node in nodes:
        loc = node.get("loc", {})
        if (
            node.get("kind") == expected_kind
            and node.get("name") == candidate.name
            and int(loc.get("line", 0) or 0) == candidate.line
            and (expected_kind != "CXXRecordDecl" or node.get("completeDefinition"))
        ):
            return node, result.stderr.strip()
    return None, (
        f"Clang AST did not contain the expected {expected_kind} "
        f"for {candidate.qualified_name} at line {candidate.line}"
    )


def scan(
    sdk_root: Path,
    headers: Iterable[Path],
    clang: str,
    compile_args: Iterable[str] = (),
) -> ApiInventory:
    resolved_root = sdk_root.resolve()
    resolved_headers = tuple(header.resolve() for header in headers)
    include_dirs = (
        resolved_root / "include",
        resolved_root / "thirdparty" / "include",
        resolved_root / "thirdparty" / "include" / "ddscxx",
    )
    classes: list[CppClass] = []
    enums: list[CppEnum] = []
    diagnostics: list[ScanDiagnostic] = []

    for header in resolved_headers:
        for candidate in discover_declarations(header):
            node, diagnostic = _clang_ast(candidate, clang, include_dirs, compile_args)
            if node is None:
                diagnostics.append(
                    ScanDiagnostic(
                        header=str(header),
                        declaration=candidate.qualified_name,
                        message=diagnostic,
                    )
                )
                continue
            if node.get("kind") == "CXXRecordDecl" and node.get("completeDefinition"):
                classes.append(parse_class(node, candidate))
            elif node.get("kind") == "EnumDecl":
                enums.append(parse_enum(node, candidate))

    inventory_headers: list[str] = []
    for header in resolved_headers:
        try:
            inventory_headers.append(str(header.relative_to(resolved_root)))
        except ValueError:
            inventory_headers.append(str(header))

    return ApiInventory(
        sdk_root=str(resolved_root),
        clang=clang,
        headers=tuple(inventory_headers),
        classes=tuple(classes),
        enums=tuple(enums),
        diagnostics=tuple(diagnostics),
    )


def _headers_from_arguments(sdk_root: Path, values: list[str]) -> list[Path]:
    def is_header(path: Path) -> bool:
        return path.suffix == ".hpp" and not any(
            part.startswith("._") for part in path.parts
        )

    if values:
        headers: list[Path] = []
        for value in values:
            path = Path(value)
            path = path if path.is_absolute() else sdk_root / path
            if path.is_dir():
                headers.extend(
                    sorted(item for item in path.rglob("*.hpp") if is_header(item))
                )
            elif is_header(path):
                headers.append(path)
        return headers
    return sorted(
        item
        for item in (sdk_root / "include" / "unitree").rglob("*.hpp")
        if is_header(item)
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan Unitree SDK2 C++ headers with Clang"
    )
    parser.add_argument("headers", nargs="*", help="Headers relative to the SDK root")
    parser.add_argument("--sdk-root", type=Path, default=Path(__file__).parents[2])
    parser.add_argument("--clang", default="clang++")
    parser.add_argument("--compile-arg", action="append", default=[])
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    headers = _headers_from_arguments(arguments.sdk_root, arguments.headers)
    inventory = scan(
        sdk_root=arguments.sdk_root,
        headers=headers,
        clang=arguments.clang,
        compile_args=arguments.compile_arg,
    )
    payload = json.dumps(inventory.to_dict(), indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    print(
        f"Scanned {len(inventory.headers)} headers: "
        f"{len(inventory.classes)} classes, {len(inventory.enums)} enums, "
        f"{inventory.method_count} methods/constructors, "
        f"{len(inventory.diagnostics)} diagnostics",
        file=sys.stderr,
    )
    return 1 if inventory.diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
