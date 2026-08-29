import re
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "generator"))

from generate_api_docs import GenerationStats, generate, parse_stubs  # noqa: E402


REFERENCE = ROOT / "docs" / "API_REFERENCE_ZH.md"


def test_checked_in_api_reference_is_current(tmp_path: Path) -> None:
    generated = tmp_path / "API_REFERENCE_ZH.md"
    stats = generate(ROOT, generated)

    assert stats == GenerationStats(
        modules=16,
        classes=189,
        functions=867,
        properties=346,
        attributes=173,
        manifest_entries=1213,
    )
    assert generated.read_bytes() == REFERENCE.read_bytes()


def test_every_manifest_entry_has_one_detailed_reference_section() -> None:
    modules, manifest, stats = parse_stubs(ROOT)
    reference = REFERENCE.read_text(encoding="utf-8")

    assert modules
    assert stats.manifest_entries == len(manifest["entries"])
    assert len(re.findall(r"^#### `unitree_sdk2_cpp", reference, re.MULTILINE)) == 1213
    for section in ("参数", "返回值", "用法"):
        assert len(re.findall(rf"^\*\*{section}\*\*$", reference, re.MULTILINE)) == 1213


def test_reference_preserves_runtime_and_motion_boundaries() -> None:
    _, manifest, _ = parse_stubs(ROOT)
    motion_entries = [
        item for item in manifest["entries"] if item.get("safety") == "MOTION_COMMAND"
    ]

    assert len(motion_entries) == 220
    assert {item["status"] for item in motion_entries} == {"AVAILABLE"}

    reference = REFERENCE.read_text(encoding="utf-8")
    assert "def get_uid(self) -> int" in reference
    assert "def get_uid(self: Any)" not in reference
    assert 'initialize(domain_id=0, network_interface="eth0")' in reference
    assert "obj.initialize(domain_id=" not in reference
    assert "写入序列必须正好包含 20 个元素" in reference
    assert "不得从默认测试或未经确认的 Agent 流程调用" in reference
    assert "def compute_crc(message: LowCmd) -> int" in reference
    assert "def lost_connection(" in reference


def test_reference_links_and_markdown_structure_are_consistent() -> None:
    reference = REFERENCE.read_text(encoding="utf-8")
    anchors = re.findall(r'<a id="([^"]+)"></a>', reference)
    links = re.findall(r"\]\(#([^)]+)\)", reference)
    code_fences = sum(line.startswith("```") for line in reference.splitlines())

    assert len(anchors) == len(set(anchors))
    assert set(links) <= set(anchors)
    assert code_fences % 2 == 0
