#!/bin/bash
WORKSPACE=/workspaces/web-scraping-python

# Create python virtual env and install packages
virtualenv $WORKSPACE/venv
source $WORKSPACE/venv/bin/activate
pip3 install -r $WORKSPACE/requirements.txt
