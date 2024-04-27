.PHONY: build

python = python

build:
	${python} -m build

pip = pip

install:
	${pip} install . -U

install-editable:
	${pip} install -e .[dev] --config-settings editable_mode=compat

test:
	ruff .
	pytest