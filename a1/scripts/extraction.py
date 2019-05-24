import glob
import os
from typing import List

from debug import debug


def extractAllStudentZip(scratchDir):
    zipfiles = "/*.zip"
    studentDirs = []

    # extract each student's zip
    for f in glob.glob("%s/%s" % (scratchDir, zipfiles)):
        filename, extension = f.split(".")
        s, name, date, f = filename.split(" - ", maxsplit=3)
        debug("Extracting: %s, %s, %s" % (name, date, f))

        studentDir = name.replace(" ", "_")

        studentDirs.append(studentDir)

        extractTo = "%s/%s" % (scratchDir, studentDir)
        debug(extractTo)
        os.system("rm -r \"%s\"" % extractTo)
        os.system("unzip -d \"%s\" \"%s.%s\"" % (extractTo, filename, extension))
        os.system("rm -r \"%s\"/__MACOSX" % extractTo)
    return studentDirs


def extractStage(allzip, rootDir, markingDir, scratchDir):
    # extract main assignment zip
    if not os.path.exists(scratchDir):
        os.system("unzip -d \"%s\" \"%s\"" % (scratchDir, allzip))

    studentDirs: List[str] = extractAllStudentZip(scratchDir)

    for directory in [markingDir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    return studentDirs
