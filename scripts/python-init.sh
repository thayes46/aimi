#!/usr/bin/env bash

python3 -m pip install --upgrade pip
python3 -m pip install pipenv
pipenv sync

echo "Successfully verified pipenv"