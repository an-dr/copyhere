import os
import sys

python = sys.executable
install_cmd = "-m pip install -e"
script_dir = os.path.dirname(os.path.realpath(__file__))

cmd = " ".join([python, install_cmd, script_dir])
os.system(cmd)
