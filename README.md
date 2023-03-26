
# Starbun

A package for running and evaluating simulation experiments

<img src="https://github.com/Kladdy/starbun/blob/master/logistics/logo.png?raw=true" alt= “Starbun” width="256" height="256">




## Installation

TBD

## Usage

TBD

## For test-publishing

```bash
python3 -m pip install --upgrade build
python3 -m build

python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

with \_\_token\_\_ as the username for twine, and the token as the password.

To then install the package, run

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps starbun
```

## For publishing

```bash
python3 -m pip install --upgrade build
python3 -m build

python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
```

with \_\_token\_\_ as the username for twine, and the token as the password.

To then install the package, run

```bash
python3 -m pip install starbun
```

## Guides used

- [Packaging Python Projects](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/)