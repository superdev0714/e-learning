#!/bin/bash

# Collect static files
python manage.py collectstatic --no-input

# Migrate database changes
python manage.py migrate

# Start development server
python manage.py runserver 0.0.0.0:8000
