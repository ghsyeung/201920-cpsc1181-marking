import subprocess
from pathlib import Path


def runJava(cpDir: Path, className: str, args: str) -> str:
    command = ["java", "-cp", str(cpDir), className]
    if len(args):
        command.append(args)
    run = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE)
    return run.stdout


def appendTo(file: Path, text: str):
    if file.exists():
        mode = 'a'  # append if already exists
    else:
        mode = 'w'  # make a new file if not
    with file.open(mode) as myfile:
        myfile.write(str(text))
        myfile.close()
