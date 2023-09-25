from setuptools import setup, find_packages
from pathlib import Path
p_directory = Path(__file__).parent.parent
long_description = (p_directory / "README.md").read_text()

VERSION = '0.0.3'
DESCRIPTION = 'Docker compose to the next level with Jinja2 templating'
LONG_DESCRIPTION = 'Docker compose to the next level with Jinja2 templating'

# Setting up
setup(
    name="jinja-compose-wrapper",
    version=VERSION,
    author="Sidney Trzepacz",
    author_email="<lafakeslimshady@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=['jinja2'],
    keywords=['python', 'docker', 'compose', 'jinja2', 'template', 'templating'],
    url="https://github.com/Sid220/jinja-compose",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        "console_scripts": ['jinja_compose=jinja_compose_wrapper:main']
    },
    packages=find_packages(),
)
