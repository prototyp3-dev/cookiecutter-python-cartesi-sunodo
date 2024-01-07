# Cookiecutter Cartesi DApp with Sunodo

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template for a Cartesi DApp written in Python and using the [python-cartesi](https://github.com/prototyp3-dev/python-cartesi) framework and [Sunodo](https://sunodo.io/).

## Features

This template initialized a minimal DApp with the following features:

- Sample implementation of the "echo" example
- Using [Sunodo](https://sunodo.io/) as the dapp build system
- Requirements managed by [pip-tools](https://pip-tools.readthedocs.io/en/latest/)
- Test case for the sample dapp using pytest

## Usage

To use this template, it is assumed you already have the following dependencies:

- Cookiecutter installed in your python environment
- NodeJS version 18 available
- Sunodo CLI installed (`npm install -g @sunodo/cli`)

To create your project, you can execute:

```shell
cookiecutter gh:prototyp3-dev/cookiecutter-python-cartesi-sunodo
```

You will be asked the following questions:

- **Project Name**: The full name of the project. This will be used in the README title, and also to seed the next questions
- **Name for the root directory of the repository**: This will be the name of the directory being created to hold the new project.
- **Name for the main package in the repository**: This is the name of the Python package within the repository that will contain your code.
