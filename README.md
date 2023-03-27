
# Starbun

A package for running and evaluating simulation experiments

<img src="https://github.com/Kladdy/starbun/blob/master/logistics/logo.png?raw=true" alt= “Starbun” width="256" height="256">

## Terminology

- **Experiment** - An experiment is the highest level in the hierarchy, and is the overarching term for a project. It is a collection of trials, and an example might be an experiment to optimize the hyperparameters of a neural network.
- **Trial** - A trial is the next level down in the hierarchy. It is a collection of runs, and an example might be a trial to optimize a specific set of hyperparameters of a neural network.
- **Run** - A run is the lowest level in the hierarchy. It is a single simulation run, and an example might be a run of a neural network with a specific set of hyperparameters.

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