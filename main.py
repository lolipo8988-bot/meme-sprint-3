#!/usr/bin/env python3
"""Meme Sprint 3 entry program (Python 3.13, standard library only).

The entry image sits beside this file as entry.png (drawn by draw.py).
This program copies it, byte for byte, to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR/entry.png when that variable is set, as it is
outside the grader's container). No network, deterministic output.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("copied entry.png does not match source size")


if __name__ == "__main__":
    main()
