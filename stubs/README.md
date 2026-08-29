# Unitree SDK2 C++ signature-preview stubs

Install the wheel to enable completion and static type checking for
`unitree_sdk2_cpp` before the Linux binary extension is available.

From a repository checkout, install the stub project into the same environment
selected by the editor:

```bash
python -m pip install ./stubs
```

The checked-in `.pyi` tree uses the importable `unitree_sdk2_cpp/` directory
name. This is required by Zed's BasedPyright indexer; the conventional
`unitree_sdk2_cpp-stubs/` directory resolves explicit imports but is skipped
when BasedPyright builds third-party automatic-import candidates.

BasedPyright intentionally does not build automatic-import candidates from this
compiled extension's ordinary `site-packages` entry. To make Zed suggest, for
example, `from unitree_sdk2_cpp import channel` when you type `chan`, add the
checked-out stub source directory to the consuming project's
`pyrightconfig.json`:

```json
{
  "autoImportCompletions": true,
  "indexing": true,
  "include": [
    ".",
    "../unitree_sdk2/unitree_sdk2_bindings/stubs/src"
  ],
  "extraPaths": [
    "../unitree_sdk2/unitree_sdk2_bindings/stubs/src"
  ]
}
```

`include` tells BasedPyright to index the declarations as automatic-import
candidates; `extraPaths` makes their module paths resolve as
`unitree_sdk2_cpp...`. Both entries are required. Adjust the relative path if
the application and SDK repositories are not siblings, then restart Zed's
BasedPyright language server. The path works for the sibling layouts
`/Users/feng/G1Agent` and `/home/qwq/G1Agent` used by this project.

Reinstall the package after changing the generated stubs:

```bash
python -m pip install --force-reinstall ./stubs
```

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
