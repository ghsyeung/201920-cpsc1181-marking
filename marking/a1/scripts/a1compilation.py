from pathlib import Path
from typing import Optional

from common.compilation_util import findDirContainingJava, javaCompile, firstFileMatching
from common.util import StudentWorkspace, RunTarget


def compileStudent(ws: StudentWorkspace):
    findDirContainingJava(ws.scratchDir, )


def getRunTarget(ws: StudentWorkspace) -> Optional[RunTarget]:
    file = firstFileMatching(ws.scratchDir, target="Luhn*.java")
    if file:
        file = file.resolve()
        javaDir: Path = file.parent.resolve()
        outDir: Path = javaDir.parent.resolve() / "out"
        outDir.mkdir(exist_ok=True)
        return RunTarget(javaDir, outDir, file)


def compileRunTarget(ws: StudentWorkspace, target: RunTarget):
    javaCompile(ws.markingDir, target.outDir, target.javaDir, "*.java")
