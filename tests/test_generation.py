import subprocess
import yaml


def test_file_generation():
    subprocess.run(["./venv/bin/jinja_compose", "-i", "tests/test_generation/compose.jyml", "-o",
                    "tests/test_generation/compose.yaml", "-p", "tests/test_generation/compose.py", "-d",
                    "echo"])

    with open("tests/test_generation/compose.yaml", "r") as fh:
        with open("tests/test_generation/expected.yaml", "r") as fh2:
            assert yaml.safe_load(fh) == yaml.safe_load(fh2)
