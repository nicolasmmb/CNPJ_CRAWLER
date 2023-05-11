SHELL := /bin/bash

install:
	pip install poetry && \
	poetry config virtualenvs.in-project true && \
	poetry install --only=prod && \
	poetry shell && \
	playwright install firefox && \
	echo "Done"

run:
	python main.py
