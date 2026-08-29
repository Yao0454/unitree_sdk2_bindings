"""Generate Unitree robot Client bindings with explicit safety metadata."""

from __future__ import annotations

import argparse
import json
import keyword
import re
from collections import Counter
from pathlib import Path
from typing import Any


CLIENT_BASE = "unitree::robot::Client"
CLIENT_BASE_BASE = "unitree::robot::ClientBase"
LEASE_CLIENT = "unitree::robot::LeaseClient"
SUPPORTED_STRATEGIES = {"CALLBACK_MANUAL", "DIRECT", "OUTPUT_WRAPPER"}
JSONIZE_BASES = {"common::Jsonize", "unitree::common::Jsonize"}


def qualified_name(item: dict[str, Any]) -> str:
    namespace = item.get("namespace", "")
    return f"{namespace}::{item['name']}" if namespace else item["name"]


def method_signature(method: dict[str, Any]) -> str:
    parameters = ", ".join(item["type"] for item in method["parameters"])
    suffix = " const" if method.get("is_const") else ""
    return f"{method['name']}({parameters}){suffix}"


def snake_case(name: str) -> str:
    first_pass = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first_pass).lower()


def python_identifier(name: str) -> str:
    return name + "_" if keyword.iskeyword(name) else name


def header_include(cpp_class: dict[str, Any], sdk_root: Path) -> str:
    header = Path(cpp_class["location"]["file"])
    if not header.is_absolute():
        header = sdk_root / header
    include_root = sdk_root / "include"
    try:
        return str(header.resolve().relative_to(include_root.resolve()))
    except ValueError as error:
        raise ValueError(
            f"header is outside SDK include directory: {header}"
        ) from error


def is_mutable_output(type_name: str) -> bool:
    return "&" in type_name and not type_name.lstrip().startswith("const ")


def value_type(type_name: str) -> str:
    result = type_name.strip()
    result = re.sub(r"\bconst\s+", "", result)
    result = re.sub(r"\s*&&?\s*$", "", result)
    return result.strip()


def qualify_local_types(
    type_name: str,
    namespace: str,
    classes_by_name: dict[str, dict[str, Any]],
) -> str:
    result = type_name
    for candidate in classes_by_name.values():
        if candidate.get("namespace") != namespace:
            continue
        name = candidate["name"]
        result = re.sub(
            rf"(?<![A-Za-z0-9_:]){re.escape(name)}(?![A-Za-z0-9_])",
            qualified_name(candidate),
            result,
        )
    return result


def module_variable(namespace: str) -> str:
    suffix = namespace.removeprefix("unitree::robot").strip(":")
    return "robot" if not suffix else "robot_" + suffix.replace("::", "_")


def parameter_name(parameter: dict[str, Any], index: int) -> str:
    return parameter.get("name") or f"arg{index}"


def python_parameter_name(parameter: dict[str, Any], index: int) -> str:
    return python_identifier(snake_case(parameter_name(parameter, index)))


def default_argument(parameter: dict[str, Any], context: str) -> str:
    if not parameter.get("has_default"):
        return ""
    value = parameter.get("default_value")
    if value is None:
        raise ValueError(f"unsupported default argument in {context}")
    return f" = {value}"


def output_suffix(method: dict[str, Any]) -> str:
    for parameter in method.get("parameters", []):
        if not is_mutable_output(parameter["type"]):
            continue
        normalized = value_type(parameter["type"])
        if normalized.startswith(("std::vector<", "std::map<")):
            normalized = normalized.split("<", 1)[0]
        return snake_case(normalized.rsplit("::", 1)[-1])
    return "result"


def method_python_names(
    methods: list[tuple[dict[str, Any], dict[str, Any]]],
    mutable_inputs: set[str],
) -> list[str]:
    base_names = [
        python_identifier(snake_case(method["name"])) for method, _ in methods
    ]
    input_shapes: list[tuple[str, ...]] = []
    for method, report in methods:
        signature = method_signature(method)
        output_wrapper = (
            report["binding_strategy"] == "OUTPUT_WRAPPER"
            and signature not in mutable_inputs
        )
        input_shapes.append(
            tuple(
                parameter["type"]
                for parameter in method["parameters"]
                if not (output_wrapper and is_mutable_output(parameter["type"]))
            )
        )
    counts = Counter(zip(base_names, input_shapes, strict=True))
    return [
        (
            f"{base_name}_{output_suffix(method)}"
            if report["binding_strategy"] == "OUTPUT_WRAPPER"
            and method_signature(method) not in mutable_inputs
            and counts[(base_name, shape)] > 1
            else base_name
        )
        for (method, report), base_name, shape in zip(
            methods, base_names, input_shapes, strict=True
        )
    ]


def render_direct_method(
    cpp_class: dict[str, Any],
    method: dict[str, Any],
    python_name: str,
    classes_by_name: dict[str, dict[str, Any]],
    mutable_input: bool = False,
    release_gil: bool = True,
) -> list[str]:
    cpp_name = qualified_name(cpp_class)
    parameters: list[tuple[str, str, str]] = []
    for index, parameter in enumerate(method["parameters"]):
        name = parameter_name(parameter, index)
        type_name = qualify_local_types(
            parameter["type"], cpp_class["namespace"], classes_by_name
        )
        if mutable_input and is_mutable_output(type_name):
            type_name = value_type(type_name)
        parameters.append((type_name, name, python_parameter_name(parameter, index)))

    lambda_parameters = [f"{cpp_name}& self"] + [
        f"{type_name} {name}" for type_name, name, _ in parameters
    ]
    call = f"self.{method['name']}({', '.join(name for _, name, _ in parameters)})"
    lines = [
        f'  {module_variable(cpp_class["namespace"])}_{cpp_class["name"]}.def(',
        f'      "{python_name}",',
        f"      []({', '.join(lambda_parameters)}) {{",
    ]
    return_type = qualify_local_types(
        method["return_type"], cpp_class["namespace"], classes_by_name
    )
    if return_type == "void":
        if release_gil:
            lines.append("        py::gil_scoped_release release;")
        lines.extend([f"        {call};", "      }"])
    else:
        if release_gil:
            lines.append("        py::gil_scoped_release release;")
        lines.extend([f"        return {call};", "      }"])
    context = f"{cpp_name}::{method_signature(method)}"
    for index, (_, _, python_name_value) in enumerate(parameters):
        lines[-1] += f', py::arg("{python_name_value}")'
        lines[-1] += default_argument(method["parameters"][index], context)
    lines[-1] += ");"
    return lines


def render_output_method(
    cpp_class: dict[str, Any],
    method: dict[str, Any],
    classes_by_name: dict[str, dict[str, Any]],
    python_name: str,
) -> list[str]:
    cpp_name = qualified_name(cpp_class)
    inputs: list[tuple[str, str]] = []
    outputs: list[tuple[str, str]] = []
    call_arguments: list[str] = []
    reserved_names = {"status"}
    for index, parameter in enumerate(method["parameters"]):
        name = parameter_name(parameter, index)
        parameter_type = qualify_local_types(
            parameter["type"], cpp_class["namespace"], classes_by_name
        )
        if is_mutable_output(parameter["type"]):
            if not parameter.get("name") or name in reserved_names:
                name = f"output_{index}"
            outputs.append((value_type(parameter_type), name))
        else:
            inputs.append((parameter_type, name))
        reserved_names.add(name)
        call_arguments.append(name)

    if not outputs:
        raise ValueError(
            f"read-only wrapper has no output: {cpp_name}::{method_signature(method)}"
        )
    if method["return_type"] == "void":
        raise ValueError(
            f"void output wrapper needs a separate policy: {cpp_name}::{method_signature(method)}"
        )

    lambda_parameters = [f"{cpp_name}& self"] + [
        f"{type_name} {name}" for type_name, name in inputs
    ]
    return_type = qualify_local_types(
        method["return_type"], cpp_class["namespace"], classes_by_name
    )
    output_names = [name for _, name in outputs]
    lines = [
        f'  {module_variable(cpp_class["namespace"])}_{cpp_class["name"]}.def(',
        f'      "{python_name}",',
        f"      []({', '.join(lambda_parameters)}) {{",
    ]
    lines.extend(f"        {type_name} {name}{{}};" for type_name, name in outputs)
    lines.extend(
        [
            f"        {return_type} status{{}};",
            "        {",
            "          py::gil_scoped_release release;",
            f"          status = self.{method['name']}({', '.join(call_arguments)});",
            "        }",
            "        return py::make_tuple(",
            "            status, "
            + ", ".join(f"std::move({name})" for name in output_names)
            + ");",
            "      }",
        ]
    )
    context = f"{cpp_name}::{method_signature(method)}"
    input_parameters = [
        parameter
        for parameter in method["parameters"]
        if not is_mutable_output(parameter["type"])
    ]
    for index, (_, name) in enumerate(inputs):
        lines[-1] += f', py::arg("{python_identifier(snake_case(name))}")'
        lines[-1] += default_argument(input_parameters[index], context)
    output_description = ", ".join(["status", *output_names])
    lines[-1] += f', "Returns ({output_description}).");'
    return lines


def render_callback_method(
    cpp_class: dict[str, Any], method: dict[str, Any], python_name: str
) -> list[str]:
    if method["name"] != "SubscribeChangeStatus" or len(method["parameters"]) != 2:
        raise ValueError(
            "callback requires a manual renderer: "
            f"{qualified_name(cpp_class)}::{method_signature(method)}"
        )
    cpp_name = qualified_name(cpp_class)
    variable = f"{module_variable(cpp_class['namespace'])}_{cpp_class['name']}"
    return [
        f"  {variable}.def(",
        f'      "{python_name}",',
        f"      []({cpp_name}& self, const std::string& name, py::function callback) {{",
        "        auto guarded_callback =",
        "            [callback = std::move(callback)](const std::string& key,",
        "                                             const std::string& status) {",
        "              py::gil_scoped_acquire acquire;",
        "              try {",
        "                callback(key, status);",
        "              } catch (py::error_already_set& error) {",
        f'                error.discard_as_unraisable("{cpp_name}.{python_name}");',
        "              }",
        "            };",
        "        py::gil_scoped_release release;",
        "        self.SubscribeChangeStatus(name, guarded_callback);",
        "      },",
        '      py::arg("name"), py::arg("callback"));',
    ]


def discover_value_classes(
    selected: list[tuple[dict[str, Any], list[tuple[dict[str, Any], dict[str, Any]]]]],
    classes_by_name: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for cpp_class, methods in selected:
        for method, _ in methods:
            for parameter in method.get("parameters", []):
                for candidate in classes_by_name.values():
                    if candidate.get("namespace") != cpp_class["namespace"]:
                        continue
                    if re.search(
                        rf"\b{re.escape(candidate['name'])}\b", parameter["type"]
                    ):
                        result[qualified_name(candidate)] = candidate
                if "PathPoint" in parameter["type"]:
                    alias = classes_by_name.get(
                        f"{cpp_class['namespace']}::stPathPoint"
                    )
                    if alias is not None:
                        result[qualified_name(alias)] = alias

    # Both B2 and Go2 publish PathPoint in their public headers. Go2 currently
    # has no Client method using it, but registering the alias keeps the two
    # robot modules consistent and makes the public value type usable.
    go2_path = classes_by_name.get("unitree::robot::go2::stPathPoint")
    if go2_path is not None:
        result[qualified_name(go2_path)] = go2_path

    # Jsonize-derived objects are the SDK's concrete RPC parameter/result
    # types. Bind the C++ objects themselves and only adapt the JSON boundary.
    for candidate in classes_by_name.values():
        if any(base["type"] in JSONIZE_BASES for base in candidate.get("bases", [])):
            result[qualified_name(candidate)] = candidate

    # Pull in value types used by public fields (for example H2 FsmIdInfo).
    # pybind11's STL casters can resolve registrations after module creation,
    # so a deterministic name order is sufficient here.
    changed = True
    while changed:
        changed = False
        for value_class in list(result.values()):
            for field in value_class.get("fields", []):
                if field.get("access") != "public":
                    continue
                for candidate in classes_by_name.values():
                    if candidate.get("namespace") != value_class.get("namespace"):
                        continue
                    if not re.search(
                        rf"\b{re.escape(candidate['name'])}\b", field["type"]
                    ):
                        continue
                    cpp_name = qualified_name(candidate)
                    if cpp_name not in result:
                        result[cpp_name] = candidate
                        changed = True
    return [result[name] for name in sorted(result)]


def is_json_value_class(cpp_class: dict[str, Any]) -> bool:
    return any(
        base["type"] in JSONIZE_BASES for base in cpp_class.get("bases", [])
    )


def public_constructors(cpp_class: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        constructor
        for constructor in cpp_class.get("constructors", [])
        if constructor.get("access") == "public"
    ]


def has_generated_default_constructor(cpp_class: dict[str, Any]) -> bool:
    return not public_constructors(cpp_class) and (
        cpp_class.get("kind") == "struct" or is_json_value_class(cpp_class)
    )


def generate(
    inventory: dict[str, Any], classification: dict[str, Any], policy: dict[str, Any]
) -> tuple[str, dict[str, Any]]:
    sdk_root = Path(inventory["sdk_root"])
    classes_by_name = {qualified_name(item): item for item in inventory["classes"]}
    selected: list[
        tuple[dict[str, Any], list[tuple[dict[str, Any], dict[str, Any]]]]
    ] = []
    mutable_input_policy = {
        cpp_name: set(signatures)
        for cpp_name, signatures in policy.get("mutable_inputs", {}).items()
    }
    utility_policy = {
        cpp_name: set(signatures)
        for cpp_name, signatures in policy.get("utility_classes", {}).items()
    }
    utility_classes: list[
        tuple[dict[str, Any], list[dict[str, Any]]]
    ] = []
    unmatched_utilities: set[tuple[str, str]] = set()
    for cpp_name, signatures in utility_policy.items():
        cpp_class = classes_by_name.get(cpp_name)
        public_methods = {
            method_signature(method): method
            for method in (cpp_class or {}).get("methods", [])
            if method.get("access") == "public"
        }
        unmatched_utilities.update(
            (cpp_name, signature) for signature in signatures - public_methods.keys()
        )
        if cpp_class is not None:
            utility_classes.append(
                (
                    cpp_class,
                    [
                        public_methods[signature]
                        for signature in signatures
                        if signature in public_methods
                    ],
                )
            )
    if unmatched_utilities:
        formatted = ", ".join(
            f"{cpp_name}::{signature}"
            for cpp_name, signature in sorted(unmatched_utilities)
        )
        raise ValueError("utility policy entries are missing: " + formatted)
    utility_classes.sort(key=lambda item: qualified_name(item[0]))

    unmatched_policy = {
        (cpp_name, signature)
        for cpp_name, signatures in policy.get("classes", {}).items()
        for signature in signatures
    }
    for client_report in classification["clients"]:
        cpp_name = client_report["qualified_name"]
        cpp_class = classes_by_name.get(cpp_name)
        if cpp_class is None or cpp_name in {
            CLIENT_BASE,
            CLIENT_BASE_BASE,
            LEASE_CLIENT,
        }:
            continue
        bases = {base["type"] for base in cpp_class.get("bases", [])}
        if CLIENT_BASE not in bases:
            continue
        report_methods = {
            (item["name"], item["signature"]): item
            for item in client_report["methods"]
            if item["binding_strategy"] in SUPPORTED_STRATEGIES
        }
        methods = [
            (method, report_methods[(method["name"], method_signature(method))])
            for method in cpp_class["methods"]
            if (method["name"], method_signature(method)) in report_methods
        ]
        for method, report in methods:
            signature = method_signature(method)
            if (
                signature in policy.get("classes", {}).get(cpp_name, [])
                and report["safety"] == "READ_ONLY"
                and report["binding_strategy"] == "OUTPUT_WRAPPER"
            ):
                unmatched_policy.discard((cpp_name, signature))
        if methods:
            selected.append((cpp_class, methods))

    if unmatched_policy:
        formatted = ", ".join(
            f"{cpp_name}::{signature}"
            for cpp_name, signature in sorted(unmatched_policy)
        )
        raise ValueError(
            "policy entries are missing or no longer classified as safe read-only: "
            + formatted
        )

    unmatched_mutable_inputs: set[tuple[str, str]] = set()
    for cpp_name, signatures in mutable_input_policy.items():
        cpp_class = classes_by_name.get(cpp_name)
        known = {
            method_signature(method)
            for method in (cpp_class or {}).get("methods", [])
            if method.get("access") == "public"
        }
        unmatched_mutable_inputs.update(
            (cpp_name, signature) for signature in signatures - known
        )
    if unmatched_mutable_inputs:
        formatted = ", ".join(
            f"{cpp_name}::{signature}"
            for cpp_name, signature in sorted(unmatched_mutable_inputs)
        )
        raise ValueError("mutable input policy entries are missing: " + formatted)

    selected.sort(key=lambda item: qualified_name(item[0]))
    value_classes = discover_value_classes(selected, classes_by_name)
    enums = [
        item
        for item in inventory.get("enums", [])
        if any(
            qualified_name(item) in parameter["type"]
            for _, methods in selected
            for method, _ in methods
            for parameter in method.get("parameters", [])
        )
    ]
    includes = {
        "unitree/robot/client/client.hpp",
        "unitree/robot/client/lease_client.hpp",
        *(header_include(item, sdk_root) for item, _ in selected),
        *(header_include(item, sdk_root) for item in value_classes),
        *(header_include(item, sdk_root) for item in enums),
        *(header_include(item, sdk_root) for item, _ in utility_classes),
    }
    namespaces = sorted(
        {item["namespace"] for item, _ in selected}
        | {item["namespace"] for item, _ in utility_classes}
        | {item["namespace"] for item in value_classes}
        | {item["namespace"] for item in enums}
    )

    lines = [
        "// Generated by generator/generate_robot_read_only_bindings.py. Do not edit manually.",
        '#include "bindings.hpp"',
        "",
        "#include <utility>",
        "#include <pybind11/functional.h>",
        "#include <pybind11/stl.h>",
        "",
        *(f"#include <{header}>" for header in sorted(includes)),
        "",
        "namespace py = pybind11;",
        "",
        "void BindRobotClients(py::module_& root) {",
        '  py::module_ robot = EnsureSubmodule(root, "robot");',
        "",
        f'  py::class_<{CLIENT_BASE_BASE}>(robot, "ClientBase")',
        '      .def("set_timeout",',
        f"           py::overload_cast<float>(&{CLIENT_BASE_BASE}::SetTimeout),",
        '           py::arg("seconds"))',
        '      .def("set_timeout_microseconds",',
        f"           py::overload_cast<int64_t>(&{CLIENT_BASE_BASE}::SetTimeout),",
        '           py::arg("microseconds"));',
        "",
        f'  py::class_<{CLIENT_BASE}, {CLIENT_BASE_BASE}>(robot, "Client")',
        '      .def("wait_lease_applied",',
        f"           []({CLIENT_BASE}& self) {{",
        "             py::gil_scoped_release release;",
        "             self.WaitLeaseApplied();",
        "           })",
        '      .def("get_api_version",',
        f"           [](const {CLIENT_BASE}& self) {{",
        "             return std::string(self.GetApiVersion());",
        "           })",
        '      .def("get_server_api_version",',
        f"           []({CLIENT_BASE}& self) {{",
        "             py::gil_scoped_release release;",
        "             return self.GetServerApiVersion();",
        "           });",
        "",
        f'  py::class_<{LEASE_CLIENT}, {CLIENT_BASE_BASE}>(robot, "LeaseClient")',
        '      .def(py::init<const std::string&>(), py::arg("name"))',
        '      .def("init",',
        f"           []({LEASE_CLIENT}& self) {{",
        "             py::gil_scoped_release release;",
        "             self.Init();",
        "           })",
        '      .def("wait_applied",',
        f"           []({LEASE_CLIENT}& self) {{",
        "             py::gil_scoped_release release;",
        "             self.WaitApplied();",
        "           })",
        f'      .def("get_id", &{LEASE_CLIENT}::GetId)',
        f'      .def("applied", &{LEASE_CLIENT}::Applied);',
        "",
    ]

    for namespace in namespaces:
        if namespace == "unitree::robot":
            continue
        path = namespace.removeprefix("unitree::robot::").split("::")
        parent = "robot"
        prefix: list[str] = []
        for part in path:
            prefix.append(part)
            variable = "robot_" + "_".join(prefix)
            if not any(line.startswith(f"  py::module_ {variable} ") for line in lines):
                lines.append(
                    f'  py::module_ {variable} = EnsureSubmodule({parent}, "{part}");'
                )
            parent = variable
    lines.append("")

    for cpp_enum in enums:
        cpp_name = qualified_name(cpp_enum)
        variable = f"{module_variable(cpp_enum['namespace'])}_{cpp_enum['name']}"
        lines.append(
            f"  py::enum_<{cpp_name}> {variable}("
            f'{module_variable(cpp_enum["namespace"])}, "{cpp_enum["name"]}");'
        )
        for enumerator in cpp_enum.get("values", []):
            lines.append(
                f'  {variable}.value("{enumerator["name"]}", '
                f"{cpp_name}::{enumerator['name']});"
            )
        lines.append(f"  {variable}.export_values();")
        lines.append("")

    for value_class in value_classes:
        cpp_name = qualified_name(value_class)
        variable = f"{module_variable(value_class['namespace'])}_{value_class['name']}"
        lines.append(
            f"  py::class_<{cpp_name}> {variable}("
            f'{module_variable(value_class["namespace"])}, "{value_class["name"]}");'
        )
        constructors = public_constructors(value_class)
        if has_generated_default_constructor(value_class):
            lines.append(f"  {variable}.def(py::init<>());")
        for constructor in constructors:
            parameter_types = [
                qualify_local_types(
                    parameter["type"], value_class["namespace"], classes_by_name
                )
                for parameter in constructor["parameters"]
            ]
            definition = f"  {variable}.def(py::init<{', '.join(parameter_types)}>()"
            context = f"{cpp_name}::{method_signature(constructor)}"
            for index, parameter in enumerate(constructor["parameters"]):
                definition += (
                    f', py::arg("{python_parameter_name(parameter, index)}")'
                    + default_argument(parameter, context)
                )
            lines.append(definition + ");")
        for field in value_class.get("fields", []):
            if field["access"] == "public":
                lines.append(
                    f'  {variable}.def_readwrite("{snake_case(field["name"])}", '
                    f"&{cpp_name}::{field['name']});"
                )
        if is_json_value_class(value_class):
            lines.extend(
                [
                    f'  {variable}.def("from_json",',
                    f"      []({cpp_name}& self, const py::dict& value) {{",
                    "        const std::string serialized =",
                    '            py::module_::import("json").attr("dumps")(value).cast<std::string>();',
                    "        unitree::common::JsonMap json;",
                    "        unitree::common::FromJsonString(serialized, json);",
                    "        self.fromJson(json);",
                    "      },",
                    '      py::arg("value"));',
                    f'  {variable}.def("to_json",',
                    f"      [](const {cpp_name}& self) {{",
                    "        unitree::common::JsonMap json;",
                    "        self.toJson(json);",
                    "        return py::module_::import(\"json\").attr(\"loads\")(",
                    "            unitree::common::ToJsonString(json));",
                    "      });",
                ]
            )
        if value_class["name"] == "stPathPoint":
            lines.append(
                f'  {module_variable(value_class["namespace"])}.attr("PathPoint") = '
                f'{module_variable(value_class["namespace"])}.attr("stPathPoint");'
            )
        lines.append("")

    utility_class_reports: list[dict[str, Any]] = []
    for utility_class, methods in utility_classes:
        cpp_name = qualified_name(utility_class)
        variable = f"{module_variable(utility_class['namespace'])}_{utility_class['name']}"
        lines.append(
            f"  py::class_<{cpp_name}> {variable}("
            f'{module_variable(utility_class["namespace"])}, "{utility_class["name"]}");'
        )
        constructors = public_constructors(utility_class)
        for constructor in constructors:
            parameter_types = [
                qualify_local_types(
                    parameter["type"], utility_class["namespace"], classes_by_name
                )
                for parameter in constructor["parameters"]
            ]
            definition = f"  {variable}.def(py::init<{', '.join(parameter_types)}>()"
            context = f"{cpp_name}::{method_signature(constructor)}"
            for index, parameter in enumerate(constructor["parameters"]):
                definition += (
                    f', py::arg("{python_parameter_name(parameter, index)}")'
                    + default_argument(parameter, context)
                )
            lines.append(definition + ");")
        method_reports: list[dict[str, Any]] = []
        for method in sorted(methods, key=method_signature):
            python_name = python_identifier(snake_case(method["name"]))
            lines.extend(
                render_direct_method(
                    utility_class,
                    method,
                    python_name,
                    classes_by_name,
                    release_gil=False,
                )
            )
            method_reports.append(
                {
                    "cpp_signature": method_signature(method),
                    "python_name": python_name,
                    "safety": "VALUE_TYPE",
                    "binding_strategy": "DIRECT",
                }
            )
        lines.append("")
        utility_class_reports.append(
            {
                "qualified_name": cpp_name,
                "python_module": "unitree_sdk2_cpp."
                + utility_class["namespace"]
                .removeprefix("unitree::")
                .replace("::", "."),
                "python_name": utility_class["name"],
                "status": "AVAILABLE_UTILITY",
                "constructors": [
                    method_signature(constructor) for constructor in constructors
                ],
                "methods": method_reports,
            }
        )

    class_reports: list[dict[str, Any]] = [
        {
            "qualified_name": LEASE_CLIENT,
            "python_module": "unitree_sdk2_cpp.robot",
            "python_name": "LeaseClient",
            "status": "AVAILABLE",
            "constructors": ["LeaseClient(const std::string &)"],
            "methods": [
                {
                    "cpp_signature": "Init()",
                    "python_name": "init",
                    "safety": "INITIALIZATION",
                    "binding_strategy": "DIRECT",
                },
                {
                    "cpp_signature": "WaitApplied()",
                    "python_name": "wait_applied",
                    "safety": "INITIALIZATION",
                    "binding_strategy": "DIRECT",
                },
                {
                    "cpp_signature": "GetId()",
                    "python_name": "get_id",
                    "safety": "READ_ONLY",
                    "binding_strategy": "DIRECT",
                },
                {
                    "cpp_signature": "Applied()",
                    "python_name": "applied",
                    "safety": "READ_ONLY",
                    "binding_strategy": "DIRECT",
                },
            ],
        }
    ]
    for cpp_class, methods in selected:
        cpp_name = qualified_name(cpp_class)
        variable = f"{module_variable(cpp_class['namespace'])}_{cpp_class['name']}"
        lines.extend(
            [
                f"  py::class_<{cpp_name}, {CLIENT_BASE}> {variable}(",
                f'      {module_variable(cpp_class["namespace"])}, "{cpp_class["name"]}");',
            ]
        )
        constructors = [
            constructor
            for constructor in cpp_class.get("constructors", [])
            if constructor.get("access") == "public"
        ]
        for constructor in constructors:
            parameter_types = [
                qualify_local_types(
                    parameter["type"], cpp_class["namespace"], classes_by_name
                )
                for parameter in constructor["parameters"]
            ]
            definition = f"  {variable}.def(py::init<{', '.join(parameter_types)}>()"
            context = f"{cpp_name}::{method_signature(constructor)}"
            for index, parameter in enumerate(constructor["parameters"]):
                definition += (
                    f', py::arg("{python_parameter_name(parameter, index)}")'
                    + default_argument(parameter, context)
                )
            lines.append(definition + ");")

        mutable_inputs = mutable_input_policy.get(cpp_name, set())
        python_names = method_python_names(methods, mutable_inputs)
        method_reports: list[dict[str, Any]] = []
        for (method, classification_method), python_name in zip(
            methods, python_names, strict=True
        ):
            signature = method_signature(method)
            strategy = classification_method["binding_strategy"]
            if signature in mutable_inputs:
                lines.extend(
                    render_direct_method(
                        cpp_class,
                        method,
                        python_name,
                        classes_by_name,
                        mutable_input=True,
                    )
                )
                strategy = "MUTABLE_INPUT_COPY"
            elif strategy == "DIRECT":
                lines.extend(
                    render_direct_method(
                        cpp_class, method, python_name, classes_by_name
                    )
                )
            elif strategy == "OUTPUT_WRAPPER":
                lines.extend(
                    render_output_method(
                        cpp_class, method, classes_by_name, python_name
                    )
                )
            elif strategy == "CALLBACK_MANUAL":
                lines.extend(render_callback_method(cpp_class, method, python_name))
            else:
                raise ValueError(
                    f"unsupported strategy {strategy}: {cpp_name}::{signature}"
                )
            method_reports.append(
                {
                    "cpp_signature": signature,
                    "python_name": python_name,
                    "safety": classification_method["safety"],
                    "binding_strategy": strategy,
                }
            )
        lines.append("")
        class_reports.append(
            {
                "qualified_name": cpp_name,
                "python_module": "unitree_sdk2_cpp."
                + cpp_class["namespace"].removeprefix("unitree::").replace("::", "."),
                "python_name": cpp_class["name"],
                "status": "AVAILABLE",
                "constructors": [
                    method_signature(constructor) for constructor in constructors
                ],
                "methods": method_reports,
            }
        )

    lines.extend(["}", ""])
    method_count = sum(len(methods) for _, methods in selected) + 10
    value_class_reports = []
    for item in value_classes:
        constructors = public_constructors(item)
        constructor_signatures = [method_signature(value) for value in constructors]
        if has_generated_default_constructor(item):
            constructor_signatures.append(f"{item['name']}()")
        methods = []
        if is_json_value_class(item):
            for method in item.get("methods", []):
                if method.get("access") != "public" or method["name"] not in {
                    "fromJson",
                    "toJson",
                }:
                    continue
                methods.append(
                    {
                        "cpp_signature": method_signature(method),
                        "python_name": snake_case(method["name"]),
                        "safety": "VALUE_TYPE",
                        "binding_strategy": (
                            "JSON_DICT_INPUT"
                            if method["name"] == "fromJson"
                            else "JSON_DICT_OUTPUT"
                        ),
                    }
                )
        value_class_reports.append(
            {
                "qualified_name": qualified_name(item),
                "python_module": "unitree_sdk2_cpp."
                + item["namespace"].removeprefix("unitree::").replace("::", "."),
                "python_name": item["name"],
                "status": "AVAILABLE_VALUE",
                "aliases": ["PathPoint"] if item["name"] == "stPathPoint" else [],
                "constructors": constructor_signatures,
                "methods": methods,
            }
        )
    bound_method_keys = {
        (item["qualified_name"], method["cpp_signature"])
        for item in class_reports
        for method in item.get("methods", [])
    } | {
        (CLIENT_BASE_BASE, "SetTimeout(int64_t)"),
        (CLIENT_BASE_BASE, "SetTimeout(float)"),
        (CLIENT_BASE, "WaitLeaseApplied()"),
        (CLIENT_BASE, "GetApiVersion() const"),
        (CLIENT_BASE, "GetServerApiVersion()"),
    }
    unbound_methods = [
        {
            "qualified_name": client["qualified_name"],
            **method,
        }
        for client in classification["clients"]
        for method in client["methods"]
        if (client["qualified_name"], method["signature"])
        not in bound_method_keys
    ]
    report = {
        "schema_version": 2,
        "sources": [
            "generated/robot_binding_report.json",
            "generator/robot_read_only_policy.json",
        ],
        "summary": {
            "client_classes": len(selected) + 1,
            "client_methods": method_count,
            "unbound_methods": len(unbound_methods),
            "read_only_methods": sum(
                1
                for _, methods in selected
                for _, item in methods
                if item["safety"] == "READ_ONLY"
            )
            + 5,
            "motion_methods_exposed": sum(
                1
                for _, methods in selected
                for _, item in methods
                if item["safety"] == "MOTION_COMMAND"
            ),
            "hardware_side_effect_methods_exposed": sum(
                1
                for _, methods in selected
                for _, item in methods
                if item["safety"] == "HARDWARE_SIDE_EFFECT"
            ),
            "value_classes": len(value_classes),
            "value_methods": sum(
                len(item.get("methods", [])) for item in value_class_reports
            ),
            "utility_classes": len(utility_class_reports),
            "utility_methods": sum(
                len(item.get("methods", [])) for item in utility_class_reports
            ),
            "enums": len(enums),
        },
        "classes": class_reports,
        "value_classes": value_class_reports,
        "utility_classes": utility_class_reports,
        "unbound_methods": unbound_methods,
    }
    return "\n".join(lines), report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--classification", type=Path, required=True)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    arguments = parser.parse_args()

    inventory = json.loads(arguments.inventory.read_text(encoding="utf-8"))
    classification = json.loads(arguments.classification.read_text(encoding="utf-8"))
    policy = json.loads(arguments.policy.read_text(encoding="utf-8"))
    source, report = generate(inventory, classification, policy)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(source, encoding="utf-8")
    arguments.report.parent.mkdir(parents=True, exist_ok=True)
    arguments.report.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"Generated {report['summary']['client_methods']} methods "
        f"for {report['summary']['client_classes']} clients"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
