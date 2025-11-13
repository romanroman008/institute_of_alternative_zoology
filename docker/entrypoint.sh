#!/bin/sh


echo "Waiting for PostgreSQL..."
until nc -z $DB_HOST $DB_PORT; do
  sleep 1
  echo "Still waiting"

done

echo "PostgreSQL is up"

python manage.py migrate --noinput

python manage.py collectstatic --noinput

echo "Loading initial data..."
python manage.py loaddata animals.json || true


echo "Starting Django"
gunicorn mywebsite.wsgi:application --bind 0.0.0.0:8000

