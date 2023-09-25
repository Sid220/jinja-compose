import argparse
import jinja2
import subprocess
import shlex
import runpy

from .helpers.io import Colours
from .helpers.const import default_injection_file
from .libjinja_compose import JinjaComposeInject, run_build

parser = argparse.ArgumentParser()
parser.add_argument('--template', '-i', '-t', default='compose.jyml', dest='template')
parser.add_argument('--output', '-o', default='compose.yaml', dest='output')
parser.add_argument("--injection-file", "-p", default=default_injection_file)
parser.add_argument('--dockercmd', '-d', nargs='?', default='/usr/local/bin/docker compose', dest='dockercmd')
parser.add_argument("--as-root", "-r", action="store_true")
parser.add_argument("action", nargs="*", default=["up -d"])


def main():
    args = parser.parse_args()

    run_build(args)

    command = ("sudo " if args.as_root else "") + f"{args.dockercmd} {' '.join(args.action)}"
    print(Colours.OKGREEN + "[+] " + Colours.ENDC + (
        "sudo " if args.as_root else "") + f"{args.dockercmd} {' '.join(args.action)}\n")
    subprocess.run(shlex.split(command))
