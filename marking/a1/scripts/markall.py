import sys
from pathlib import Path

from .a1validate import validateA1
from .a1compilation import getRunTarget, compileRunTarget
from .a1test import runA1Tests
from common.debug import debug
from common.extraction import extractMain, allZipFilesIn, createStudentWorkspace, extractStudent
from common.util import Workspace, StudentWorkspace


def runA1():
    if len(sys.argv) != 3:
        print("""
    Usage: ./scripts/markall.py <zipfile> <root folder> 
        """)
        exit(0)

    mainZip = Path(sys.argv[1])
    rootDir = Path(sys.argv[2])
    if (not rootDir.exists() or not mainZip.exists()):
        print("Invalid rootDir or main zip file")
        exit(-1)

    scratchDir = (rootDir / "scratch").resolve()
    scratchDir.mkdir(exist_ok=True)
    markingDir = (rootDir / "marking").resolve()
    markingDir.mkdir(exist_ok=True)
    testCasesDir: Path = (rootDir / "test_cases").resolve()

    workspace = Workspace(rootDir, scratchDir, markingDir, mainZip, testCasesDir)
    debug("Running with %s" % str(workspace))

    extractMain(workspace, clean=True)

    skipExtract = False

    for submission in allZipFilesIn(workspace.scratchDir)[:]:
        studentWorkspace: StudentWorkspace = createStudentWorkspace(workspace, submission)

        print("Running %s" % studentWorkspace.studentDirName)

        if not skipExtract:
            extractStudent(studentWorkspace)
        runTarget = getRunTarget(studentWorkspace)
        if runTarget:
            compileRunTarget(studentWorkspace, runTarget)
            runA1Tests(studentWorkspace, runTarget, override=True)
            validateA1(workspace.testCasesDir, studentWorkspace, override=True)

        print("\n")
