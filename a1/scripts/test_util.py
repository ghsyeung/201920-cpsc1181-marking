import os
import subprocess


def runJava(cpDir: str, className: str, args: str):
    command = ["java", "-cp", cpDir, className, args]
    run = subprocess.run(command, stdout=subprocess.PIPE)
    return run.stdout


def appendTo(file: str, text: str):
    if os.path.exists(file):
        mode = 'a'  # append if already exists
    else:
        mode = 'w'  # make a new file if not
    with open(file, mode) as myfile:
        myfile.write(text)
