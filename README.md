# Unitree SDK2 Python bindings

This directory contains a generated pybind11 binding layer. It binds the
SDK-owned `unitree::common::OsHelper` singleton and all 64 DDS message classes
currently shipped under the SDK's Go2, HG, double-IMU, and ROS2 IDL trees.
The `idl.g1` module adds G1-friendly aliases for all 13 HG messages plus SDK-backed
CRC helpers. `robot.g1` exposes all four G1 clients, their 49 public methods, and
the seven official runtime safety checks.
Message fields use copy semantics, so reading or assigning an array, vector, or
nested value does not expose a dangling C++ reference. The operating-system
methods are read-only. Robot command methods are present, but the default tests
only inspect registrations and never construct a Client, initialize DDS, or
send a command.

The repository currently ships Linux ELF libraries for `x86_64` and
`aarch64`. Build and import testing therefore requires one of those Linux
targets; configuration fails explicitly on macOS and other unsupported hosts.

```bash
python -m pip install -e .
python -c "import unitree_sdk2_cpp as u; print(u.OsHelper.instance().get_hostname())"
```

The checked-in IDL binding sources are generated from Clang's JSON AST. The
inventory command accepts individual headers or a directory:

```bash
python generator/scan_headers.py \
  --sdk-root .. \
  --output generated/idl_inventory.json \
  include/unitree/idl

python generator/generate_bindings.py \
  --inventory generated/idl_inventory.json \
  --overrides generator/overrides.yaml \
  --namespace-prefix unitree_go::msg::dds_ \
  --function BindGo2Idl --module idl --module go2 \
  --output src/generated/idl/go2.cpp --report generated/idl_go2_report.json
```

The same generator invocation is used for `BindHgIdl`,
`BindHgDoubleImuIdl`, and `BindRos2Idl`; CMake runs all four when
`-DUNITREE_REGENERATE_BINDINGS=ON` is enabled.

`generated/idl_parity_report.json` records the current binding classification.
It distinguishes generated support from intentional ignored overloads and from
manual, unsupported, or genuinely missing API entries.

Typed DDS channels use an explicit generated registry rather than attempting
to instantiate an arbitrary C++ template at runtime:

```python
from unitree_sdk2_cpp import channel
from unitree_sdk2_cpp.idl.go2 import LowState

channel.initialize(0)
publisher = channel.ChannelPublisher("rt/lowstate", LowState)
publisher.init_channel()
# publisher.write(LowState())
publisher.close_channel()
channel.release()
```

Subscribers copy each DDS sample into a Python-owned message before invoking
the callback. The callback is kept alive by the C++ reader, acquires the GIL
only for the call, and exceptions are reported as unraisable rather than
escaping a DDS worker thread. `channel.initialize` and `publisher.write` are
deliberately absent from the default tests; hardware or network tests must be
opted into explicitly by the caller.

## Robot clients

The robot inventory currently contains 103 headers, 129 classes, one enum,
and 775 methods or constructors. Of the 29 Client classes and 340 public Client
methods, the safety classifier reports:

| Classification | Methods |
| --- | ---: |
| Read-only query | 50 |
| Initialization or lifecycle | 32 |
| Other hardware side effect | 38 |
| Motion command | 220 |

The generated runtime surface exposes 336 of the 340 public Client methods
across 25 concrete SDK Client classes plus `LeaseClient`. This includes all 220
methods classified as motion commands, 50 read-only methods, and 36 methods
with other hardware side effects. The four remaining methods are the abstract
`ClientBase::Init` entry and the three internal `ClientStub` request methods.

The Robot module also exposes 80 parameter/result value classes. The 72
SDK `Jsonize` classes keep their public C++ fields and provide `from_json(dict)`
and `to_json()` wrappers that delegate serialization to the SDK. `LeaseCache`
and `LeaseContext` are available as pure in-memory utility classes; using them
does not initialize DDS.

Direct methods release the GIL while executing C++. Mutable C++ output
references are returned as Python values. The two configuration callbacks keep
their Python callable alive, acquire the GIL on the SDK worker thread, and
report Python exceptions as unraisable instead of unwinding through DDS.

C++ output references are returned with the SDK status code instead of being
represented as mutable Python arguments:

```python
from unitree_sdk2_cpp import channel, robot

channel.initialize(0, "eth0")
client = robot.g1.LocoClient()
client.set_timeout(5.0)
client.init()
status, fsm_id = client.get_fsm_id()
channel.release()
```

Default tests only inspect the registered Python surface; they do not construct
a Client, initialize DDS, contact hardware, invoke a query, or send a command.
Real tests must opt into `hardware`; motion tests must additionally opt into
`motion` and provide their own physical safety procedure.

For Linux developer builds, the same step can be enabled with
`-DUNITREE_REGENERATE_BINDINGS=ON`. Normal wheel builds use the checked-in
generated source, so end users do not need Clang installed.

The wheel installs the CycloneDDS shared libraries beside the extension under
`.libs` and sets the extension RPATH to `$ORIGIN/.libs`. Before distribution,
the Linux build must also prove that `libunitree_sdk2.a` is position-independent
and audit the resulting extension with `readelf`, `ldd`, and an import test.

## Verification

On 2026-08-28 the IDL and typed-channel revision was built on the supplied
Ubuntu 20.04 aarch64 host
(`g++ 9.4.0`, Conda Python 3.10.20). `pip install -e . --no-build-isolation`
completed successfully, the resulting
`unitree_sdk2_cpp.cpython-310-aarch64-linux-gnu.so` imported without setting
`LD_LIBRARY_PATH`. All 64 DDS message classes and all 64 typed publisher and
subscriber registrations loaded successfully. The observed full safe suite
completed with `22 passed in 9.60s`; `readelf` showed
`RUNPATH=$ORIGIN/.libs`, and `ldd`
resolved both CycloneDDS SONAMEs from the wheel's `.libs` directory with no
missing libraries. Verification used only temporary directories and did not
modify the remote SDK checkout.

That result predates the complete generated Robot Client surface. The current
macOS source-level suite reports `33 passed, 4 skipped`; the skipped tests
import the Linux extension. The expanded Robot Client source still requires a
fresh Linux compile, import, and symbol audit before it is considered
binary-verified.

## Signature-preview package

`dist/unitree_sdk2_cpp_stubs-0.3.0-py3-none-any.whl` is a platform-independent
PEP 561 stub wheel for writing application code before the Linux extension is
available:

```bash
python -m pip install dist/unitree_sdk2_cpp_stubs-0.3.0-py3-none-any.whl
```

It covers 64 IDL classes with 341 properties and 121 Robot classes with 634
public methods or constructors, plus `OsHelper` and typed channels. Mypy and
Pyright can therefore check code against `unitree_sdk2_cpp` on macOS, Windows,
or Linux. The wheel is type information only; executing imports still requires
the compiled Linux extension.

The packaged manifest contains 1213 entries: 1167 `AVAILABLE` and 46
`SIGNATURE_ONLY`. G1 contributes five CRC overload entries and seven safety
checks without duplicating the underlying HG message registrations.

Every preview method is marked `AVAILABLE` or `SIGNATURE_ONLY` in its hover
documentation and in the packaged `api_manifest.json`. Motion methods are now
`AVAILABLE`, which means the runtime entry exists, not that calling it is safe.
The manifest retains `MOTION_COMMAND` and `HARDWARE_SIDE_EFFECT` metadata so an
Agent or test harness can enforce an explicit execution policy.

## Documentation

- [Chinese beginner guide](docs/BEGINNER_GUIDE_ZH.md)
- [Complete Chinese API reference](docs/API_REFERENCE_ZH.md)

The API reference is generated from the checked-in `.pyi` files, availability
manifest, and Clang AST inventories. Regenerate it after changing the signature
surface:

```bash
python generator/generate_api_docs.py
```
