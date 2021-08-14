#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn caserepo.wsgi:application --bind 0.0.0.0:8000