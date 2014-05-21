#!/bin/sh

# Install necessary PIL dependencies
brew install libjpeg libpng

# Install necessary Python dependencies
pip install -r -U requirements.txt