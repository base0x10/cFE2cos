#!/bin/bash

sudo apt-get update
# Tools nessesary for both composite and the cFE
sudo apt-get -y install make

# Tools nessesary for the cFE
sudo apt-get -y install cmake

# Tools nessesary for the cFE tools
sudo apt-get -y install python-qt4
sudo apt-get -y install pyqt4-dev-tools

# Tools nessesary for composite
sudo apt-get -y install bc
sudo apt-get -y install gcc-multilib
sudo apt-get -y install binutils-dev
sudo apt-get -y install qemu-kvm

# Useful tools to have around
sudo apt-get -y install git
sudo apt-get -y install ntp
