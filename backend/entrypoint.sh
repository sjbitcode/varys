#!/usr/bin/env bash

# python manage.py runserver 0.0.0.0:8000
gunicorn --reload --bind 0.0.0.0:8000 varys.wsgi:application