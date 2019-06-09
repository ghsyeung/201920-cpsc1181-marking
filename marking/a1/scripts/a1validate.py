import difflib
import subprocess
from pathlib import Path
from typing import Callable

from common.test_util import appendTo
from common.util import StudentWorkspace


def diffWithDifflib(i: Path, o: Path, validateOutput: Path):
    def append(text: str):
        appendTo(validateOutput, text)

    with i.open("r") as f, o.open("r") as g:
        flines = f.readlines()
        glines = g.readlines()
        diff = difflib.unified_diff(flines, glines, i.name, o.name, n=4, lineterm="\n")
        append("Comparing to %s\n" % i)
        l = list(diff)
        if not l:
            append("PASS!\n\n")
        else:
            append("MISMATCH!\n")
            append("".join(l))
            append("\n")


def diffWithDiff(i: Path, o: Path, append: Callable[[str], None]):
    run = subprocess.run(["diff", "-iw", i, o], encoding="utf-8", stdout=subprocess.PIPE)
    append("Comparing to %s\n" % i)
    if (run.returncode == 0):
        append("PASS!\n\n")
    else:
        append("MISMATCH!\n")
        append(str(run.stdout))
        append("\n\n")


def validateA1(testCasesDir: Path, ws: StudentWorkspace, override=False):
    runOutputDir = ws.markingDir / "output"
    validateOutput = ws.markingDir / "validation.out"

    # remove the file if override is True
    if override and validateOutput.exists():
        validateOutput.unlink()

    def append(text: str):
        appendTo(validateOutput, text)

    allTruthFiles = sorted(testCasesDir.glob("*.truth"), key=lambda x: int(x.name.split(".")[0]))
    for i in allTruthFiles:
        testNum, _ = i.name.split(".")
        outputFile = runOutputDir / ("%s.out" % testNum)
        diffWithDiff(i, outputFile, append)