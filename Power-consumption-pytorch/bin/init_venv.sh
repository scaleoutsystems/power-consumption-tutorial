#!/bin/bash
set -e

# Init venv
python -m venv .power-consumption-pytorch

# Pip deps
.power-consumption-pytorch/bin/pip install --upgrade pip
.power-consumption-pytorch/bin/pip install -e /home/ubuntu/fedn/fedn
.power-consumption-pytorch/bin/pip install -r requirements.txt --no-cache-dir
