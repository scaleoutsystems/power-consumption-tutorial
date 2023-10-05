#!/bin/bash

# Install virtualenv
python3 -m pip install virtualenv

# Init venv
python3 -m virtualenv .power-consumption-pytorch

# Pip deps
.power-consumption-pytorch/bin/pip install --upgrade pip
.power-consumption-pytorch/bin/pip install -e /home/ubuntu/fedn/fedn
.power-consumption-pytorch/bin/pip install -r requirements-osx-m1.txt
