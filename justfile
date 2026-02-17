run:
    uv run python manage.py runserver

test:
    uv run python manage.py test

mmm:
    uv run python manage.py makemigrations
    uv run python manage.py migrate

shell:
    uv run python manage.py shell

createsuperuser:
    uv run python manage.py createsuperuser
