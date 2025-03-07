# Contributing

## Development environment

### Pip

Create a development environment with `Python>=3.9`.

Please do not create a venv directly in the project directory.
else pytest will find too many tests.

You can then install the development and test dependencies with:

```bash
python -m pip install --group dev --editable .venv
source .venv/bin/activate
```

[!WARNING]
This example only works with pip in version 25.1 or newer.
Version 25.1 has a planned release date of 2025-04-30

### UV

Tox requires a plug in to work with uv, to install all dependencies the command
for syncing the environment needs to be thus:

```bash
uv sync --group=uv
```

Future code examples are valid for `pip` but work with uv too, if you prefix
the commands with uv run.

## Tests

To run the test suite, we use `pytest`:

```bash
pytest
```

## Pre-commit

We use precommit hooks to ensure code style and format.

Install `precommit` from pip

```bash
pip install pre-commit
pre-commit install
```

Now after each commit, the style hooks will run and auto format the code.

You can also manually run the pre-commit hooks without a commit with `pre-commit run -a`.
