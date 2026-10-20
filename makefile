install:
    poetry install

lint:
    poetry run ruff check .

build:
    poetry build

.PHONY: install lint build