#!/bin/sh
# Entrypoint for our application. Making sure the db is avaible.

set -e
  
host="$1"
port="$2"

while ! nc -z $host $port; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing backend-service"

flask db init
flask db revision -m "create tables"
flask db upgrade
gunicorn -b 0.0.0.0:5000 --access-logfile /var/logs/sennder/sennder.logs --capture-output --enable-stdio-inheritance --log-level debug app:app