#!/usr/bin/env bash
sudo apt-get update
sudo apt-get -y install python-dev build-essential 
sudo apt-get -y install freetds-dev
sudo apt-get -y install python-pip
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
virtualenv venv
source venv/bin/activate
pip install -U setuptools
pip install -r requirements.txt
deactivate
