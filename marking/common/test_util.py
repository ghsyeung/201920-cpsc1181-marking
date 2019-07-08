import select
import subprocess
import time
from pathlib import Path

from common.debug import debug


def runJava(cpDir: Path, className: str, args: str) -> str:
    command = ["java", "-cp", str(cpDir), className]
    if len(args):
        command.append(args)
    run = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE)
    return run.stdout

def runJavaWithInput(cpDir: Path, className: str, args: [str], input: str, sleep=1) -> str:
    def notEmptyAndNotComment(s:str) -> bool:
        stripped = s.strip()
        return stripped != "" and not stripped.startswith("#")

    command = ["java", "-cp", str(cpDir), className]
    if len(args):
        command.extend(args)

    output = ""
    lines = filter(notEmptyAndNotComment, input.split("\n"))
    try:
        echo = subprocess.Popen(["cat"], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        process = subprocess.Popen(command, encoding='utf-8', stdout=echo.stdin, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            time.sleep(sleep)
            for line in lines:
                process.stdin.write(line + "\n")
                process.stdin.flush()

                echo.stdin.write(line + "\n")
                echo.stdin.flush()

                time.sleep(sleep)

            (stdout, _) = echo.communicate()
            output += stdout or ""
        except:  # Including KeyboardInterrupt, communicate handled that.
            (stdout, _) = echo.communicate()
            output += stdout or ""

            echo.kill()
            process.kill()
        retcode = process.poll()
        debug("Completed %s with retcode %d " % (" ".join(command), retcode))
    finally:
        try:
            process.__exit__()
        except:
            pass
    return output

def appendTo(file: Path, text: str):
    if file.exists():
        mode = 'a'  # append if already exists
    else:
        mode = 'w'  # make a new file if not
    with file.open(mode) as myfile:
        myfile.write(str(text))
        myfile.close()
