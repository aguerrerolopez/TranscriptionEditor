#!/bin/bash

# Echo the process
echo "Installing the required packages..."
# Create a virtual environment
python3 -m venv manual_transcriptor
echo "Virtual environment created."

echo "Activating the virtual environment..."
# Activate the virtual environment
source manual_transcriptor/bin/activate

echo "Installing the required packages..."
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

echo "Installation complete. Run ./run.sh to run the app."