import sys
from pathlib import Path
import difflib

from debug import debug
from test_util import appendTo
from util import StudentWorkspace


def validateA1(testCasesDir: Path, ws: StudentWorkspace):
    runOutputDir = ws.markingDir / "output"
    validateOutput = ws.markingDir / "validation.out"

    def append(text:str):
        appendTo(validateOutput, text)

    for i in sorted(testCasesDir.glob("*.truth")):
        testNum, _ = i.name.split(".")
        outputFile = runOutputDir / ("%s.out" % testNum)

        with i.open("r") as f,  outputFile.open("r") as g:
            flines = f.readlines()
            glines = g.readlines()
            diff = difflib.unified_diff(flines, glines, i.name, outputFile.name, lineterm="\n")
            sys.stdout.writelines(diff)
            append("Comparing to %s\n\n" % i)
            append("".join(list(diff)))
            append("\n\n")


