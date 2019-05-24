import shutil
import zipfile
from pathlib import Path
from typing import List

import util
from util import Workspace, StudentWorkspace


def allZipFilesIn(dir: Path) -> List[Path]:
    return list(filter(util.isFile, dir.glob("*.zip")))


def submissionZipToName(file: Path) -> str:
    filename, extension = file.name.split(".")
    s, name, date, f = filename.split(" - ", maxsplit=3)
    studentDir = name.replace(" ", "_")
    return studentDir


def createStudentWorkspace(workspace: Workspace, submission: Path):
    studentDirName = submissionZipToName(submission)
    studentScratchDir = workspace.scratchDir / studentDirName
    studentMarkingDir = workspace.markingDir / studentDirName
    return StudentWorkspace(studentMarkingDir, studentScratchDir, submission)


def extractMain(ws: Workspace, clean=False):
    if clean and ws.scratchDir.exists():
        shutil.rmtree(ws.scratchDir)
        ws.scratchDir.mkdir()

    zipfile.ZipFile(ws.mainZip, 'r').extractall(path=ws.scratchDir)


def extractStudent(ws: StudentWorkspace, clean=False):
    if clean and ws.scratchDir.exists():
        shutil.rmtree(ws.scratchDir)
        ws.scratchDir.mkdir()

    zipfile.ZipFile(ws.studentZip, 'r').extractall(path=ws.scratchDir)

    for i in filter(util.isDir, ws.scratchDir.glob("__MACOSX")):
        shutil.rmtree(i)
