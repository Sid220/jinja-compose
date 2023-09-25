import argparse
import jinja2
import subprocess
import shlex
import runpy

from .helpers.io import Colours
from .libjinja_compose import JinjaComposeInject

default_injection_file = "compose.py"
parser = argparse.ArgumentParser()
parser.add_argument('--template', '-i', '-t', default='compose.jyml', dest='template')
parser.add_argument('--output', '-o', default='compose.yaml', dest='output')
parser.add_argument("--injection-file", "-p", default=default_injection_file)
parser.add_argument('--dockercmd', '-d', nargs='?', default='/usr/local/bin/docker compose', dest='dockercmd')
parser.add_argument("--as-root", "-r", action="store_true")
parser.add_argument("action", nargs="*", default=["up -d"])


def main():
    args = parser.parse_args()

    injects = {}
    try:
        raw_injects = runpy.run_path(args.injection_file)
        for inject in raw_injects:
            try:
                if raw_injects[inject].__base__ == JinjaComposeInject:
                    injects[raw_injects[inject].__name__] = (raw_injects[inject])
            except AttributeError:
                continue
    except FileNotFoundError:
        if args.injection_file == default_injection_file:
            print(Colours.OKBLUE + "[i]" + Colours.ENDC + " No such injection file: " + args.injection_file)
        else:
            raise FileNotFoundError("No such injection file: " + args.injection_file)

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = args.template
    try:
        template = templateEnv.get_template(TEMPLATE_FILE)
    except jinja2.exceptions.TemplateNotFound:
        raise FileNotFoundError("Cannot open template: " + TEMPLATE_FILE)

    outputText = template.render(injects)
    with open(args.output, "w") as fh:
        fh.write(outputText)

    command = ("sudo " if args.as_root else "") + f"{args.dockercmd} {' '.join(args.action)}"
    print(Colours.OKGREEN + "[+] " + Colours.ENDC + (
        "sudo " if args.as_root else "") + f"{args.dockercmd} {' '.join(args.action)}\n")
    subprocess.run(shlex.split(command))