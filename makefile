install:
	poetry install

lint:
	poetry run ruff check --no-cache

build:
	poetry build

.PHONY: install lint build