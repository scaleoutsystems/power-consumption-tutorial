#!/bin/bash
set -e

# Install virtualenv
pip install virtualenv

# Init venv
python -m virtualenv .power-consumption-keras

# Pip deps
.power-consumption-keras/bin/pip install --upgrade pip
.power-consumption-keras/bin/pip install -r requirements.txt
