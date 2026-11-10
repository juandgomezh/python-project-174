install:
	poetry install

lint:
	poetry run ruff check --no-cache

build:
	poetry build

test:
    poetry run pytest --cov=gendiff --cov-report=term-missing

.PHONY: install lint test build