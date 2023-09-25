import runpy

import jinja2
from .helpers.const import default_injection_file
from .helpers.io import Colours


class JinjaComposeInject:
    pass


def run_build(args):
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
