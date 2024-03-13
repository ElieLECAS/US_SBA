#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "En attente de Postgres..."
    sleep 1
done

echo "Effectuer les migrations"
python manage.py makemigrations && python manage.py migrate

python manage.py collectstatic --no-input

echo "Lancer le serveur"

gunicorn sba_app.wsgi:application --workers=4 --timeout 120 --bind=0.0.0.0:80

# python manage.py runserver 0.0.0.0:80

# >>> from django.conf import settings
# >>> settings.DATABASES