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

build-docs:
	cd docs && make html

build-clean-docs:
	cd docs && make clean && make html