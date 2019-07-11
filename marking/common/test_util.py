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

def runJavaWithInput(cpDir: Path, className: str, args: [str], input: str, sleep=0.5) -> str:
    def notEmpty(s:str) -> bool:
        stripped = s.strip()
        return stripped != ""

    def notComment(s:str) -> bool:
        stripped = s.strip()
        return not stripped.startswith("#")

    command = ["java", "-cp", str(cpDir), className]
    if len(args):
        command.extend(args)

    output = ""
    lines = filter(notEmpty, input.split("\n"))
    try:
        # A hack to get all process.stdin, process.stdout and process.stderr in the same place
        echo = subprocess.Popen(["cat"], encoding='utf-8', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        process = subprocess.Popen(command, encoding='utf-8', stdout=echo.stdin, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            # enabled command delay
            cachedCommand = None
            time.sleep(sleep)
            for line in lines:
                if notComment(line):
                    # if we have a delayed command, we run it first
                    if cachedCommand is not None:
                        process.stdin.write(cachedCommand + "\n")
                        process.stdin.flush()
                        time.sleep(sleep)

                    cachedCommand = line
                    echo.stdin.write(line + "\n")
                    echo.stdin.flush()
                else:
                    echo.stdin.write("\n" + line + "\n\n")
                    echo.stdin.flush()

            # final delayed command
            if cachedCommand is not None:
                process.stdin.write(cachedCommand + "\n")
                process.stdin.flush()
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
