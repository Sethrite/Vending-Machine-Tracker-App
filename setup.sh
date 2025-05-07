#!/bin/bash

# Download pipenv
pip install pipenv

# Download dependencies
pipenv install pyarduino django pillow

# Set up Django settings
export DJANGO_SETTINGS_MODULE=App.settings

# Making and applying the migrations to the database
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

# Setup for the database assets and relations, also setting up Serial Connections
pipenv run python manage.py setup_vending

# If you have a serial connection through usb, uncomment this
# pipenv run python manage.py setup_serial

# Running the server, locally hosted on the computer.
# Using 3 different terminals to run the different commands in the background
echo "Starting Django server..."
pipenv run python manage.py runserver &
sleep 3

echo "Decreasing snack counts periodically..."
pipenv run python manage.py decrement_snacks &
sleep 3

# Open the web app in the default browser
echo "Opening browser..."
powershell.exe -Command "Start-Process 'http://127.0.0.1:8000/'"