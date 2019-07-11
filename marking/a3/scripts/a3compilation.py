import shutil;
from pathlib import Path
from typing import Optional, List

from common.compilation_util import findDirContainingJava, javaCompile, firstFileMatching
from common.util import StudentWorkspace, RunTarget


def compileStudent(ws: StudentWorkspace):
    findDirContainingJava(ws.scratchDir, )


def findSrcFolder(dir: Path) -> Optional[Path]:
    file = firstFileMatching(dir, target="Run*.java")
    print(file)
    if file:
        file = file.resolve()
        return file.parent.resolve()


def getRunTarget(ws: StudentWorkspace) -> Optional[RunTarget]:
    javaDir = findSrcFolder(ws.scratchDir)
    if javaDir:
        outDir: Path = javaDir.parent.resolve() / "out"
        outDir.mkdir(exist_ok=True)
        return RunTarget(javaDir, outDir, "")


def compileRunTarget(ws: StudentWorkspace, target: RunTarget, classNames: List[str]):
    for i in classNames:
        javaCompile(ws.markingDir, target.outDir, target.javaDir, "%s.java" % i)


def copyExtraSource(extraSourceDir: Path, rt: RunTarget):
    print(extraSourceDir)
    extraJavaFiles = list(extraSourceDir.resolve().glob("*.java"))
    print(extraJavaFiles)
    for i in extraJavaFiles:
        shutil.copy(i, rt.javaDir)
    return [i.stem for i in extraJavaFiles]
