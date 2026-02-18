"""
Seed script para criar categorias e 90 produtos.
Uso: uv run python manage.py shell < seeds/0020_seed_produtos.py
"""

import random
from decimal import Decimal

from casas_floripa.models import Categoria, Produto

CATEGORIAS = [
    "Eletrodoméstico",
    "Eletrônico",
    "Cozinha",
    "Lavanderia",
    "Climatização",
    "Áudio e Vídeo",
    "Geek e Nerd",
]

PRODUTOS = [
    # Cozinha
    {
        "nome": "Geladeira Frost Free 375L",
        "descricao": "Geladeira duplex frost free com 375 litros, painel eletrônico e gaveta de frutas e verduras.",
        "codigo_fabricante": "GEL-FF375-BR",
        "preco": Decimal("3299.90"),
        "quantidade_estoque": 12,
        "categoria": "Cozinha",
    },
    {
        "nome": "Geladeira Inverse 460L",
        "descricao": "Geladeira inverse com freezer na parte inferior, 460 litros, tecnologia no frost.",
        "codigo_fabricante": "GEL-INV460-SS",
        "preco": Decimal("5499.00"),
        "quantidade_estoque": 5,
        "categoria": "Cozinha",
    },
    {
        "nome": "Fogão 5 Bocas Inox",
        "descricao": "Fogão 5 bocas com acendimento automático, forno com grill e timer digital.",
        "codigo_fabricante": "FOG-5B-INOX",
        "preco": Decimal("1899.90"),
        "quantidade_estoque": 18,
        "categoria": "Cozinha",
    },
    {
        "nome": "Fogão 4 Bocas Branco",
        "descricao": "Fogão 4 bocas com acendimento automático, tampa de vidro e forno autolimpante.",
        "codigo_fabricante": "FOG-4B-BCO",
        "preco": Decimal("1099.00"),
        "quantidade_estoque": 25,
        "categoria": "Cozinha",
    },
    {
        "nome": "Micro-ondas 32L",
        "descricao": "Micro-ondas 32 litros com função tira odor, receitas pré-programadas e painel digital.",
        "codigo_fabricante": "MCO-32L-PT",
        "preco": Decimal("699.90"),
        "quantidade_estoque": 30,
        "categoria": "Cozinha",
    },
    {
        "nome": "Micro-ondas 20L",
        "descricao": "Micro-ondas compacto 20 litros, ideal para esquentar e descongelar alimentos.",
        "codigo_fabricante": "MCO-20L-BC",
        "preco": Decimal("449.90"),
        "quantidade_estoque": 40,
        "categoria": "Cozinha",
    },
    {
        "nome": "Lava-louças 14 Serviços",
        "descricao": "Lava-louças para 14 serviços com 6 programas de lavagem e meia carga.",
        "codigo_fabricante": "LLO-14S-INX",
        "preco": Decimal("3899.00"),
        "quantidade_estoque": 6,
        "categoria": "Cozinha",
    },
    {
        "nome": "Depurador de Ar 60cm",
        "descricao": "Depurador de ar slim 60cm com 3 velocidades e filtro de carvão ativado.",
        "codigo_fabricante": "DEP-60-BCO",
        "preco": Decimal("349.90"),
        "quantidade_estoque": 22,
        "categoria": "Cozinha",
    },
    {
        "nome": "Forno Elétrico 44L",
        "descricao": "Forno elétrico de bancada 44 litros com convecção, grill e timer.",
        "codigo_fabricante": "FEL-44L-PT",
        "preco": Decimal("599.90"),
        "quantidade_estoque": 15,
        "categoria": "Cozinha",
    },
    # Lavanderia
    {
        "nome": "Máquina de Lavar 11kg",
        "descricao": "Lavadora automática 11kg com 12 programas de lavagem e cesto inox.",
        "codigo_fabricante": "LAV-11KG-BR",
        "preco": Decimal("2199.90"),
        "quantidade_estoque": 14,
        "categoria": "Lavanderia",
    },
    {
        "nome": "Máquina de Lavar 15kg",
        "descricao": "Lavadora 15kg com ciclo rápido, lavagem com água quente e dosagem automática.",
        "codigo_fabricante": "LAV-15KG-INX",
        "preco": Decimal("3599.00"),
        "quantidade_estoque": 8,
        "categoria": "Lavanderia",
    },
    {
        "nome": "Lava e Seca 11kg",
        "descricao": "Lava e seca 11kg de lavagem e 7kg de secagem, motor inverter silencioso.",
        "codigo_fabricante": "LES-11KG-PT",
        "preco": Decimal("4299.00"),
        "quantidade_estoque": 7,
        "categoria": "Lavanderia",
    },
    {
        "nome": "Secadora de Roupas 10kg",
        "descricao": "Secadora de roupas 10kg por condensação com sensor de secagem e 15 programas.",
        "codigo_fabricante": "SEC-10KG-BC",
        "preco": Decimal("3199.00"),
        "quantidade_estoque": 4,
        "categoria": "Lavanderia",
    },
    {
        "nome": "Tanquinho 10kg",
        "descricao": "Tanquinho semiautomático 10kg com 4 programas e filtro cata-fiapos.",
        "codigo_fabricante": "TNQ-10KG-BC",
        "preco": Decimal("699.90"),
        "quantidade_estoque": 20,
        "categoria": "Lavanderia",
    },
    {
        "nome": "Ferro de Passar a Vapor",
        "descricao": "Ferro de passar com base cerâmica, vapor vertical e spray, 1200W.",
        "codigo_fabricante": "FER-VAP-1200",
        "preco": Decimal("149.90"),
        "quantidade_estoque": 50,
        "categoria": "Lavanderia",
    },
    # Climatização
    {
        "nome": "Ar-Condicionado Split 12000 BTUs",
        "descricao": "Ar-condicionado split hi-wall 12000 BTUs, ciclo frio, função sleep e timer.",
        "codigo_fabricante": "ARC-12K-QF",
        "preco": Decimal("2299.00"),
        "quantidade_estoque": 10,
        "categoria": "Climatização",
    },
    {
        "nome": "Ar-Condicionado Split 9000 BTUs Inverter",
        "descricao": "Ar-condicionado split inverter 9000 BTUs, quente e frio, classificação A.",
        "codigo_fabricante": "ARC-9K-INV",
        "preco": Decimal("2799.00"),
        "quantidade_estoque": 9,
        "categoria": "Climatização",
    },
    {
        "nome": "Ventilador de Coluna 40cm",
        "descricao": "Ventilador de coluna 40cm com 3 velocidades, oscilação e inclinação regulável.",
        "codigo_fabricante": "VEN-COL-40",
        "preco": Decimal("199.90"),
        "quantidade_estoque": 35,
        "categoria": "Climatização",
    },
    {
        "nome": "Ventilador de Teto",
        "descricao": "Ventilador de teto com 3 pás, luminária, controle de parede e 3 velocidades.",
        "codigo_fabricante": "VEN-TET-3P",
        "preco": Decimal("299.90"),
        "quantidade_estoque": 18,
        "categoria": "Climatização",
    },
    {
        "nome": "Aquecedor a Óleo",
        "descricao": "Aquecedor a óleo com 9 elementos, 3 níveis de potência e termostato ajustável.",
        "codigo_fabricante": "AQC-OLE-9E",
        "preco": Decimal("449.90"),
        "quantidade_estoque": 12,
        "categoria": "Climatização",
    },
    {
        "nome": "Desumidificador de Ar 12L",
        "descricao": "Desumidificador portátil com capacidade de 12 litros/dia, timer e dreno contínuo.",
        "codigo_fabricante": "DES-12L-PT",
        "preco": Decimal("1299.00"),
        "quantidade_estoque": 6,
        "categoria": "Climatização",
    },
    # Áudio e Vídeo
    {
        "nome": 'Smart TV LED 50" 4K',
        "descricao": "Smart TV LED 50 polegadas 4K UHD, HDR10, Wi-Fi integrado e 3 HDMI.",
        "codigo_fabricante": "TV-50-4K-SM",
        "preco": Decimal("2599.00"),
        "quantidade_estoque": 11,
        "categoria": "Áudio e Vídeo",
    },
    {
        "nome": 'Smart TV LED 32"',
        "descricao": "Smart TV LED 32 polegadas HD, Wi-Fi, 2 HDMI e 1 USB.",
        "codigo_fabricante": "TV-32-HD-SM",
        "preco": Decimal("1299.00"),
        "quantidade_estoque": 20,
        "categoria": "Áudio e Vídeo",
    },
    {
        "nome": 'Smart TV OLED 55" 4K',
        "descricao": "Smart TV OLED 55 polegadas 4K, Dolby Vision e Atmos, 4 HDMI 2.1.",
        "codigo_fabricante": "TV-55-OLED",
        "preco": Decimal("6999.00"),
        "quantidade_estoque": 3,
        "categoria": "Áudio e Vídeo",
    },
    {
        "nome": "Soundbar 2.1 com Subwoofer",
        "descricao": "Soundbar 2.1 canais com subwoofer sem fio, Bluetooth e 300W RMS.",
        "codigo_fabricante": "SDB-21-300W",
        "preco": Decimal("1199.00"),
        "quantidade_estoque": 14,
        "categoria": "Áudio e Vídeo",
    },
    {
        "nome": "Caixa de Som Bluetooth Portátil",
        "descricao": "Caixa de som portátil Bluetooth 5.0, à prova d'água IPX7, 20W, 12h de bateria.",
        "codigo_fabricante": "CXS-BT-20W",
        "preco": Decimal("349.90"),
        "quantidade_estoque": 45,
        "categoria": "Áudio e Vídeo",
    },
    # Eletrodoméstico (portáteis / outros)
    {
        "nome": "Aspirador de Pó Robô",
        "descricao": "Aspirador de pó robô com mapeamento a laser, sucção 2500Pa e controle por app.",
        "codigo_fabricante": "ASP-ROBO-25",
        "preco": Decimal("2499.00"),
        "quantidade_estoque": 8,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Aspirador de Pó Vertical",
        "descricao": "Aspirador de pó vertical sem fio, bateria de lítio, 45 min de autonomia.",
        "codigo_fabricante": "ASP-VER-45M",
        "preco": Decimal("899.90"),
        "quantidade_estoque": 16,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Cafeteira Expresso",
        "descricao": "Cafeteira expresso automática com moedor integrado, 15 bar de pressão.",
        "codigo_fabricante": "CAF-EXP-15B",
        "preco": Decimal("1899.00"),
        "quantidade_estoque": 10,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Liquidificador 1200W",
        "descricao": "Liquidificador com motor de 1200W, 12 velocidades e copo de tritan 3L.",
        "codigo_fabricante": "LIQ-1200-3L",
        "preco": Decimal("249.90"),
        "quantidade_estoque": 38,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Batedeira Planetária 600W",
        "descricao": "Batedeira planetária 600W com 3 batedores, tigela inox de 5L e 12 velocidades.",
        "codigo_fabricante": "BAT-PLA-600",
        "preco": Decimal("599.90"),
        "quantidade_estoque": 13,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Air Fryer 5.5L",
        "descricao": "Fritadeira elétrica sem óleo 5.5 litros com timer, temperatura ajustável até 200°C.",
        "codigo_fabricante": "AFR-55L-PT",
        "preco": Decimal("499.90"),
        "quantidade_estoque": 28,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Panela de Pressão Elétrica 6L",
        "descricao": "Panela de pressão elétrica 6 litros com 14 funções pré-programadas e timer.",
        "codigo_fabricante": "PPE-6L-INX",
        "preco": Decimal("399.90"),
        "quantidade_estoque": 19,
        "categoria": "Eletrodoméstico",
    },
    # Eletrônico
    {
        "nome": 'Notebook 15.6" Core i5',
        "descricao": "Notebook 15.6 polegadas, Intel Core i5, 8GB RAM, SSD 256GB, Windows 11.",
        "codigo_fabricante": "NTB-15-I5-8",
        "preco": Decimal("3499.00"),
        "quantidade_estoque": 7,
        "categoria": "Eletrônico",
    },
    {
        "nome": 'Tablet 10" 64GB',
        "descricao": "Tablet 10 polegadas, 64GB armazenamento, 4GB RAM, Wi-Fi e câmera 8MP.",
        "codigo_fabricante": "TAB-10-64G",
        "preco": Decimal("1599.00"),
        "quantidade_estoque": 15,
        "categoria": "Eletrônico",
    },
    {
        "nome": "Impressora Multifuncional Wi-Fi",
        "descricao": "Impressora multifuncional jato de tinta, Wi-Fi, imprime, copia e digitaliza.",
        "codigo_fabricante": "IMP-MF-WIFI",
        "preco": Decimal("599.90"),
        "quantidade_estoque": 20,
        "categoria": "Eletrônico",
    },
    # Sem categoria (demonstrar nullable)
    {
        "nome": "Purificador de Água",
        "descricao": "Purificador de água com 3 estágios de filtragem, água natural e gelada.",
        "codigo_fabricante": "PUR-3E-BCO",
        "preco": Decimal("899.00"),
        "quantidade_estoque": 17,
        "categoria": None,
    },
    {
        "nome": "Umidificador de Ar 3L",
        "descricao": "Umidificador ultrassônico 3 litros, operação silenciosa, até 12h de autonomia.",
        "codigo_fabricante": "UMD-3L-BC",
        "preco": Decimal("179.90"),
        "quantidade_estoque": 25,
        "categoria": None,
    },
    {
        "nome": "Espremedor de Frutas Elétrico",
        "descricao": "Espremedor de frutas elétrico com jarra de 1L, dupla rotação e cone universal.",
        "codigo_fabricante": "ESP-FRT-1L",
        "preco": Decimal("89.90"),
        "quantidade_estoque": 33,
        "categoria": None,
    },
    {
        "nome": "Grill Elétrico 2000W",
        "descricao": "Grill elétrico 2000W com placas antiaderentes removíveis e coletor de gordura.",
        "codigo_fabricante": "GRL-2000-PT",
        "preco": Decimal("299.90"),
        "quantidade_estoque": 21,
        "categoria": None,
    },
    # Geek e Nerd
    {
        "nome": "Console PlayStation 5",
        "descricao": "Console PlayStation 5 com leitor de disco, controle DualSense, SSD 825GB.",
        "codigo_fabricante": "GK-PS5-DSC",
        "preco": Decimal("4499.00"),
        "quantidade_estoque": 6,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Console Xbox Series X",
        "descricao": "Console Xbox Series X 1TB, 4K a 120fps, retrocompatível com milhares de jogos.",
        "codigo_fabricante": "GK-XBSX-1TB",
        "preco": Decimal("4299.00"),
        "quantidade_estoque": 5,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Console Nintendo Switch OLED",
        "descricao": "Nintendo Switch modelo OLED com tela de 7 polegadas, dock e Joy-Con.",
        "codigo_fabricante": "GK-NSW-OLED",
        "preco": Decimal("2499.00"),
        "quantidade_estoque": 10,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Headset Gamer 7.1 Surround",
        "descricao": "Headset gamer com som surround 7.1 virtual, microfone retrátil, RGB e almofadas memory foam.",
        "codigo_fabricante": "GK-HSG-71S",
        "preco": Decimal("399.90"),
        "quantidade_estoque": 25,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Teclado Mecânico RGB",
        "descricao": "Teclado mecânico gamer com switches blue, iluminação RGB por tecla, layout ABNT2.",
        "codigo_fabricante": "GK-TEC-MRGB",
        "preco": Decimal("349.90"),
        "quantidade_estoque": 30,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Mouse Gamer 16000 DPI",
        "descricao": "Mouse gamer óptico com sensor de 16000 DPI, 8 botões programáveis e peso ajustável.",
        "codigo_fabricante": "GK-MOU-16K",
        "preco": Decimal("249.90"),
        "quantidade_estoque": 35,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Mousepad Gamer XL 90x40cm",
        "descricao": "Mousepad gamer extra grande 90x40cm com base antiderrapante e borda costurada.",
        "codigo_fabricante": "GK-MPD-XL90",
        "preco": Decimal("89.90"),
        "quantidade_estoque": 50,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": 'Monitor Gamer 27" 165Hz',
        "descricao": "Monitor gamer 27 polegadas IPS, 165Hz, 1ms, QHD 2560x1440, FreeSync e G-Sync.",
        "codigo_fabricante": "GK-MON-27QH",
        "preco": Decimal("2299.00"),
        "quantidade_estoque": 8,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": 'Monitor Gamer 24" 144Hz',
        "descricao": "Monitor gamer 24 polegadas Full HD, 144Hz, 1ms, painel VA, entrada HDMI e DisplayPort.",
        "codigo_fabricante": "GK-MON-24FH",
        "preco": Decimal("1199.00"),
        "quantidade_estoque": 14,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Cadeira Gamer Reclinável",
        "descricao": "Cadeira gamer com encosto reclinável até 180°, apoio de braço 4D, almofadas lombar e cervical.",
        "codigo_fabricante": "GK-CDR-180R",
        "preco": Decimal("1599.00"),
        "quantidade_estoque": 9,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Webcam Full HD 1080p",
        "descricao": "Webcam Full HD 1080p com microfone duplo, autofoco e correção de luz.",
        "codigo_fabricante": "GK-WCM-1080",
        "preco": Decimal("299.90"),
        "quantidade_estoque": 20,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Placa de Captura HDMI 4K",
        "descricao": "Placa de captura externa HDMI 4K para streaming, USB 3.0, compatível com OBS.",
        "codigo_fabricante": "GK-CAP-4K",
        "preco": Decimal("899.90"),
        "quantidade_estoque": 7,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Ring Light 26cm com Tripé",
        "descricao": "Ring light LED 26cm com tripé ajustável de 2m, 3 modos de luz e suporte para celular.",
        "codigo_fabricante": "GK-RGL-26CM",
        "preco": Decimal("129.90"),
        "quantidade_estoque": 22,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Controle Pro para Switch",
        "descricao": "Controle Pro sem fio para Nintendo Switch com NFC, giroscópio e bateria de 40h.",
        "codigo_fabricante": "GK-CTR-SWPR",
        "preco": Decimal("349.90"),
        "quantidade_estoque": 15,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Volante com Pedais Force Feedback",
        "descricao": "Volante gamer com force feedback, pedais e câmbio, compatível com PC, PS5 e Xbox.",
        "codigo_fabricante": "GK-VOL-FFB",
        "preco": Decimal("1899.00"),
        "quantidade_estoque": 4,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Deck de Streaming 15 Teclas",
        "descricao": "Stream deck com 15 teclas LCD customizáveis para controle de lives e automação.",
        "codigo_fabricante": "GK-SDK-15T",
        "preco": Decimal("999.90"),
        "quantidade_estoque": 11,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Microfone Condensador USB",
        "descricao": "Microfone condensador USB cardioide para podcast e streaming, com botão de mute e ganho.",
        "codigo_fabricante": "GK-MIC-CUSB",
        "preco": Decimal("499.90"),
        "quantidade_estoque": 18,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Luminária de Mesa LED Darth Vader",
        "descricao": "Luminária de mesa temática Star Wars Darth Vader, LED com 3 intensidades, USB.",
        "codigo_fabricante": "GK-LUM-DVDR",
        "preco": Decimal("189.90"),
        "quantidade_estoque": 13,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Caneca Térmica Gamer 450ml",
        "descricao": "Caneca térmica gamer 450ml em aço inox com tampa deslizante e estampa pixel art.",
        "codigo_fabricante": "GK-CNC-450G",
        "preco": Decimal("69.90"),
        "quantidade_estoque": 60,
        "categoria": "Geek e Nerd",
    },
    # Mais Cozinha
    {
        "nome": "Cooktop Indução 4 Bocas",
        "descricao": "Cooktop por indução 4 zonas com painel touch, timer individual e trava de segurança.",
        "codigo_fabricante": "CKT-IND-4B",
        "preco": Decimal("2899.00"),
        "quantidade_estoque": 7,
        "categoria": "Cozinha",
    },
    {
        "nome": "Adega Climatizada 12 Garrafas",
        "descricao": "Adega climatizada para 12 garrafas com controle digital de temperatura e luz interna LED.",
        "codigo_fabricante": "ADG-12G-PT",
        "preco": Decimal("1099.00"),
        "quantidade_estoque": 9,
        "categoria": "Cozinha",
    },
    {
        "nome": "Freezer Vertical 246L",
        "descricao": "Freezer vertical 246 litros com degelo automático e 7 gavetas transparentes.",
        "codigo_fabricante": "FRZ-VER-246",
        "preco": Decimal("2899.90"),
        "quantidade_estoque": 5,
        "categoria": "Cozinha",
    },
    {
        "nome": "Coifa de Parede 90cm",
        "descricao": "Coifa de parede 90cm em inox com 3 velocidades, filtro de alumínio lavável e iluminação.",
        "codigo_fabricante": "COI-PAR-90I",
        "preco": Decimal("1799.00"),
        "quantidade_estoque": 6,
        "categoria": "Cozinha",
    },
    {
        "nome": "Processador de Alimentos 800W",
        "descricao": "Processador de alimentos 800W com 3 discos, lâmina inox e copo de 3.1L.",
        "codigo_fabricante": "PRC-ALM-800",
        "preco": Decimal("399.90"),
        "quantidade_estoque": 17,
        "categoria": "Cozinha",
    },
    # Mais Eletrônico
    {
        "nome": 'Notebook Gamer 15.6" RTX 4060',
        "descricao": 'Notebook gamer 15.6", Intel Core i7, 16GB RAM, SSD 512GB, RTX 4060, tela 144Hz.',
        "codigo_fabricante": "NTB-GM-4060",
        "preco": Decimal("7499.00"),
        "quantidade_estoque": 4,
        "categoria": "Eletrônico",
    },
    {
        "nome": 'Monitor Ultrawide 34" Curvo',
        "descricao": "Monitor ultrawide 34 polegadas curvo, UWQHD 3440x1440, 100Hz, USB-C com PD 65W.",
        "codigo_fabricante": "MON-UW34-CV",
        "preco": Decimal("3299.00"),
        "quantidade_estoque": 5,
        "categoria": "Eletrônico",
    },
    {
        "nome": "Roteador Wi-Fi 6 Mesh",
        "descricao": "Sistema mesh Wi-Fi 6 com 2 unidades, cobertura de até 350m², 5400Mbps.",
        "codigo_fabricante": "ROT-WF6-MSH",
        "preco": Decimal("1299.00"),
        "quantidade_estoque": 12,
        "categoria": "Eletrônico",
    },
    {
        "nome": "HD Externo 2TB USB 3.0",
        "descricao": "HD externo portátil 2TB USB 3.0 com backup automático e proteção por senha.",
        "codigo_fabricante": "HDE-2TB-U30",
        "preco": Decimal("449.90"),
        "quantidade_estoque": 22,
        "categoria": "Eletrônico",
    },
    {
        "nome": "SSD Externo 1TB NVMe",
        "descricao": "SSD externo 1TB NVMe com velocidade de leitura de 1050MB/s, USB-C, compacto.",
        "codigo_fabricante": "SSD-EXT-1TB",
        "preco": Decimal("699.90"),
        "quantidade_estoque": 15,
        "categoria": "Eletrônico",
    },
    {
        "nome": "Smartwatch com GPS",
        "descricao": "Smartwatch com GPS integrado, monitor cardíaco, SpO2, tela AMOLED e 7 dias de bateria.",
        "codigo_fabricante": "SWT-GPS-AMO",
        "preco": Decimal("1199.00"),
        "quantidade_estoque": 18,
        "categoria": "Eletrônico",
    },
    # Mais Eletrodoméstico
    {
        "nome": "Robô Aspirador e Passa Pano",
        "descricao": "Robô aspirador e passa pano 2 em 1, navegação inteligente, base autoesvaziante.",
        "codigo_fabricante": "ASP-ROBO-PP",
        "preco": Decimal("3499.00"),
        "quantidade_estoque": 5,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Vaporizador de Roupas Portátil",
        "descricao": "Vaporizador de roupas portátil 1500W, aquece em 25s, reservatório de 300ml.",
        "codigo_fabricante": "VAP-ROP-15W",
        "preco": Decimal("199.90"),
        "quantidade_estoque": 24,
        "categoria": "Eletrodoméstico",
    },
    {
        "nome": "Máquina de Gelo 15kg/dia",
        "descricao": "Máquina de gelo portátil com produção de 15kg/dia, 2 tamanhos de gelo, inox.",
        "codigo_fabricante": "MGE-15K-INX",
        "preco": Decimal("1499.00"),
        "quantidade_estoque": 8,
        "categoria": "Eletrodoméstico",
    },
    # Mais Áudio e Vídeo
    {
        "nome": "Projetor Full HD 6000 Lumens",
        "descricao": "Projetor Full HD nativo, 6000 lumens, contraste 10000:1, HDMI, tela até 300 polegadas.",
        "codigo_fabricante": "PRJ-FHD-6KL",
        "preco": Decimal("3199.00"),
        "quantidade_estoque": 4,
        "categoria": "Áudio e Vídeo",
    },
    {
        "nome": "Fone de Ouvido Bluetooth ANC",
        "descricao": "Fone de ouvido over-ear Bluetooth 5.3 com cancelamento ativo de ruído, 30h de bateria.",
        "codigo_fabricante": "FON-BT-ANC",
        "preco": Decimal("599.90"),
        "quantidade_estoque": 22,
        "categoria": "Áudio e Vídeo",
    },
    {
        "nome": "Receiver AV 5.1 Canais",
        "descricao": "Receiver AV 5.1 canais com 100W por canal, Bluetooth, HDMI ARC e Dolby Digital.",
        "codigo_fabricante": "RCV-51-100W",
        "preco": Decimal("2499.00"),
        "quantidade_estoque": 3,
        "categoria": "Áudio e Vídeo",
    },
    {
        "nome": "Toca-Discos de Vinil Retrô",
        "descricao": "Toca-discos de vinil com design retrô, caixas de som embutidas, Bluetooth e saída RCA.",
        "codigo_fabricante": "TDV-RETRO-BT",
        "preco": Decimal("699.90"),
        "quantidade_estoque": 10,
        "categoria": "Áudio e Vídeo",
    },
    # Mais Climatização
    {
        "nome": "Ar-Condicionado Portátil 12000 BTUs",
        "descricao": "Ar-condicionado portátil 12000 BTUs, sem instalação, controle remoto e timer.",
        "codigo_fabricante": "ARC-PORT-12K",
        "preco": Decimal("2999.00"),
        "quantidade_estoque": 6,
        "categoria": "Climatização",
    },
    {
        "nome": "Climatizador Evaporativo 7L",
        "descricao": "Climatizador evaporativo 7 litros com 3 velocidades, função umidificar e ionizar.",
        "codigo_fabricante": "CLM-EVP-7L",
        "preco": Decimal("549.90"),
        "quantidade_estoque": 14,
        "categoria": "Climatização",
    },
    # Mais Lavanderia
    {
        "nome": "Máquina de Lavar 17kg",
        "descricao": "Lavadora 17kg com cesto inox, dosagem inteligente de sabão e 16 programas.",
        "codigo_fabricante": "LAV-17KG-TI",
        "preco": Decimal("4599.00"),
        "quantidade_estoque": 4,
        "categoria": "Lavanderia",
    },
    {
        "nome": "Passadeira a Vapor Vertical",
        "descricao": "Passadeira a vapor vertical 1800W com cabide dobrável e reservatório de 1.6L.",
        "codigo_fabricante": "PAS-VAP-18V",
        "preco": Decimal("449.90"),
        "quantidade_estoque": 11,
        "categoria": "Lavanderia",
    },
    # Sem categoria
    {
        "nome": "Balança Digital de Cozinha 10kg",
        "descricao": "Balança digital de cozinha com capacidade de 10kg, display LCD e tara automática.",
        "codigo_fabricante": "BAL-DIG-10K",
        "preco": Decimal("59.90"),
        "quantidade_estoque": 40,
        "categoria": None,
    },
    {
        "nome": "Seladora a Vácuo Doméstica",
        "descricao": "Seladora a vácuo para conservação de alimentos, compatível com rolos e sacos avulsos.",
        "codigo_fabricante": "SEL-VAC-DOM",
        "preco": Decimal("299.90"),
        "quantidade_estoque": 15,
        "categoria": None,
    },
    {
        "nome": "Afiador Elétrico de Facas",
        "descricao": "Afiador elétrico de facas com 2 estágios, guia angular e base antiderrapante.",
        "codigo_fabricante": "AFI-ELE-2E",
        "preco": Decimal("129.90"),
        "quantidade_estoque": 18,
        "categoria": None,
    },
    # Mais Geek e Nerd
    {
        "nome": "Controle Arcade Fightstick",
        "descricao": "Controle arcade fightstick com botões Sanwa, compatível com PC e consoles, cabo de 3m.",
        "codigo_fabricante": "GK-ARC-FSK",
        "preco": Decimal("799.90"),
        "quantidade_estoque": 6,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Mini PC Gamer Ryzen 7",
        "descricao": "Mini PC gamer AMD Ryzen 7, 16GB RAM, SSD 512GB, Radeon integrada, Wi-Fi 6E.",
        "codigo_fabricante": "GK-MPC-RZ7",
        "preco": Decimal("4299.00"),
        "quantidade_estoque": 5,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Base Cooler para Notebook RGB",
        "descricao": 'Base cooler para notebook até 17" com 5 ventoinhas, iluminação RGB e altura ajustável.',
        "codigo_fabricante": "GK-BCN-RGB",
        "preco": Decimal("159.90"),
        "quantidade_estoque": 28,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Hub USB-C 9 em 1",
        "descricao": "Hub USB-C 9 em 1 com HDMI 4K, 3x USB 3.0, leitor SD/microSD, Ethernet e PD 100W.",
        "codigo_fabricante": "GK-HUB-9E1",
        "preco": Decimal("279.90"),
        "quantidade_estoque": 19,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Óculos de Realidade Virtual",
        "descricao": "Headset de realidade virtual standalone com tela 4K, tracking 6DoF e 128GB.",
        "codigo_fabricante": "GK-VR-4K128",
        "preco": Decimal("3499.00"),
        "quantidade_estoque": 3,
        "categoria": "Geek e Nerd",
    },
    {
        "nome": "Drone com Câmera 4K",
        "descricao": "Drone com câmera 4K estabilizada em 3 eixos, alcance de 10km, 30min de voo e GPS.",
        "codigo_fabricante": "GK-DRN-4KGP",
        "preco": Decimal("5999.00"),
        "quantidade_estoque": 2,
        "categoria": "Geek e Nerd",
    },
]


def run():
    categorias = {}
    cat_created = 0
    for nome in CATEGORIAS:
        cat, created = Categoria.objects.get_or_create(nome=nome)
        categorias[nome] = cat
        if created:
            cat_created += 1
    print(
        f"Categorias: {cat_created} criadas, {len(CATEGORIAS) - cat_created} já existiam."
    )

    prod_created = 0
    prod_existing = 0
    for dados in PRODUTOS:
        cat_nome = dados.pop("categoria")
        dados["categoria"] = categorias[cat_nome] if cat_nome else None
        dados["url_imagem"] = (
            f"https://placehold.co/400x400?text={dados['codigo_fabricante']}"
        )
        _, created = Produto.objects.get_or_create(
            codigo_fabricante=dados.pop("codigo_fabricante"),
            defaults=dados,
        )
        if created:
            prod_created += 1
        else:
            prod_existing += 1

    print(
        f"Produtos: {prod_created} criados, {prod_existing} já existiam. Total: {Produto.objects.count()}"
    )

    # Fake vector embedding (gibberish para aumentar volume da tabela; útil para demo de .only())
    random.seed(42)
    fake_vector = (
        "[" + ",".join(str(round(random.uniform(-1, 1), 6)) for _ in range(1536)) + "]"
    )
    n = Produto.objects.all().update(vector_embedding=fake_vector)
    print(f"Vector embedding (fake) atualizado em {n} produtos.")


run()
