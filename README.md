# Jinja Compose
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/sid220/jinja-compose/pytest.yml?logo=github&label=Tests&link=https%3A%2F%2Fgithub.com%2FSid220%2Fjinja-compose%2Factions%2Fworkflows%2Fpytest.yml) ![Codecov](https://img.shields.io/codecov/c/github/sid220/jinja-compose?logo=codecov)
 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jinja-compose-wrapper) ![PyPI - Status](https://img.shields.io/pypi/status/jinja-compose-wrapper?logo=pypi&label=PyPI%20Status) ![PyPI - License](https://img.shields.io/pypi/l/jinja-compose-wrapper) ![PyPI - Version](https://img.shields.io/pypi/v/jinja-compose-wrapper?label=PyPI%20Version&logo=pypi) ![PyPI - Format](https://img.shields.io/pypi/format/jinja-compose-wrapper?logo=pypi&label=PyPI%20Format)

`jinja-compose` is a tool for running docker-compose commands with Jinja2 templating.

## Installation
```bash
pip install jinja-compose-wrapper
```
Then ensure your Python bin directory is in your PATH.

## Usage
Jinja Compose operates using the same syntax as docker-compose, but with the addition of a template and optional injection file.
The typical project setup looks like this:
```
/project_dir
├── compose.jyml
├── compose.py
└── compose.yaml  [generated by jinja-compose]
```
Where `compose.jyml` is a Jinja2 template file, `compose.py` is an optional Python file containing variables to be injected into the template, and `compose.yaml` is the generated docker-compose file.

### Example
In `compose.jyml` we define a service called `server`, which only runs in production when the `is_production` variable is defined and only forwards ports on a certain host.
```yaml
services:
  server:
    build:
      context: .
    image: sid220/apriltag_localisation:latest
    environment:
      - DAPRILTAG_PRODUCTION={{ MyJinjaComposeInjection.is_production }}
      - OPENCV_VIDEOIO_DEBUG=1
    {% if MyJinjaComposeInjection.my_static_method() == 'special_host' %}
    ports:
        - "5000:5000"
    {% endif %}
```
To define the `is_production` variable and `my_static_method` method, we create a `compose.py` file with a class that inherits from `JinjaComposeInject`.
```python
from jinja_compose_wrapper.libjinja_compose import JinjaComposeInject
import socket

class MyJinjaComposeInjection(JinjaComposeInject):
    is_production = 1
    
    @staticmethod
    def my_static_method():
        return socket.gethostname()
```
Once done we can now bring this service up:
```bash
jinja_compose up
```
Or just build the yaml file:
```bash
jinja_compose -d echo
```
## Full Usage Documentation
```
jinja_compose [-h] [--template TEMPLATE] [--output OUTPUT] [--injection-file INJECTION_FILE] [--dockercmd [DOCKERCMD]] [--as-root] [action ...]

positional arguments:
  action

options:
  -h, --help            show this help message and exit
  --template TEMPLATE, -i TEMPLATE, -t TEMPLATE
  --output OUTPUT, -o OUTPUT
  --injection-file INJECTION_FILE, -p INJECTION_FILE
  --dockercmd [DOCKERCMD], -d [DOCKERCMD]
  --as-root, -r
```
