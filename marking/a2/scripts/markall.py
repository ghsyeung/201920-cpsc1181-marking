import sys
from pathlib import Path

from .a2compilation import getRunTarget, compileRunTarget, copyA2TestFiles
from .a2test import runA2Tests
from .a2validate import validateA2
from common.debug import debug
from common.extraction import extractMain, allZipFilesIn, createStudentWorkspace, extractStudent
from common.util import Workspace, StudentWorkspace


def runA2():
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
    testCases = (rootDir / "test_cases").resolve()

    workspace = Workspace(rootDir, scratchDir, markingDir, testCases, mainZip)
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
            classNames = copyA2TestFiles(workspace.testCasesDir, studentWorkspace)
            compileRunTarget(studentWorkspace, runTarget, classNames)
            runA2Tests(studentWorkspace, runTarget, override=True)
            validateA2(workspace.testCasesDir, studentWorkspace, override=True)

        print("\n")
