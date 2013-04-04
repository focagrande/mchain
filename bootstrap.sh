#!/bin/bash

apt-get install -y unzip
apt-get install -y python-pip

pip install jsonrpclib
pip install tornado

sudo wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

