import shutil
from typing import Callable

from common.test_util import runJava, appendTo
from common.util import StudentWorkspace, RunTarget


def runA2Tests(ws: StudentWorkspace, target: RunTarget, override=False):
    runOutputDir = (ws.markingDir / "output").resolve()
    if not override and runOutputDir.exists():
        raise Exception("Safety Check: %s already exists and override flag is False" % str(runOutputDir))

    if runOutputDir.exists():
        shutil.rmtree(runOutputDir)
    runOutputDir.mkdir(exist_ok=True)

    def singleJavaRun(className: str, args: str):
        cpDir = target.outDir
        # Not using target.targetFile for A2
        return runJava(cpDir, className, args)

    def appendOutput(testFor: str, text: str):
        fileName = "%s.out" % testFor;
        appendTo(runOutputDir / fileName, text)

    testCase("ATest1", singleJavaRun, appendOutput)
    testCase("ATest1_1", singleJavaRun, appendOutput)
    testCase("ATest2", singleJavaRun, appendOutput)
    testCase("ATest2_1", singleJavaRun, appendOutput)
    testCase("ATest2_2", singleJavaRun, appendOutput)

def testCase(testFor: str, runJava: Callable[[str, str], str], append: Callable[[int, str], None]):
    javaOut = runJava(testFor, "")
    append(testFor, javaOut)
