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

# Servir os slides (Reveal.js). Abra a URL que aparecer (ex.: http://localhost:3000)
slides:
    cd slides && npx serve .

# Compactar o banco SQLite (rodar após limpar dados do Silk)
vacuum:
    uv run python manage.py shell -c "import sqlite3; from django.conf import settings; conn = sqlite3.connect(settings.DATABASES['default']['NAME']); conn.execute('VACUUM'); conn.close(); print('VACUUM done')"
