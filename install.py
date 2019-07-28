# The Script : https://gist.github.com/an-dr/9f3256f4ccd97bc6e04751b542364bff

from os.path import realpath, dirname, join
from os import system as x


def x(cmd):
    # imports
    from psutil import MACOS, WINDOWS, LINUX
    from subprocess import Popen as shell
    from sys import stdout
    # shell cfg
    if WINDOWS:
        SHELL, NEXT_CMD = "powershell", ";"
    elif MACOS or LINUX:
        SHELL, NEXT_CMD = "sh", ";"
    # run
    shell([SHELL, NEXT_CMD.join(cmd)], stdout=stdout).communicate()


THIS = dirname(realpath(__file__))

import sys
from info import info

python = sys.executable
install_cmd = "setup.py install"
uninstall_cmd = "-m pip uninstall -y"

cmd_uninstall = " ".join([python, uninstall_cmd, info['name']])
cmd_install = " ".join([python, install_cmd])

X = [
    cmd_uninstall,
    cmd_install,
]
x(X)
