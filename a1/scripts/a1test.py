from typing import List, Callable

from test_util import runJava, appendTo


def testCase(testFor: str, testNum: int, args: str, runJava: Callable[[str], str], append: Callable[[int, str], None]):
    javaOut = runJava(args)
    append(testNum, javaOut)


def runTest(markingDir: str, scratchDir: str, studentDir: str):
    def singleJavaRun(args: str):
        cpDir = "%s/%s/out" % (scratchDir, studentDir)
        className = "LuhnA1"
        return runJava(cpDir, className, args)

    runOutputDir = "%s/%s/%s" % (markingDir, studentDir, "output")

    def appendOutput(testNum: int, text: str):
        appendTo("%s/%d.in" % (runOutputDir, testNum), text)

    testCase("single non number", 1, "aaa", singleJavaRun, appendOutput)
    testCase("single number less than 2 characters", 2, "2", singleJavaRun, appendOutput)
    testCase("2 digit number - invalid", 2, "41", singleJavaRun, appendOutput)
    testCase("2 digit number - valid", 2, "42", singleJavaRun, appendOutput)
    testCase("long number - invalid", 2, "4298999999999999999999999999999999", singleJavaRun, appendOutput)


def testStage(markingDir: str, scratchDir: str, studentDirs: List[str]):
    for studentDir in studentDirs:
        runTest(markingDir, scratchDir, studentDir)
