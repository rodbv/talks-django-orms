# Rodar o servidor (sem Silk nem DDT)
run:
    uv run python manage.py runserver

# Rodar com Silk (profiling em /silk/)
silk:
    SILK=TRUE uv run python manage.py runserver

# Rodar com Django Debug Toolbar (em /__debug__/)
ddt:
    DDT=TRUE uv run python manage.py runserver

# Criar migrações e aplicar
mmm:
    uv run python manage.py makemigrations
    uv run python manage.py migrate

# Rodar todos os seeds
seed:
    uv run python manage.py seed

# Rodar testes (pytest)
test:
    uv run --group dev pytest

# Servir os slides (Reveal.js). Abra a URL que aparecer (ex.: http://localhost:3000)
slides:
    cd slides && npx serve .

# Servir os slides com hot reload (recarrega ao editar slides.md ou index.html)
slides-watch:
    cd slides && npx live-server . --port=3000 --no-browser

# Compactar o banco SQLite (rodar após limpar dados do Silk)
vacuum:
    uv run python manage.py shell -c "import sqlite3; from django.conf import settings; conn = sqlite3.connect(settings.DATABASES['default']['NAME']); conn.execute('VACUUM'); conn.close(); print('VACUUM done')"
