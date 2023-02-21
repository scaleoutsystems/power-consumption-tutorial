#!/bin/bash
set -e

# Init venv
python -m venv .power-consumption-keras

# Pip deps
.power-consumption-keras/bin/pip install --upgrade pip
.power-consumption-keras/bin/pip install -e ../../fedn
.power-consumption-keras/bin/pip install -r requirements.txt
