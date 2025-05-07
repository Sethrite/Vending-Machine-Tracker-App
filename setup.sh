#!/bin/bash

# Download pipenv
pip install pipenv

# Download dependencies
pipenv install pyarduino django pillow

# Setup virtual environment
pipenv shell

# Set up Django settings
export DJANGO_SETTINGS_MODULE=App.settings

# Setup for the database assets and relations, also setting up Serial Connections
python manage.py shell < setupVendingMachine.py
python manage.py shell < setupSerial.py

# Running the server, locally hosted on the computer.
# Using 3 different terminals to run the different commands in the background
echo "Starting Django server..."
pipenv run python manage.py runserver &
sleep 3

echo "Decreasing snack counts periodically..."
pipenv run python manage.py decrement_snacks &
sleep 3

pipenv run python manage.py demonstration &