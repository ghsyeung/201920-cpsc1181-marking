import shutil
from pathlib import Path
from typing import Callable

from common.compilation_util import firstFileMatching
from common.test_util import runJavaWithInput, appendTo
from common.util import StudentWorkspace, RunTarget

def runA3Tests(testCasesDir: Path, ws: StudentWorkspace, target: RunTarget, override=False):
    runOutputDir = (ws.markingDir / "output").resolve()
    if not override and runOutputDir.exists():
        raise Exception("Safety Check: %s already exists and override flag is False" % str(runOutputDir))

    if runOutputDir.exists():
        shutil.rmtree(runOutputDir)
    runOutputDir.mkdir(exist_ok=True)

    def singleJavaRun(className: str, args: str, input: str):
        cpDir = target.outDir
        # Not using target.targetFile for A3
        return runJavaWithInput(cpDir, className, args, input)

    def appendOutput(testFor: str, text: str):
        fileName = "%s.out" % testFor;
        appendTo(runOutputDir / fileName, text)

    def readTestFile(testNum: int):
        filePath = firstFileMatching(testCasesDir, "%d.in" % testNum)
        with open(filePath, 'r') as content_file:
            content = content_file.read()
            return content

    for testNum in range(1, 7):
        testCase(testNum, readTestFile, singleJavaRun, appendOutput)

def testCase(testNum: int, readTestInput: Callable[[int], str], runJava: Callable[[str, str], str], append: Callable[[int, str], None]):
    input = readTestInput(testNum)
    javaOut = runJava("RunSystem", ["100", "0"], input)
    append(testNum, javaOut)
