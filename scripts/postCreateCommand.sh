#!/bin/bash

# Create python virtual env and install packages
virtualenv $PWD/venv
source $PWD/venv/bin/activate
pip3 install -r $PWD/requirements.txt
