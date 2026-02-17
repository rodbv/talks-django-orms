"""
Seed script para criar 30 clientes.
Uso: uv run python manage.py shell < seeds/seed_clientes.py
"""

import random
from datetime import date

from casas_floripa.models import Cliente

CLIENTES = [
    {"first_name": "Ana", "last_name": "Silva", "celular": "(48) 99101-2001", "status_financeiro": "regular", "data_nascimento": date(1985, 3, 15)},
    {"first_name": "Bruno", "last_name": "Santos", "celular": "(48) 99102-2002", "status_financeiro": "regular", "data_nascimento": date(1990, 7, 22)},
    {"first_name": "Carla", "last_name": "Oliveira", "celular": "(48) 99103-2003", "status_financeiro": "pendente", "data_nascimento": date(1978, 11, 8)},
    {"first_name": "Daniel", "last_name": "Souza", "celular": "(48) 99104-2004", "status_financeiro": "regular", "data_nascimento": date(1995, 1, 30)},
    {"first_name": "Eduarda", "last_name": "Pereira", "celular": "(48) 99105-2005", "status_financeiro": "bloqueado", "data_nascimento": date(1982, 6, 12)},
    {"first_name": "Felipe", "last_name": "Costa", "celular": "(48) 99106-2006", "status_financeiro": "regular", "data_nascimento": date(2000, 9, 5)},
    {"first_name": "Gabriela", "last_name": "Ferreira", "celular": "(48) 99107-2007", "status_financeiro": "regular", "data_nascimento": date(1973, 4, 18)},
    {"first_name": "Henrique", "last_name": "Rodrigues", "celular": "(48) 99108-2008", "status_financeiro": "pendente", "data_nascimento": date(1988, 12, 25)},
    {"first_name": "Isabela", "last_name": "Almeida", "celular": "(48) 99109-2009", "status_financeiro": "regular", "data_nascimento": date(1965, 2, 14)},
    {"first_name": "João", "last_name": "Nascimento", "celular": "(48) 99110-2010", "status_financeiro": "regular", "data_nascimento": date(1998, 8, 7)},
    {"first_name": "Karina", "last_name": "Lima", "celular": "(48) 99111-2011", "status_financeiro": "bloqueado", "data_nascimento": date(1955, 5, 20)},
    {"first_name": "Lucas", "last_name": "Gomes", "celular": "(48) 99112-2012", "status_financeiro": "regular", "data_nascimento": date(2003, 10, 3)},
    {"first_name": "Mariana", "last_name": "Ribeiro", "celular": "(48) 99113-2013", "status_financeiro": "regular", "data_nascimento": date(1992, 7, 16)},
    {"first_name": "Nicolas", "last_name": "Martins", "celular": "(48) 99114-2014", "status_financeiro": "pendente", "data_nascimento": date(1980, 3, 28)},
    {"first_name": "Olívia", "last_name": "Araújo", "celular": "(48) 99115-2015", "status_financeiro": "regular", "data_nascimento": date(1970, 11, 11)},
    {"first_name": "Pedro", "last_name": "Barbosa", "celular": "(48) 99116-2016", "status_financeiro": "regular", "data_nascimento": date(2005, 1, 9)},
    {"first_name": "Rafaela", "last_name": "Cardoso", "celular": "(48) 99117-2017", "status_financeiro": "bloqueado", "data_nascimento": date(1948, 6, 30)},
    {"first_name": "Samuel", "last_name": "Cavalcanti", "celular": "(48) 99118-2018", "status_financeiro": "regular", "data_nascimento": date(1996, 4, 22)},
    {"first_name": "Tatiana", "last_name": "Monteiro", "celular": "(48) 99119-2019", "status_financeiro": "regular", "data_nascimento": date(1987, 9, 15)},
    {"first_name": "Ulisses", "last_name": "Teixeira", "celular": "(48) 99120-2020", "status_financeiro": "pendente", "data_nascimento": date(1960, 12, 1)},
    {"first_name": "Valentina", "last_name": "Correia", "celular": "(48) 99121-2021", "status_financeiro": "regular", "data_nascimento": date(2007, 2, 18)},
    {"first_name": "Wagner", "last_name": "Dias", "celular": "(48) 99122-2022", "status_financeiro": "regular", "data_nascimento": date(1975, 8, 4)},
    {"first_name": "Ximena", "last_name": "Moreira", "celular": "(48) 99123-2023", "status_financeiro": "regular", "data_nascimento": date(1943, 5, 27)},
    {"first_name": "Yago", "last_name": "Campos", "celular": "(48) 99124-2024", "status_financeiro": "bloqueado", "data_nascimento": date(1999, 10, 13)},
    {"first_name": "Zilda", "last_name": "Mendes", "celular": "(48) 99125-2025", "status_financeiro": "regular", "data_nascimento": date(1941, 7, 8)},
    {"first_name": "Adriana", "last_name": "Rocha", "celular": "(48) 99126-2026", "status_financeiro": "pendente", "data_nascimento": date(1993, 3, 21)},
    {"first_name": "Bernardo", "last_name": "Pinto", "celular": "(48) 99127-2027", "status_financeiro": "regular", "data_nascimento": date(2001, 6, 14)},
    {"first_name": "Cecília", "last_name": "Freitas", "celular": "(48) 99128-2028", "status_financeiro": "regular", "data_nascimento": date(1968, 9, 30)},
    {"first_name": "Diego", "last_name": "Vieira", "celular": "(48) 99129-2029", "status_financeiro": "regular", "data_nascimento": date(1984, 12, 17)},
    {"first_name": "Elisa", "last_name": "Carvalho", "celular": "(48) 99130-2030", "status_financeiro": "pendente", "data_nascimento": date(2006, 4, 5)},
]


def run():
    created = 0
    for i, dados in enumerate(CLIENTES, start=1):
        username = f"{dados['first_name'].lower()}.{dados['last_name'].lower()}"
        email = f"{username}@email.com"

        if Cliente.objects.filter(username=username).exists():
            print(f"  Já existe: {username}")
            continue

        Cliente.objects.create_user(
            username=username,
            email=email,
            password="senha123",
            first_name=dados["first_name"],
            last_name=dados["last_name"],
            celular=dados["celular"],
            status_financeiro=dados["status_financeiro"],
            data_nascimento=dados["data_nascimento"],
        )
        created += 1

    print(f"Criados {created} clientes. Total: {Cliente.objects.count()}")


run()
