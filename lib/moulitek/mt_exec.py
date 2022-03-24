import subprocess

def call_system(command, timeout = 60):
    return subprocess.call("timeout %ds %s 1> /dev/null 2> /dev/null" % (timeout, command), shell=True)

