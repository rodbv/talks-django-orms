"""
Seed script para criar categorias e ~40 produtos de eletrodomésticos.
Uso: uv run python manage.py shell < seeds/seed_produtos.py
"""

from decimal import Decimal

from casas_floripa.models import Categoria, Produto

CATEGORIAS = [
    "Eletrodoméstico",
    "Eletrônico",
    "Cozinha",
    "Lavanderia",
    "Climatização",
    "Áudio e Vídeo",
]

PRODUTOS = [
    # Cozinha
    {"nome": "Geladeira Frost Free 375L", "descricao": "Geladeira duplex frost free com 375 litros, painel eletrônico e gaveta de frutas e verduras.", "codigo_fabricante": "GEL-FF375-BR", "preco": Decimal("3299.90"), "quantidade_estoque": 12, "categoria": "Cozinha"},
    {"nome": "Geladeira Inverse 460L", "descricao": "Geladeira inverse com freezer na parte inferior, 460 litros, tecnologia no frost.", "codigo_fabricante": "GEL-INV460-SS", "preco": Decimal("5499.00"), "quantidade_estoque": 5, "categoria": "Cozinha"},
    {"nome": "Fogão 5 Bocas Inox", "descricao": "Fogão 5 bocas com acendimento automático, forno com grill e timer digital.", "codigo_fabricante": "FOG-5B-INOX", "preco": Decimal("1899.90"), "quantidade_estoque": 18, "categoria": "Cozinha"},
    {"nome": "Fogão 4 Bocas Branco", "descricao": "Fogão 4 bocas com acendimento automático, tampa de vidro e forno autolimpante.", "codigo_fabricante": "FOG-4B-BCO", "preco": Decimal("1099.00"), "quantidade_estoque": 25, "categoria": "Cozinha"},
    {"nome": "Micro-ondas 32L", "descricao": "Micro-ondas 32 litros com função tira odor, receitas pré-programadas e painel digital.", "codigo_fabricante": "MCO-32L-PT", "preco": Decimal("699.90"), "quantidade_estoque": 30, "categoria": "Cozinha"},
    {"nome": "Micro-ondas 20L", "descricao": "Micro-ondas compacto 20 litros, ideal para esquentar e descongelar alimentos.", "codigo_fabricante": "MCO-20L-BC", "preco": Decimal("449.90"), "quantidade_estoque": 40, "categoria": "Cozinha"},
    {"nome": "Lava-louças 14 Serviços", "descricao": "Lava-louças para 14 serviços com 6 programas de lavagem e meia carga.", "codigo_fabricante": "LLO-14S-INX", "preco": Decimal("3899.00"), "quantidade_estoque": 6, "categoria": "Cozinha"},
    {"nome": "Depurador de Ar 60cm", "descricao": "Depurador de ar slim 60cm com 3 velocidades e filtro de carvão ativado.", "codigo_fabricante": "DEP-60-BCO", "preco": Decimal("349.90"), "quantidade_estoque": 22, "categoria": "Cozinha"},
    {"nome": "Forno Elétrico 44L", "descricao": "Forno elétrico de bancada 44 litros com convecção, grill e timer.", "codigo_fabricante": "FEL-44L-PT", "preco": Decimal("599.90"), "quantidade_estoque": 15, "categoria": "Cozinha"},
    # Lavanderia
    {"nome": "Máquina de Lavar 11kg", "descricao": "Lavadora automática 11kg com 12 programas de lavagem e cesto inox.", "codigo_fabricante": "LAV-11KG-BR", "preco": Decimal("2199.90"), "quantidade_estoque": 14, "categoria": "Lavanderia"},
    {"nome": "Máquina de Lavar 15kg", "descricao": "Lavadora 15kg com ciclo rápido, lavagem com água quente e dosagem automática.", "codigo_fabricante": "LAV-15KG-INX", "preco": Decimal("3599.00"), "quantidade_estoque": 8, "categoria": "Lavanderia"},
    {"nome": "Lava e Seca 11kg", "descricao": "Lava e seca 11kg de lavagem e 7kg de secagem, motor inverter silencioso.", "codigo_fabricante": "LES-11KG-PT", "preco": Decimal("4299.00"), "quantidade_estoque": 7, "categoria": "Lavanderia"},
    {"nome": "Secadora de Roupas 10kg", "descricao": "Secadora de roupas 10kg por condensação com sensor de secagem e 15 programas.", "codigo_fabricante": "SEC-10KG-BC", "preco": Decimal("3199.00"), "quantidade_estoque": 4, "categoria": "Lavanderia"},
    {"nome": "Tanquinho 10kg", "descricao": "Tanquinho semiautomático 10kg com 4 programas e filtro cata-fiapos.", "codigo_fabricante": "TNQ-10KG-BC", "preco": Decimal("699.90"), "quantidade_estoque": 20, "categoria": "Lavanderia"},
    {"nome": "Ferro de Passar a Vapor", "descricao": "Ferro de passar com base cerâmica, vapor vertical e spray, 1200W.", "codigo_fabricante": "FER-VAP-1200", "preco": Decimal("149.90"), "quantidade_estoque": 50, "categoria": "Lavanderia"},
    # Climatização
    {"nome": "Ar-Condicionado Split 12000 BTUs", "descricao": "Ar-condicionado split hi-wall 12000 BTUs, ciclo frio, função sleep e timer.", "codigo_fabricante": "ARC-12K-QF", "preco": Decimal("2299.00"), "quantidade_estoque": 10, "categoria": "Climatização"},
    {"nome": "Ar-Condicionado Split 9000 BTUs Inverter", "descricao": "Ar-condicionado split inverter 9000 BTUs, quente e frio, classificação A.", "codigo_fabricante": "ARC-9K-INV", "preco": Decimal("2799.00"), "quantidade_estoque": 9, "categoria": "Climatização"},
    {"nome": "Ventilador de Coluna 40cm", "descricao": "Ventilador de coluna 40cm com 3 velocidades, oscilação e inclinação regulável.", "codigo_fabricante": "VEN-COL-40", "preco": Decimal("199.90"), "quantidade_estoque": 35, "categoria": "Climatização"},
    {"nome": "Ventilador de Teto", "descricao": "Ventilador de teto com 3 pás, luminária, controle de parede e 3 velocidades.", "codigo_fabricante": "VEN-TET-3P", "preco": Decimal("299.90"), "quantidade_estoque": 18, "categoria": "Climatização"},
    {"nome": "Aquecedor a Óleo", "descricao": "Aquecedor a óleo com 9 elementos, 3 níveis de potência e termostato ajustável.", "codigo_fabricante": "AQC-OLE-9E", "preco": Decimal("449.90"), "quantidade_estoque": 12, "categoria": "Climatização"},
    {"nome": "Desumidificador de Ar 12L", "descricao": "Desumidificador portátil com capacidade de 12 litros/dia, timer e dreno contínuo.", "codigo_fabricante": "DES-12L-PT", "preco": Decimal("1299.00"), "quantidade_estoque": 6, "categoria": "Climatização"},
    # Áudio e Vídeo
    {"nome": "Smart TV LED 50\" 4K", "descricao": "Smart TV LED 50 polegadas 4K UHD, HDR10, Wi-Fi integrado e 3 HDMI.", "codigo_fabricante": "TV-50-4K-SM", "preco": Decimal("2599.00"), "quantidade_estoque": 11, "categoria": "Áudio e Vídeo"},
    {"nome": "Smart TV LED 32\"", "descricao": "Smart TV LED 32 polegadas HD, Wi-Fi, 2 HDMI e 1 USB.", "codigo_fabricante": "TV-32-HD-SM", "preco": Decimal("1299.00"), "quantidade_estoque": 20, "categoria": "Áudio e Vídeo"},
    {"nome": "Smart TV OLED 55\" 4K", "descricao": "Smart TV OLED 55 polegadas 4K, Dolby Vision e Atmos, 4 HDMI 2.1.", "codigo_fabricante": "TV-55-OLED", "preco": Decimal("6999.00"), "quantidade_estoque": 3, "categoria": "Áudio e Vídeo"},
    {"nome": "Soundbar 2.1 com Subwoofer", "descricao": "Soundbar 2.1 canais com subwoofer sem fio, Bluetooth e 300W RMS.", "codigo_fabricante": "SDB-21-300W", "preco": Decimal("1199.00"), "quantidade_estoque": 14, "categoria": "Áudio e Vídeo"},
    {"nome": "Caixa de Som Bluetooth Portátil", "descricao": "Caixa de som portátil Bluetooth 5.0, à prova d'água IPX7, 20W, 12h de bateria.", "codigo_fabricante": "CXS-BT-20W", "preco": Decimal("349.90"), "quantidade_estoque": 45, "categoria": "Áudio e Vídeo"},
    # Eletrodoméstico (portáteis / outros)
    {"nome": "Aspirador de Pó Robô", "descricao": "Aspirador de pó robô com mapeamento a laser, sucção 2500Pa e controle por app.", "codigo_fabricante": "ASP-ROBO-25", "preco": Decimal("2499.00"), "quantidade_estoque": 8, "categoria": "Eletrodoméstico"},
    {"nome": "Aspirador de Pó Vertical", "descricao": "Aspirador de pó vertical sem fio, bateria de lítio, 45 min de autonomia.", "codigo_fabricante": "ASP-VER-45M", "preco": Decimal("899.90"), "quantidade_estoque": 16, "categoria": "Eletrodoméstico"},
    {"nome": "Cafeteira Expresso", "descricao": "Cafeteira expresso automática com moedor integrado, 15 bar de pressão.", "codigo_fabricante": "CAF-EXP-15B", "preco": Decimal("1899.00"), "quantidade_estoque": 10, "categoria": "Eletrodoméstico"},
    {"nome": "Liquidificador 1200W", "descricao": "Liquidificador com motor de 1200W, 12 velocidades e copo de tritan 3L.", "codigo_fabricante": "LIQ-1200-3L", "preco": Decimal("249.90"), "quantidade_estoque": 38, "categoria": "Eletrodoméstico"},
    {"nome": "Batedeira Planetária 600W", "descricao": "Batedeira planetária 600W com 3 batedores, tigela inox de 5L e 12 velocidades.", "codigo_fabricante": "BAT-PLA-600", "preco": Decimal("599.90"), "quantidade_estoque": 13, "categoria": "Eletrodoméstico"},
    {"nome": "Air Fryer 5.5L", "descricao": "Fritadeira elétrica sem óleo 5.5 litros com timer, temperatura ajustável até 200°C.", "codigo_fabricante": "AFR-55L-PT", "preco": Decimal("499.90"), "quantidade_estoque": 28, "categoria": "Eletrodoméstico"},
    {"nome": "Panela de Pressão Elétrica 6L", "descricao": "Panela de pressão elétrica 6 litros com 14 funções pré-programadas e timer.", "codigo_fabricante": "PPE-6L-INX", "preco": Decimal("399.90"), "quantidade_estoque": 19, "categoria": "Eletrodoméstico"},
    # Eletrônico
    {"nome": "Notebook 15.6\" Core i5", "descricao": "Notebook 15.6 polegadas, Intel Core i5, 8GB RAM, SSD 256GB, Windows 11.", "codigo_fabricante": "NTB-15-I5-8", "preco": Decimal("3499.00"), "quantidade_estoque": 7, "categoria": "Eletrônico"},
    {"nome": "Tablet 10\" 64GB", "descricao": "Tablet 10 polegadas, 64GB armazenamento, 4GB RAM, Wi-Fi e câmera 8MP.", "codigo_fabricante": "TAB-10-64G", "preco": Decimal("1599.00"), "quantidade_estoque": 15, "categoria": "Eletrônico"},
    {"nome": "Impressora Multifuncional Wi-Fi", "descricao": "Impressora multifuncional jato de tinta, Wi-Fi, imprime, copia e digitaliza.", "codigo_fabricante": "IMP-MF-WIFI", "preco": Decimal("599.90"), "quantidade_estoque": 20, "categoria": "Eletrônico"},
    # Sem categoria (demonstrar nullable)
    {"nome": "Purificador de Água", "descricao": "Purificador de água com 3 estágios de filtragem, água natural e gelada.", "codigo_fabricante": "PUR-3E-BCO", "preco": Decimal("899.00"), "quantidade_estoque": 17, "categoria": None},
    {"nome": "Umidificador de Ar 3L", "descricao": "Umidificador ultrassônico 3 litros, operação silenciosa, até 12h de autonomia.", "codigo_fabricante": "UMD-3L-BC", "preco": Decimal("179.90"), "quantidade_estoque": 25, "categoria": None},
    {"nome": "Espremedor de Frutas Elétrico", "descricao": "Espremedor de frutas elétrico com jarra de 1L, dupla rotação e cone universal.", "codigo_fabricante": "ESP-FRT-1L", "preco": Decimal("89.90"), "quantidade_estoque": 33, "categoria": None},
    {"nome": "Grill Elétrico 2000W", "descricao": "Grill elétrico 2000W com placas antiaderentes removíveis e coletor de gordura.", "codigo_fabricante": "GRL-2000-PT", "preco": Decimal("299.90"), "quantidade_estoque": 21, "categoria": None},
]


def run():
    Produto.objects.all().delete()
    Categoria.objects.all().delete()
    print("Produtos e categorias existentes removidos.")

    categorias = {}
    for nome in CATEGORIAS:
        categorias[nome] = Categoria.objects.create(nome=nome)
    print(f"Criadas {len(categorias)} categorias.")

    created = 0
    for dados in PRODUTOS:
        cat_nome = dados.pop("categoria")
        dados["categoria"] = categorias[cat_nome] if cat_nome else None
        dados["url_imagem"] = f"https://placehold.co/400x400?text={dados['codigo_fabricante']}"
        Produto.objects.create(**dados)
        created += 1

    print(f"Criados {created} produtos. Total: {Produto.objects.count()}")


run()
