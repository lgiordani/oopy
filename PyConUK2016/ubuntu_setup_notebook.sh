#!/bin/bash

# This script sets up the Jupyter Notebook development environment

sudo apt-get install -y python3-dev build-essential virtualenv

virtualenv -p python3 venv3 
source venv3/bin/activate

pip install -U pip
pip install jupyter
