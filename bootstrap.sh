#!/bin/bash

apt-get install -y unzip
apt-get install -y python-pip
apt-get install -y git

pip install jsonrpclib
pip install tornado
pip install supervisord
pip install requests