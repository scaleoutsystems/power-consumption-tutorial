#!/bin/bash

# Install virtualenv
python3 -m pip install virtualenv

# Init venv
python3 -m virtualenv .power-consumption-keras

# Pip deps
.power-consumption-keras/bin/pip install --upgrade pip
.power-consumption-keras/bin/pip install -r requirements.txt
