web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn portfolioapi.wsgi --log-file -
release: python manage.py migrate
