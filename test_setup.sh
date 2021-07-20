#!/usr/bin/env bash

sleep 5
python manage.py migrate 
python manage.py loaddata dump.json 
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
gunicorn caserepo.wsgi:application --bind 0.0.0.0:8000