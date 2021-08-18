#!/usr/bin/env bash

sleep 5
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py graph_models caseapi -g -o static/caseapi_model.png
gunicorn caserepo.wsgi:application --bind 0.0.0.0:8000