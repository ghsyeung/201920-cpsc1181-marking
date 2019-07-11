import argparse
import sys
from pathlib import Path

from common.debug import debug
from common.extraction import extractMain, allZipFilesIn, createStudentWorkspace, extractStudent
from common.util import Workspace, StudentWorkspace, RunConfig
from .a3compilation import getRunTarget, compileRunTarget, copyExtraSource
from .a3test import runA3Tests
from .a3validate import validateA3


def runA3():
    argparser = argparse.ArgumentParser(description="Assignment 3")
    argparser.add_argument('--no-extract', '-e', dest="no_extract", action='store_true', help='skip extraction of zip file')
    argparser.add_argument('--no-compile', '-c', dest="no_compile", action='store_true', help='skip compilation stage')
    argparser.add_argument('--only-extract', '-E', dest="only_extract", action='store_true', help='only extract D2L zip file')
    argparser.add_argument('mainZip', type=str, help='D2L zip file')
    argparser.add_argument('rootDir', type=str, help='output folder')
    argparser.add_argument('student', type=str, nargs='?', help='student name')

    args = argparser.parse_args(sys.argv[1:])

    mainZip = Path(args.mainZip)
    rootDir = Path(args.rootDir)
    if (not rootDir.exists() or not mainZip.exists()):
        print("Invalid rootDir or main zip file")
        exit(-1)

    scratchDir = (rootDir / "scratch").resolve()
    scratchDir.mkdir(exist_ok=True)
    markingDir = (rootDir / "marking").resolve()
    markingDir.mkdir(exist_ok=True)
    testCasesDir: Path = (rootDir / "test_cases").resolve()
    extraSourceDir: Path = (rootDir / "java_files").resolve()

    runConfig = RunConfig(args.no_extract, args.no_compile, args.only_extract, args.student)
    workspace = Workspace(rootDir, scratchDir, markingDir, mainZip, testCasesDir, extraSourceDir)
    debug("Running with \n  config=%s \n  in %s" % (str(runConfig), str(workspace)))

    skipExtract = runConfig.noExtract or runConfig.student

    extractMain(workspace, clean=not skipExtract)

    for submission in allZipFilesIn(workspace.scratchDir)[:]:
        studentWorkspace: StudentWorkspace = createStudentWorkspace(workspace, submission)

        # run for everyone or only the student specified
        if not runConfig.student or runConfig.student == studentWorkspace.studentDirName:
            print("Running %s" % studentWorkspace.studentDirName)

            if not skipExtract:
                extractStudent(studentWorkspace)

            if not runConfig.onlyExtract:
                runTarget = getRunTarget(studentWorkspace)
                if runTarget:
                    extraClasses = copyExtraSource(workspace.extraSourceDir, runTarget)
                    classNames = ["RunSystem"] + extraClasses
                    if not runConfig.noCompile:
                        compileRunTarget(studentWorkspace, runTarget, classNames)
                    runA3Tests(workspace.testCasesDir, studentWorkspace, runTarget, override=True)
                    validateA3(workspace.testCasesDir, studentWorkspace, override=True)

            print("\n")
