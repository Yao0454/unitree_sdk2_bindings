"""Generate discoverable source companions without implementing robot APIs."""

from __future__ import annotations

import ast
from pathlib import Path


def generate_source_companions(package: Path) -> None:
    output = package.parent / "unitree_sdk2_cpp"
    for stub in sorted(package.rglob("*.pyi")):
        relative = stub.relative_to(package)
        tree = ast.parse(stub.read_text(encoding="utf-8"))
        declarations: list[str] = []
        functions: set[str] = set()
        for node in tree.body:
            if isinstance(node, ast.ImportFrom) and node.level:
                # Match the real exported namespaces and message aliases.
                if any(alias.asname == alias.name for alias in node.names):
                    declarations.append(ast.unparse(node))
            elif isinstance(node, ast.ClassDef):
                declarations.append(f"class {node.name}:\n    pass")
            elif isinstance(node, ast.FunctionDef):
                if node.name not in functions:
                    declarations.append(f"def {node.name}(*args: Any, **kwargs: Any) -> Any: ...")
                    functions.add(node.name)
            elif isinstance(node, ast.Assign) and isinstance(node.value, ast.Name):
                declarations.append(ast.unparse(node))
        header = (
            '"""Generated source companion. Full types and Chinese help are in the PEP 561 stubs.\n'
            'Robot APIs are provided exclusively by the separately installed native extension.\n'
            '"""\nfrom typing import TYPE_CHECKING, Any\n\nif TYPE_CHECKING:\n'
        )
        body = "\n\n".join(declarations) or "pass"
        source = header + "\n".join("    " + line if line else "" for line in body.splitlines()) + "\n\n"
        if relative == Path("__init__.pyi"):
            source += (Path(__file__).parent / "templates/native_loader.py").read_text(encoding="utf-8")
        else:
            source += (
                'if not TYPE_CHECKING:\n'
                '    raise ImportError("This source companion has no runtime API; install unitree-sdk2-cpp.")\n'
            )
        target = output / relative.with_suffix(".py")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source, encoding="utf-8")
