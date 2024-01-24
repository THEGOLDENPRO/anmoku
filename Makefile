.PHONY: build

python = python

build:
	${python} -m build --wheel

pip = pip

install:
	${pip} install . -U

install-dev:
	${pip} install .[dev] -U

install-editable:
	${pip} install -e . --config-settings editable_mode=compat

test:
	ruff .
	pytest