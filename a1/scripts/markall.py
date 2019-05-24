#!/usr/bin/python3

import os
import sys

from debug import debug
from extraction import extractStage
from a1compilation import compileStage as a1CompileStage
from a1test import testStage  as a1TestStage

if len(sys.argv) != 3:
    print("""
Usage: ./scripts/markall.py <zipfile> <root folder> 
    """)
    exit(0)

allzip = os.path.abspath(sys.argv[1])
rootDir = os.path.abspath(sys.argv[2])
markingDir = os.path.abspath(rootDir + "/marking")
scratchDir = os.path.abspath(rootDir + "/scratch")

debug(
    "Running with\nzipFile=%s\nrootDir=%s\nmarkingDir=%s\nscratchDir=%s\n" % (allzip, rootDir, markingDir, scratchDir));

studentDirs = extractStage(allzip, rootDir, markingDir, scratchDir)
studentDirs = [studentDirs[0]]

a1CompileStage(markingDir, scratchDir, studentDirs)

a1TestStage(markingDir, scratchDir, studentDirs)
