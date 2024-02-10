#!/usr/bin/env bash


python3 manage.py makemigrations


python3 manage.py migrate

python3 manage.py collectstatic --no-input

exec gunicorn web_malushka.wsgi -b 0.0.0.0:80 
