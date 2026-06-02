from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _run(args: list[str], *, cwd: Path | None = None) -> None:
    print("+ " + " ".join(args), flush=True)
    subprocess.run(args, cwd=cwd, check=True)


def _venv_python(venv: Path) -> Path:
    if sys.platform == "win32":
        return venv / "Scripts" / "python.exe"
    return venv / "bin" / "python"


def _pack_import_name() -> str:
    metadata_path = next((ROOT / "src").glob("*/metadata.json"))
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    return metadata["origin"]["import_name"]


def _default_wheels() -> list[Path]:
    return sorted((ROOT / "dist").glob("*.whl"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a built governance-pack wheel in a clean downstream SSOT repo.")
    parser.add_argument("--wheel", nargs="+", type=Path, default=_default_wheels(), help="Built wheel path(s) to install.")
    parser.add_argument(
        "--ssot-registry-requirement",
        default=os.environ.get("SSOT_REGISTRY_REQUIREMENT", "ssot-registry>=0.2.22,<0.3.0"),
        help="ssot-registry package requirement to validate against.",
    )
    parser.add_argument("--ssot-registry-version", help="Exact ssot-registry version to validate against.")
    args = parser.parse_args()
    ssot_registry_requirement = args.ssot_registry_requirement
    if args.ssot_registry_version:
        ssot_registry_requirement = f"ssot-registry=={args.ssot_registry_version}"

    wheels = [path.resolve() for path in args.wheel]
    if not wheels:
        raise SystemExit("No wheel files found. Build the package into dist/ first.")
    for wheel in wheels:
        if not wheel.exists():
            raise SystemExit(f"Wheel not found: {wheel}")

    with tempfile.TemporaryDirectory(prefix="governance-pack-gate-") as temp:
        temp_path = Path(temp)
        venv = temp_path / "venv"
        downstream = temp_path / "downstream"
        downstream.mkdir()
        python = _venv_python(venv)

        _run([sys.executable, "-m", "venv", str(venv)])
        _run([str(python), "-m", "pip", "install", "--upgrade", "pip"])
        _run([str(python), "-m", "pip", "install", ssot_registry_requirement, *map(str, wheels)])
        _run([str(python), "-m", "ssot_registry", "init", str(downstream), "--force"])
        _run([str(python), "-m", "ssot_registry", "pack", "sync", str(downstream), _pack_import_name(), "--all", "--trust", "--yes"])
        _run([str(python), "-m", "ssot_registry", "validate", str(downstream)])


if __name__ == "__main__":
    main()
