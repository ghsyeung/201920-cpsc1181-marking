#!/usr/bin/python3

import sys
from pathlib import Path

import util

if len(sys.argv) != 2:
    print("""
Usage: ./scripts/listCompileErrors.py <marking folder>
    """)
    exit(0)

markingFolder = Path(sys.argv[1]).resolve()
if (not markingFolder.exists()):
    print("Invalid marking folder")
    exit(-1)

for i in filter(util.isDir, markingFolder.glob("*")):
    compileOutput: Path = i / "compile.out"
    if not compileOutput.exists():
        print(i.name, "- no compile.out")
    else:
        statResult = compileOutput.stat()
        if statResult.st_size > 0:
            print(i.name)
