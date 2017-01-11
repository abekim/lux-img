#!/bin/sh

# Install necessary PIL dependencies
brew install libjpeg libpng

# Install necessary Python dependencies
pip install -Ur requirements.txt
