import os
from typing import List

from compilation_util import findDirContainingJava, javaCompile
from debug import debug


def compileStage(markingDir: str, scratchDir: str, studentDirs: List[str]):
    for dir in studentDirs:
        markingDirOfStudent = "%s/%s" % (markingDir, dir)
        os.system("mkdir %s" % markingDirOfStudent)

        javaDir = findDirContainingJava(scratchDir, dir, target="Luhn*.java")
        outDir = "%s/%s/%s" % (scratchDir, dir, "out")
        if javaDir != None:
            cpDir = str(javaDir.resolve())
            javaCompile(markingDirOfStudent, outDir, cpDir, "*.java")
