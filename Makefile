SHELL := /bin/bash

setup:
	@./scripts/python-init.sh

run:
	make setup
	pipenv run python3 -m aimi

test:
	make setup
	pipenv run python3 -m aimi -t
