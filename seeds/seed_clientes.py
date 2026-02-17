"""
Seed script para criar 130 clientes.
Uso: uv run python manage.py shell < seeds/seed_clientes.py
"""

import random
import unicodedata
from datetime import date

from casas_floripa.models import Cliente

PROVEDORES = ["gmail.com", "hotmail.com", "yahoo.com.br", "bol.com.br", "outlook.com"]

random.seed(42)

CLIENTES = [
    {"nome": "Ana", "sobrenome": "Silva", "telefone": "(48) 99101-2001", "status_financeiro": "regular", "data_nascimento": date(1985, 3, 15)},
    {"nome": "Bruno", "sobrenome": "Santos", "telefone": "(48) 99102-2002", "status_financeiro": "regular", "data_nascimento": date(1990, 7, 22)},
    {"nome": "Carla", "sobrenome": "Oliveira", "telefone": "(48) 99103-2003", "status_financeiro": "pendente", "data_nascimento": date(1978, 11, 8)},
    {"nome": "Daniel", "sobrenome": "Souza", "telefone": "(48) 99104-2004", "status_financeiro": "regular", "data_nascimento": date(1995, 1, 30)},
    {"nome": "Eduarda", "sobrenome": "Pereira", "telefone": "(48) 99105-2005", "status_financeiro": "bloqueado", "data_nascimento": date(1982, 6, 12)},
    {"nome": "Felipe", "sobrenome": "Costa", "telefone": "(48) 99106-2006", "status_financeiro": "regular", "data_nascimento": date(2000, 9, 5)},
    {"nome": "Gabriela", "sobrenome": "Ferreira", "telefone": "(48) 99107-2007", "status_financeiro": "regular", "data_nascimento": date(1973, 4, 18)},
    {"nome": "Henrique", "sobrenome": "Rodrigues", "telefone": "(48) 99108-2008", "status_financeiro": "pendente", "data_nascimento": date(1988, 12, 25)},
    {"nome": "Isabela", "sobrenome": "Almeida", "telefone": "(48) 99109-2009", "status_financeiro": "regular", "data_nascimento": date(1965, 2, 14)},
    {"nome": "João", "sobrenome": "Nascimento", "telefone": "(48) 99110-2010", "status_financeiro": "regular", "data_nascimento": date(1998, 8, 7)},
    {"nome": "Karina", "sobrenome": "Lima", "telefone": "(48) 99111-2011", "status_financeiro": "bloqueado", "data_nascimento": date(1955, 5, 20)},
    {"nome": "Lucas", "sobrenome": "Gomes", "telefone": "(48) 99112-2012", "status_financeiro": "regular", "data_nascimento": date(2003, 10, 3)},
    {"nome": "Mariana", "sobrenome": "Ribeiro", "telefone": "(48) 99113-2013", "status_financeiro": "regular", "data_nascimento": date(1992, 7, 16)},
    {"nome": "Nicolas", "sobrenome": "Martins", "telefone": "(48) 99114-2014", "status_financeiro": "pendente", "data_nascimento": date(1980, 3, 28)},
    {"nome": "Olívia", "sobrenome": "Araújo", "telefone": "(48) 99115-2015", "status_financeiro": "regular", "data_nascimento": date(1970, 11, 11)},
    {"nome": "Pedro", "sobrenome": "Barbosa", "telefone": "(48) 99116-2016", "status_financeiro": "regular", "data_nascimento": date(2005, 1, 9)},
    {"nome": "Rafaela", "sobrenome": "Cardoso", "telefone": "(48) 99117-2017", "status_financeiro": "bloqueado", "data_nascimento": date(1948, 6, 30)},
    {"nome": "Samuel", "sobrenome": "Cavalcanti", "telefone": "(48) 99118-2018", "status_financeiro": "regular", "data_nascimento": date(1996, 4, 22)},
    {"nome": "Tatiana", "sobrenome": "Monteiro", "telefone": "(48) 99119-2019", "status_financeiro": "regular", "data_nascimento": date(1987, 9, 15)},
    {"nome": "Ulisses", "sobrenome": "Teixeira", "telefone": "(48) 99120-2020", "status_financeiro": "pendente", "data_nascimento": date(1960, 12, 1)},
    {"nome": "Valentina", "sobrenome": "Correia", "telefone": "(48) 99121-2021", "status_financeiro": "regular", "data_nascimento": date(2007, 2, 18)},
    {"nome": "Wagner", "sobrenome": "Dias", "telefone": "(48) 99122-2022", "status_financeiro": "regular", "data_nascimento": date(1975, 8, 4)},
    {"nome": "Ximena", "sobrenome": "Moreira", "telefone": "(48) 99123-2023", "status_financeiro": "regular", "data_nascimento": date(1943, 5, 27)},
    {"nome": "Yago", "sobrenome": "Campos", "telefone": "(48) 99124-2024", "status_financeiro": "bloqueado", "data_nascimento": date(1999, 10, 13)},
    {"nome": "Zilda", "sobrenome": "Mendes", "telefone": "(48) 99125-2025", "status_financeiro": "regular", "data_nascimento": date(1941, 7, 8)},
    {"nome": "Adriana", "sobrenome": "Rocha", "telefone": "(48) 99126-2026", "status_financeiro": "pendente", "data_nascimento": date(1993, 3, 21)},
    {"nome": "Bernardo", "sobrenome": "Pinto", "telefone": "(48) 99127-2027", "status_financeiro": "regular", "data_nascimento": date(2001, 6, 14)},
    {"nome": "Cecília", "sobrenome": "Freitas", "telefone": "(48) 99128-2028", "status_financeiro": "regular", "data_nascimento": date(1968, 9, 30)},
    {"nome": "Diego", "sobrenome": "Vieira", "telefone": "(48) 99129-2029", "status_financeiro": "regular", "data_nascimento": date(1984, 12, 17)},
    {"nome": "Elisa", "sobrenome": "Carvalho", "telefone": "(48) 99130-2030", "status_financeiro": "pendente", "data_nascimento": date(2006, 4, 5)},
    # 100 clientes adicionais
    {"nome": "Renata", "sobrenome": "Lopes", "telefone": "(48) 99131-2031", "status_financeiro": "regular", "data_nascimento": date(1991, 5, 12)},
    {"nome": "Thiago", "sobrenome": "Azevedo", "telefone": "(48) 99132-2032", "status_financeiro": "regular", "data_nascimento": date(1983, 9, 28)},
    {"nome": "Larissa", "sobrenome": "Nunes", "telefone": "(48) 99133-2033", "status_financeiro": "pendente", "data_nascimento": date(1997, 2, 7)},
    {"nome": "Rodrigo", "sobrenome": "Barros", "telefone": "(48) 99134-2034", "status_financeiro": "regular", "data_nascimento": date(1976, 11, 19)},
    {"nome": "Patrícia", "sobrenome": "Fonseca", "telefone": "(48) 99135-2035", "status_financeiro": "regular", "data_nascimento": date(1988, 7, 3)},
    {"nome": "Marcos", "sobrenome": "Cunha", "telefone": "(48) 99136-2036", "status_financeiro": "bloqueado", "data_nascimento": date(1962, 4, 25)},
    {"nome": "Juliana", "sobrenome": "Ramos", "telefone": "(48) 99137-2037", "status_financeiro": "regular", "data_nascimento": date(2002, 1, 14)},
    {"nome": "Gustavo", "sobrenome": "Moura", "telefone": "(48) 99138-2038", "status_financeiro": "regular", "data_nascimento": date(1994, 8, 21)},
    {"nome": "Fernanda", "sobrenome": "Batista", "telefone": "(48) 99139-2039", "status_financeiro": "pendente", "data_nascimento": date(1971, 3, 9)},
    {"nome": "Rafael", "sobrenome": "Duarte", "telefone": "(48) 99140-2040", "status_financeiro": "regular", "data_nascimento": date(1986, 12, 5)},
    {"nome": "Camila", "sobrenome": "Melo", "telefone": "(48) 99141-2041", "status_financeiro": "regular", "data_nascimento": date(1999, 6, 18)},
    {"nome": "André", "sobrenome": "Pires", "telefone": "(48) 99142-2042", "status_financeiro": "regular", "data_nascimento": date(1957, 10, 30)},
    {"nome": "Letícia", "sobrenome": "Machado", "telefone": "(48) 99143-2043", "status_financeiro": "bloqueado", "data_nascimento": date(2004, 5, 22)},
    {"nome": "Fábio", "sobrenome": "Sampaio", "telefone": "(48) 99144-2044", "status_financeiro": "regular", "data_nascimento": date(1980, 9, 11)},
    {"nome": "Aline", "sobrenome": "Borges", "telefone": "(48) 99145-2045", "status_financeiro": "regular", "data_nascimento": date(1993, 1, 27)},
    {"nome": "Leandro", "sobrenome": "Assis", "telefone": "(48) 99146-2046", "status_financeiro": "pendente", "data_nascimento": date(1967, 7, 16)},
    {"nome": "Priscila", "sobrenome": "Miranda", "telefone": "(48) 99147-2047", "status_financeiro": "regular", "data_nascimento": date(1989, 4, 8)},
    {"nome": "Vinícius", "sobrenome": "Pacheco", "telefone": "(48) 99148-2048", "status_financeiro": "regular", "data_nascimento": date(2001, 11, 2)},
    {"nome": "Débora", "sobrenome": "Andrade", "telefone": "(48) 99149-2049", "status_financeiro": "regular", "data_nascimento": date(1974, 6, 20)},
    {"nome": "Marcelo", "sobrenome": "Nogueira", "telefone": "(48) 99150-2050", "status_financeiro": "bloqueado", "data_nascimento": date(1952, 8, 14)},
    {"nome": "Viviane", "sobrenome": "Rezende", "telefone": "(48) 99151-2051", "status_financeiro": "regular", "data_nascimento": date(1996, 2, 28)},
    {"nome": "Carlos", "sobrenome": "Dantas", "telefone": "(48) 99152-2052", "status_financeiro": "regular", "data_nascimento": date(1981, 10, 6)},
    {"nome": "Simone", "sobrenome": "Brito", "telefone": "(48) 99153-2053", "status_financeiro": "pendente", "data_nascimento": date(1963, 3, 17)},
    {"nome": "Eduardo", "sobrenome": "Tavares", "telefone": "(48) 99154-2054", "status_financeiro": "regular", "data_nascimento": date(2005, 7, 9)},
    {"nome": "Cláudia", "sobrenome": "Siqueira", "telefone": "(48) 99155-2055", "status_financeiro": "regular", "data_nascimento": date(1977, 12, 23)},
    {"nome": "Roberto", "sobrenome": "Lacerda", "telefone": "(48) 99156-2056", "status_financeiro": "regular", "data_nascimento": date(1945, 5, 1)},
    {"nome": "Luciana", "sobrenome": "Figueiredo", "telefone": "(48) 99157-2057", "status_financeiro": "bloqueado", "data_nascimento": date(1990, 9, 15)},
    {"nome": "Alexandre", "sobrenome": "Aguiar", "telefone": "(48) 99158-2058", "status_financeiro": "regular", "data_nascimento": date(1972, 4, 29)},
    {"nome": "Bianca", "sobrenome": "Coelho", "telefone": "(48) 99159-2059", "status_financeiro": "regular", "data_nascimento": date(2003, 8, 11)},
    {"nome": "Sérgio", "sobrenome": "Medeiros", "telefone": "(48) 99160-2060", "status_financeiro": "pendente", "data_nascimento": date(1958, 1, 5)},
    {"nome": "Natália", "sobrenome": "Guimarães", "telefone": "(48) 99161-2061", "status_financeiro": "regular", "data_nascimento": date(1994, 6, 24)},
    {"nome": "Ricardo", "sobrenome": "Sales", "telefone": "(48) 99162-2062", "status_financeiro": "regular", "data_nascimento": date(1984, 11, 18)},
    {"nome": "Vanessa", "sobrenome": "Alencar", "telefone": "(48) 99163-2063", "status_financeiro": "regular", "data_nascimento": date(1969, 3, 7)},
    {"nome": "Paulo", "sobrenome": "Rego", "telefone": "(48) 99164-2064", "status_financeiro": "bloqueado", "data_nascimento": date(1950, 9, 22)},
    {"nome": "Amanda", "sobrenome": "Valente", "telefone": "(48) 99165-2065", "status_financeiro": "regular", "data_nascimento": date(1998, 5, 16)},
    {"nome": "Otávio", "sobrenome": "Braga", "telefone": "(48) 99166-2066", "status_financeiro": "regular", "data_nascimento": date(1987, 2, 10)},
    {"nome": "Raquel", "sobrenome": "Coutinho", "telefone": "(48) 99167-2067", "status_financeiro": "pendente", "data_nascimento": date(1975, 8, 31)},
    {"nome": "Matheus", "sobrenome": "Queiroz", "telefone": "(48) 99168-2068", "status_financeiro": "regular", "data_nascimento": date(2000, 12, 13)},
    {"nome": "Sandra", "sobrenome": "Magalhães", "telefone": "(48) 99169-2069", "status_financeiro": "regular", "data_nascimento": date(1966, 7, 4)},
    {"nome": "Leonardo", "sobrenome": "Bastos", "telefone": "(48) 99170-2070", "status_financeiro": "regular", "data_nascimento": date(1992, 10, 26)},
    {"nome": "Elaine", "sobrenome": "Soares", "telefone": "(48) 99171-2071", "status_financeiro": "bloqueado", "data_nascimento": date(1953, 4, 19)},
    {"nome": "Caio", "sobrenome": "Vasconcelos", "telefone": "(48) 99172-2072", "status_financeiro": "regular", "data_nascimento": date(2006, 1, 8)},
    {"nome": "Mônica", "sobrenome": "Pinheiro", "telefone": "(48) 99173-2073", "status_financeiro": "regular", "data_nascimento": date(1979, 6, 21)},
    {"nome": "Jorge", "sobrenome": "Xavier", "telefone": "(48) 99174-2074", "status_financeiro": "pendente", "data_nascimento": date(1961, 11, 3)},
    {"nome": "Lívia", "sobrenome": "Castro", "telefone": "(48) 99175-2075", "status_financeiro": "regular", "data_nascimento": date(1997, 3, 14)},
    {"nome": "Antônio", "sobrenome": "Maia", "telefone": "(48) 99176-2076", "status_financeiro": "regular", "data_nascimento": date(1942, 8, 27)},
    {"nome": "Carolina", "sobrenome": "Leal", "telefone": "(48) 99177-2077", "status_financeiro": "regular", "data_nascimento": date(1991, 5, 6)},
    {"nome": "Danilo", "sobrenome": "Bezerra", "telefone": "(48) 99178-2078", "status_financeiro": "bloqueado", "data_nascimento": date(1983, 12, 19)},
    {"nome": "Flávia", "sobrenome": "Marques", "telefone": "(48) 99179-2079", "status_financeiro": "regular", "data_nascimento": date(1970, 2, 11)},
    {"nome": "Hugo", "sobrenome": "Chaves", "telefone": "(48) 99180-2080", "status_financeiro": "regular", "data_nascimento": date(2004, 9, 23)},
    {"nome": "Ingrid", "sobrenome": "Paiva", "telefone": "(48) 99181-2081", "status_financeiro": "pendente", "data_nascimento": date(1986, 7, 15)},
    {"nome": "Júlio", "sobrenome": "Esteves", "telefone": "(48) 99182-2082", "status_financeiro": "regular", "data_nascimento": date(1956, 4, 2)},
    {"nome": "Karen", "sobrenome": "Fontes", "telefone": "(48) 99183-2083", "status_financeiro": "regular", "data_nascimento": date(1995, 11, 28)},
    {"nome": "Lúcio", "sobrenome": "Amaral", "telefone": "(48) 99184-2084", "status_financeiro": "regular", "data_nascimento": date(1974, 1, 17)},
    {"nome": "Milena", "sobrenome": "Reis", "telefone": "(48) 99185-2085", "status_financeiro": "bloqueado", "data_nascimento": date(2002, 6, 9)},
    {"nome": "Nelson", "sobrenome": "Cruz", "telefone": "(48) 99186-2086", "status_financeiro": "regular", "data_nascimento": date(1947, 10, 21)},
    {"nome": "Paloma", "sobrenome": "Henrique", "telefone": "(48) 99187-2087", "status_financeiro": "regular", "data_nascimento": date(1989, 3, 4)},
    {"nome": "Rui", "sobrenome": "Santiago", "telefone": "(48) 99188-2088", "status_financeiro": "pendente", "data_nascimento": date(1968, 8, 16)},
    {"nome": "Socorro", "sobrenome": "Trindade", "telefone": "(48) 99189-2089", "status_financeiro": "regular", "data_nascimento": date(1944, 12, 29)},
    {"nome": "Tomás", "sobrenome": "Carneiro", "telefone": "(48) 99190-2090", "status_financeiro": "regular", "data_nascimento": date(1993, 5, 20)},
    {"nome": "Úrsula", "sobrenome": "Ventura", "telefone": "(48) 99191-2091", "status_financeiro": "regular", "data_nascimento": date(1981, 9, 7)},
    {"nome": "Vera", "sobrenome": "Porto", "telefone": "(48) 99192-2092", "status_financeiro": "bloqueado", "data_nascimento": date(1959, 2, 22)},
    {"nome": "Wesley", "sobrenome": "Arruda", "telefone": "(48) 99193-2093", "status_financeiro": "regular", "data_nascimento": date(2007, 7, 13)},
    {"nome": "Yasmin", "sobrenome": "Pedrosa", "telefone": "(48) 99194-2094", "status_financeiro": "regular", "data_nascimento": date(1996, 4, 1)},
    {"nome": "Álvaro", "sobrenome": "Bittencourt", "telefone": "(48) 99195-2095", "status_financeiro": "pendente", "data_nascimento": date(1977, 11, 25)},
    {"nome": "Betânia", "sobrenome": "Florêncio", "telefone": "(48) 99196-2096", "status_financeiro": "regular", "data_nascimento": date(1964, 6, 8)},
    {"nome": "Cássio", "sobrenome": "Prado", "telefone": "(48) 99197-2097", "status_financeiro": "regular", "data_nascimento": date(1990, 1, 19)},
    {"nome": "Dalila", "sobrenome": "Rangel", "telefone": "(48) 99198-2098", "status_financeiro": "regular", "data_nascimento": date(2005, 10, 31)},
    {"nome": "Emílio", "sobrenome": "Sá", "telefone": "(48) 99199-2099", "status_financeiro": "bloqueado", "data_nascimento": date(1949, 3, 12)},
    {"nome": "Fabiana", "sobrenome": "Toledo", "telefone": "(48) 99200-2100", "status_financeiro": "regular", "data_nascimento": date(1985, 8, 24)},
    {"nome": "Gilberto", "sobrenome": "Amorim", "telefone": "(48) 99201-2101", "status_financeiro": "regular", "data_nascimento": date(1972, 5, 6)},
    {"nome": "Helena", "sobrenome": "Viana", "telefone": "(48) 99202-2102", "status_financeiro": "pendente", "data_nascimento": date(1998, 12, 18)},
    {"nome": "Igor", "sobrenome": "Silveira", "telefone": "(48) 99203-2103", "status_financeiro": "regular", "data_nascimento": date(1960, 7, 10)},
    {"nome": "Joana", "sobrenome": "Brandão", "telefone": "(48) 99204-2104", "status_financeiro": "regular", "data_nascimento": date(2003, 2, 23)},
    {"nome": "Klaus", "sobrenome": "Telles", "telefone": "(48) 99205-2105", "status_financeiro": "regular", "data_nascimento": date(1979, 9, 14)},
    {"nome": "Lorena", "sobrenome": "Guedes", "telefone": "(48) 99206-2106", "status_financeiro": "bloqueado", "data_nascimento": date(1954, 4, 27)},
    {"nome": "Murilo", "sobrenome": "Pessoa", "telefone": "(48) 99207-2107", "status_financeiro": "regular", "data_nascimento": date(1992, 11, 9)},
    {"nome": "Nair", "sobrenome": "Cabral", "telefone": "(48) 99208-2108", "status_financeiro": "regular", "data_nascimento": date(1940, 6, 2)},
    {"nome": "Oscar", "sobrenome": "Motta", "telefone": "(48) 99209-2109", "status_financeiro": "pendente", "data_nascimento": date(1987, 1, 21)},
    {"nome": "Paula", "sobrenome": "Santana", "telefone": "(48) 99210-2110", "status_financeiro": "regular", "data_nascimento": date(1973, 8, 13)},
    {"nome": "Renato", "sobrenome": "Chagas", "telefone": "(48) 99211-2111", "status_financeiro": "regular", "data_nascimento": date(2001, 3, 5)},
    {"nome": "Sueli", "sobrenome": "Cordeiro", "telefone": "(48) 99212-2112", "status_financeiro": "regular", "data_nascimento": date(1965, 10, 17)},
    {"nome": "Tânia", "sobrenome": "Bentes", "telefone": "(48) 99213-2113", "status_financeiro": "bloqueado", "data_nascimento": date(1951, 5, 29)},
    {"nome": "Ubiratã", "sobrenome": "Lins", "telefone": "(48) 99214-2114", "status_financeiro": "regular", "data_nascimento": date(1994, 12, 11)},
    {"nome": "Valéria", "sobrenome": "Proença", "telefone": "(48) 99215-2115", "status_financeiro": "regular", "data_nascimento": date(1982, 7, 24)},
    {"nome": "Wilson", "sobrenome": "Farias", "telefone": "(48) 99216-2116", "status_financeiro": "pendente", "data_nascimento": date(1946, 2, 6)},
    {"nome": "Xuxa", "sobrenome": "Mattos", "telefone": "(48) 99217-2117", "status_financeiro": "regular", "data_nascimento": date(1976, 9, 18)},
    {"nome": "Yuri", "sobrenome": "Fragoso", "telefone": "(48) 99218-2118", "status_financeiro": "regular", "data_nascimento": date(2000, 4, 30)},
    {"nome": "Zélia", "sobrenome": "Drummond", "telefone": "(48) 99219-2119", "status_financeiro": "regular", "data_nascimento": date(1969, 11, 12)},
    {"nome": "Aparecida", "sobrenome": "Seabra", "telefone": "(48) 99220-2120", "status_financeiro": "bloqueado", "data_nascimento": date(1943, 6, 25)},
    {"nome": "Benedito", "sobrenome": "Couto", "telefone": "(48) 99221-2121", "status_financeiro": "regular", "data_nascimento": date(1991, 1, 7)},
    {"nome": "Conceição", "sobrenome": "Luz", "telefone": "(48) 99222-2122", "status_financeiro": "regular", "data_nascimento": date(1978, 8, 19)},
    {"nome": "Dorival", "sobrenome": "Bueno", "telefone": "(48) 99223-2123", "status_financeiro": "pendente", "data_nascimento": date(1957, 3, 3)},
    {"nome": "Eunice", "sobrenome": "Guerra", "telefone": "(48) 99224-2124", "status_financeiro": "regular", "data_nascimento": date(2006, 10, 15)},
    {"nome": "Francisco", "sobrenome": "Rabelo", "telefone": "(48) 99225-2125", "status_financeiro": "regular", "data_nascimento": date(1984, 5, 28)},
    {"nome": "Graça", "sobrenome": "Macedo", "telefone": "(48) 99226-2126", "status_financeiro": "regular", "data_nascimento": date(1971, 12, 10)},
    {"nome": "Heloísa", "sobrenome": "Padilha", "telefone": "(48) 99227-2127", "status_financeiro": "bloqueado", "data_nascimento": date(1948, 7, 22)},
    {"nome": "Ivo", "sobrenome": "Passos", "telefone": "(48) 99228-2128", "status_financeiro": "regular", "data_nascimento": date(1997, 2, 4)},
    {"nome": "Josefa", "sobrenome": "Barreto", "telefone": "(48) 99229-2129", "status_financeiro": "regular", "data_nascimento": date(1966, 9, 16)},
    {"nome": "Lázaro", "sobrenome": "Pimentel", "telefone": "(48) 99230-2130", "status_financeiro": "regular", "data_nascimento": date(1988, 4, 8)},
]


def remover_acentos(texto):
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")


def gerar_email(nome, sobrenome):
    local = f"{remover_acentos(nome).lower()}.{remover_acentos(sobrenome).lower()}"
    provedor = random.choice(PROVEDORES)
    return f"{local}@{provedor}"


def run():
    Cliente.objects.all().delete()
    print("Clientes existentes removidos.")

    created = 0
    for dados in CLIENTES:
        dados["email"] = gerar_email(dados["nome"], dados["sobrenome"])
        Cliente.objects.create(**dados)
        created += 1

    print(f"Criados {created} clientes. Total: {Cliente.objects.count()}")


run()
