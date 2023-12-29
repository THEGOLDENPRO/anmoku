.PHONY: build

build:
	python -m build --wheel

install:
	pip install . -U

install-dev:
	pip install .[dev] -U

install-editable:
	pip install -e . --config-settings editable_mode=compat

test:
	ruff .
	pytest