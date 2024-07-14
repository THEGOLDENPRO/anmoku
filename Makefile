.PHONY: build

PYTHON = python

build:
	${PYTHON} -m build

PIP = pip

install:
	${PIP} install . -U

install-editable:
	${PIP} install -e .[dev] --config-settings editable_mode=compat

test:
	ruff check .
	pytest -v