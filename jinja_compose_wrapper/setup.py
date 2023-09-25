from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Docker compose to the next level with Jinja2 templating'
LONG_DESCRIPTION = 'Docker compose to the next level with Jinja2 templating'

# Setting up
setup(
    name="jinja-compose-wrapper",
    version=VERSION,
    author="Sidney Trzepacz",
    author_email="<lafakeslimshady@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=['jinja2'],
    keywords=['python', 'docker', 'compose', 'jinja2', 'template', 'templating'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ['jinja_compose=jinja_compose_wrapper:main']
    },
    packages=find_packages(),
)
