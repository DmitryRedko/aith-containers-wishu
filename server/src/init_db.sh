#!/usr/bin/env bash

# Создание миграций
python3 manage.py makemigrations
# применение миграций
python3 manage.py migrate
# Восстановление из бэкапа
python3 manage.py loaddata backup.json