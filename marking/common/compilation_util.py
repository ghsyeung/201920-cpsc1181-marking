import os
from pathlib import Path

from common import util
from common.debug import debug


def firstFileMatching(studentScratch: Path, target="*.java") -> Path:
    files = list(filter(util.isFile, studentScratch.glob("**/%s" % target)))
    first = files[0] if len(files) > 0 else None
    return first


def findDirContainingJava(studentScratch: Path, target="*.java") -> Path:
    first = firstFileMatching(studentScratch, target)
    return first.parent if first else None


def javaCompile(markingDir: Path, outDir: Path, cpDir: Path, file: str):
    command = "javac -d \"%s\" -cp \"%s\" \"%s\"/%s" % (str(outDir), str(cpDir), str(cpDir), file)
    debug(command)
    os.system("%s >> \"%s\"/compile.out 2>&1" % (command, str(markingDir)))
