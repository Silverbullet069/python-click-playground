# python-click-playground

[![PyPI](https://img.shields.io/pypi/v/python-click-playground.svg)](https://pypi.org/project/python-click-playground/)
[![Changelog](https://img.shields.io/github/v/release/Silverbullet069/python-click-playground?include_prereleases&label=changelog)](https://github.com/Silverbullet069/python-click-playground/releases)
[![Tests](https://github.com/Silverbullet069/python-click-playground/actions/workflows/test.yml/badge.svg)](https://github.com/Silverbullet069/python-click-playground/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Silverbullet069/python-click-playground/blob/master/LICENSE)

This is a playground to learn about creating Python application using Click library.

## Installation

Install this tool using `pip`:
```bash
pip install python-click-playground
```
## Usage

For help, run:
```bash
python-click-playground --help
```
You can also use:
```bash
python -m python_click_playground --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd python-click-playground
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
