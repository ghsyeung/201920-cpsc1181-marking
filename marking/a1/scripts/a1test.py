import shutil
from typing import Callable

from common.test_util import runJava, appendTo
from common.util import StudentWorkspace, RunTarget


def runA1Tests(ws: StudentWorkspace, target: RunTarget, override=False):
    runOutputDir = (ws.markingDir / "output").resolve()
    if not override and runOutputDir.exists():
        raise Exception("Safety Check: %s already exists and override flag is False" % str(runOutputDir))

    if runOutputDir.exists():
        shutil.rmtree(runOutputDir)
    runOutputDir.mkdir(exist_ok=True)

    def singleJavaRun(args: str):
        cpDir = target.outDir
        className = target.targetFile.stem
        return runJava(cpDir, className, args)

    def appendOutput(testNum: int, text: str):
        fileName = "%d.out" % testNum;
        appendTo(runOutputDir / fileName, text)

    testCase("single non number", 1, "aaa", singleJavaRun, appendOutput)
    testCase("single number less than 2 characters", 2, "2", singleJavaRun, appendOutput)
    testCase("2 digit number - invalid", 3, "41", singleJavaRun, appendOutput)
    testCase("2 digit number - valid", 4, "42", singleJavaRun, appendOutput)
    testCase("long number - invalid", 5, "4485513999294613", singleJavaRun, appendOutput)

    testCase("long number - valid", 6, "4485513999294612", singleJavaRun, appendOutput)
    testCase("empty arguments", 7, "", singleJavaRun, appendOutput)
    testCase("Zero is not positive", 8, "0000", singleJavaRun, appendOutput)
    testCase("Valid number greater than lng.MAX_VALUE", 9, "5305901611460339130131428629990709253530", singleJavaRun,
             appendOutput)
    testCase("Invalid number greater than Long.MAX_VALUE", 10, "5305901611460339130131428629990709253531",
             singleJavaRun, appendOutput)


def testCase(testFor: str, testNum: int, args: str, runJava: Callable[[str], str], append: Callable[[int, str], None]):
    javaOut = runJava(args)
    append(testNum, javaOut)

