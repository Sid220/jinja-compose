import argparse

import yaml

from jinja_compose_wrapper import run_build


def test_build():
    run_build(argparse.Namespace(injection_file="tests/test_generation/compose.py",
                                 output="tests/test_generation/compose.yaml",
                                 template="tests/test_generation/compose.jyml"))
    with open("tests/test_generation/compose.yaml", "r") as fh:
        with open("tests/test_generation/expected.yaml", "r") as fh2:
            assert yaml.safe_load(fh) == yaml.safe_load(fh2)
