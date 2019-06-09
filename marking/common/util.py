from pathlib import Path
from typing import NamedTuple


class Workspace(NamedTuple):
    rootDir: Path
    scratchDir: Path
    markingDir: Path
    testCasesDir: Path
    mainZip: Path


class StudentWorkspace(NamedTuple):
    markingDir: Path
    scratchDir: Path
    studentZip: Path
    studentDirName: str

class RunTarget(NamedTuple):
    javaDir: Path
    outDir: Path
    targetFile: Path

def isDir(x: Path):
    return x.is_dir()


def isFile(x: Path):
    return x.is_file()
