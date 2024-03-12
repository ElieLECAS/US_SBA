#!/bin/sh

echo "Effectuer les migrations"
python manage.py makemigrations && python manage.py migrate

python manage.py collectstatic --no-input

echo "Lancer le serveur"

gunicorn sba_app.wsgi:application --workers=2 --timeout 120 --bind=0.0.0.0:8001