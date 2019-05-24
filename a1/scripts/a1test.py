import shutil
from typing import Callable

from test_util import runJava, appendTo
from util import StudentWorkspace, RunTarget


def runA1Tests(ws: StudentWorkspace, target: RunTarget, override=False):
    runOutputDir = (ws.markingDir / "output").resolve()
    if not override and runOutputDir.exists():
        raise Exception("Safety Check: %s already exists and override flag is False" % str(runOutputDir))

    if runOutputDir.exists():
        shutil.rmtree(runOutputDir)
    runOutputDir.mkdir(exist_ok=True)

    def singleJavaRun(args: str):
        cpDir = target.outDir
        className, extension = target.targetFile.name.split(".")
        return runJava(cpDir, className, args)

    def appendOutput(testNum: int, text: str):
        fileName = "%d.out" % testNum;
        appendTo(runOutputDir / fileName, text)

    testCase("single non number", 1, "aaa", singleJavaRun, appendOutput)
    testCase("single number less than 2 characters", 2, "2", singleJavaRun, appendOutput)
    testCase("2 digit number - invalid", 3, "41", singleJavaRun, appendOutput)
    testCase("2 digit number - valid", 4, "42", singleJavaRun, appendOutput)
    testCase("long number - invalid", 5, "4298999999999999999999999999999999", singleJavaRun, appendOutput)


def testCase(testFor: str, testNum: int, args: str, runJava: Callable[[str], str], append: Callable[[int, str], None]):
    javaOut = runJava(args)
    append(testNum, javaOut)

