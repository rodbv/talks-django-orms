# Rodar o servidor
run:
    uv run python manage.py runserver

# Criar migrações e aplicar
mmm:
    uv run python manage.py makemigrations
    uv run python manage.py migrate

# Rodar todos os seeds
seed:
    uv run python manage.py seed
