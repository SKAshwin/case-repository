#!/usr/bin/env bash

python manage.py collectstatic --noinput
gunicorn caserepo.wsgi:application --bind 0.0.0.0:80