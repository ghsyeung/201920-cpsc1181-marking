import os
from pathlib import Path

from debug import debug


def findDirContainingJava(scratchDir: str, dir: str, target="*.java") -> Path:
    files = list(Path(scratchDir, dir).glob("**/%s" % target))
    first = files[0] if len(files) > 0 else None
    return first.parent if first else None

def javaCompile(markingDir:str, outDir:str, cpDir: str, file: str):
    command = "javac -d \"%s\" -cp \"%s\" \"%s\"/%s" % (outDir, cpDir, cpDir, file)
    debug(command)
    os.system("%s >> \"%s\"/compile.out 2>&1" % (command, markingDir))
