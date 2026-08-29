# Unitree SDK2 C++ signature-preview stubs

Install the wheel to enable completion and static type checking for
`unitree_sdk2_cpp` before the Linux binary extension is available.

From a repository checkout, install the stub project into the same environment
selected by the editor:

```bash
python -m pip install ./stubs
```

Editable installs are also supported:

```bash
python -m pip install -e ./stubs
```

The package includes a design-time placeholder module so Pylance can index
`channel`, `idl`, `robot`, and their public symbols for automatic imports. On a
supported Linux system, the compiled extension takes precedence over that
placeholder at runtime.

`AVAILABLE` signatures exist in the current binding source. `SIGNATURE_ONLY`
signatures are design-time previews and do not provide a runtime implementation.
Hardware and motion APIs can be `AVAILABLE`; that means the runtime entry exists,
not that it is safe to execute. See the packaged `api_manifest.json` for both
availability and safety metadata.

This is a stub-only package: it enables IDE completion and Mypy/Pyright, but it
does not make `import unitree_sdk2_cpp` executable without the Linux extension.
Installing the real extension alongside this wheel supplies the runtime.

The repository also provides a [Chinese beginner guide](../docs/BEGINNER_GUIDE_ZH.md)
and an exhaustive [Chinese API reference](../docs/API_REFERENCE_ZH.md) covering
every generated function, overload, property, parameter, and return value.
