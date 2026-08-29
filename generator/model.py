from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class BindingStatus(str, Enum):
    SUPPORTED = "SUPPORTED"
    MANUAL = "MANUAL"
    UNSUPPORTED = "UNSUPPORTED"
    IGNORED = "IGNORED"
    MISSING = "MISSING"


@dataclass(frozen=True)
class SourceLocation:
    file: str
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class CppParameter:
    name: str
    type: str
    has_default: bool = False
    default_value: str | None = None


@dataclass(frozen=True)
class CppMethod:
    name: str
    return_type: str
    parameters: tuple[CppParameter, ...] = ()
    access: str = "public"
    is_const: bool = False
    is_static: bool = False
    is_virtual: bool = False
    is_pure_virtual: bool = False
    is_noexcept: bool = False
    is_constructor: bool = False
    location: SourceLocation | None = None

    @property
    def signature(self) -> str:
        parameters = ", ".join(parameter.type for parameter in self.parameters)
        suffix = " const" if self.is_const else ""
        if self.is_noexcept:
            suffix += " noexcept"
        return f"{self.name}({parameters}){suffix}"


@dataclass(frozen=True)
class CppField:
    name: str
    type: str
    access: str
    location: SourceLocation | None = None


@dataclass(frozen=True)
class CppBase:
    type: str
    access: str
    is_virtual: bool = False


@dataclass(frozen=True)
class CppClass:
    namespace: str
    name: str
    kind: str
    location: SourceLocation
    constructors: tuple[CppMethod, ...] = ()
    methods: tuple[CppMethod, ...] = ()
    fields: tuple[CppField, ...] = ()
    bases: tuple[CppBase, ...] = ()
    is_abstract: bool = False
    is_polymorphic: bool = False
    is_trivially_copyable: bool = False
    status: BindingStatus = BindingStatus.MISSING

    @property
    def qualified_name(self) -> str:
        if not self.namespace:
            return self.name
        return f"{self.namespace}::{self.name}"


@dataclass(frozen=True)
class CppEnumerator:
    name: str
    value: str | None = None


@dataclass(frozen=True)
class CppEnum:
    namespace: str
    name: str
    location: SourceLocation
    values: tuple[CppEnumerator, ...] = ()
    is_scoped: bool = False
    underlying_type: str | None = None
    status: BindingStatus = BindingStatus.MISSING

    @property
    def qualified_name(self) -> str:
        if not self.namespace:
            return self.name
        return f"{self.namespace}::{self.name}"


@dataclass(frozen=True)
class ScanDiagnostic:
    header: str
    declaration: str
    message: str


@dataclass(frozen=True)
class ApiInventory:
    sdk_root: str
    clang: str
    headers: tuple[str, ...]
    classes: tuple[CppClass, ...] = ()
    enums: tuple[CppEnum, ...] = ()
    diagnostics: tuple[ScanDiagnostic, ...] = ()
    schema_version: int = 1

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def method_count(self) -> int:
        return sum(len(c.constructors) + len(c.methods) for c in self.classes)
