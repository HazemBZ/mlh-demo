
ANNOUNCE_TEMPLATE = {
    "_csrf-frontend": "wHkILzO4ZLWYcgmAg_XBDslBoEunHBOk_W2UnsVd9hCHAEMCC_k94qwGaK22vqBqjRDsCcVwZsKkLP_brweRTw==",
    "count": "1",
    "uploadedfiles": '["50021671392639.jpg"]',
    "removefiles": "",
    "previousurl": "https://www.cava.tn/",
    "productId": "",
    "Products[category]": "2",  # {2: Immobilier} (alaways immobilier)
    "Products[subCategory]": "52",  # {55: Appartements, 56: Maisons et Villas}
    "Products[attributes][16]": "10820", # {10820: Meublé, 10821: Non Meublé}
    "Products[attributes][17]": "1000", # Surface en m^2
    "range_values": ["10;999999", "1;10", "1;5"],
    "Products[attributes][21]": "3", # Nombre de pieces
    "Products[attributes][22]": "1", # Nombre de selles de bains
    "Products[attributes][40]": "10933", # Type transaction {10933: A Vendre, 10934: A Louer}
    "Products[name]": "Vente",  # Titre annonce
    "Products[description]": "<p>Vente+appartement</p>",  # Description annonce
    "Products[price]": "200000000",  # Prix
    "Products[currency]": "TND-TND",
    "Products[product_phone]": "123456789",
    "Products[whatsapp]": "",
    "prod_location": "1", # {1: En Tunisie, 2: A l'etrangé}
    "Products[state]": "2",
    "under_state": "38",  # Villes
    "Products[stateid]": "38",  # Regions
    "Products[parentstateid]": "2",
    "abroadLocation": "",
    "Products[productCondition]": "",
    "Products[exchangeToBuy]": "0",
    "Products[delivery]": "0",
    "Products[videoUrl]": "",
    "Products[promotion][type]": "",
    "Products[promotion][addtype]": "",
    "Products[uploadSessionId]": "",
}


ANNOUNCE_TEMPLATE_ORIGINAL = {
    "_csrf-frontend": "wHkILzO4ZLWYcgmAg_XBDslBoEunHBOk_W2UnsVd9hCHAEMCC_k94qwGaK22vqBqjRDsCcVwZsKkLP_brweRTw==",
    "count": "1",
    "uploadedfiles": '["50021671392639.jpg"]',
    "removefiles": "",
    "previousurl": "https://www.cava.tn/",
    "productId": "",
    "Products[category]": "2",
    "Products[subCategory]": "52",
    "Products[attributes][16]": "10820",
    "Products[attributes][17]": "1000",
    "range_values": ["10;999999", "1;10", "1;5"],
    "Products[attributes][21]": "3",
    "Products[attributes][22]": "1",
    "Products[attributes][40]": "10933",
    "Products[name]": "Vente",
    "Products[description]": "<p>Vente+appartement</p>",
    "Products[price]": "200000000",
    "Products[currency]": "TND-TND",
    "Products[product_phone]": "123456789",
    "Products[whatsapp]": "",
    "prod_location": "1",
    "Products[state]": "2",
    "under_state": "38",
    "Products[stateid]": "38",
    "Products[parentstateid]": "2",
    "abroadLocation": "",
    "Products[productCondition]": "",
    "Products[exchangeToBuy]": "0",
    "Products[delivery]": "0",
    "Products[videoUrl]": "",
    "Products[promotion][type]": "",
    "Products[promotion][addtype]": "",
    "Products[uploadSessionId]": "",
}


regions_dict = {
    "Ben Arous": 1,
    "Tunis": 2,
    "Ariana": 3,
    "Monastir": 4,
    "Gabes": 5,
    "Sousse": 6,
    "Nabeul": 7,
    "Medenine": 8,
    "Sfax": 9,
    "Kébili": 10,
    "Zaghouan": 11,
    "Kairouan": 12,
    "Manouba": 13,
    "Tataouine": 14,
    "Jendouba": 15,
    "Bizerte": 16,
    "Mahdia": 17,
    "Kasserine": 18,
    "Sidi Bouzid": 19,
    "Tozeur": 20,
    "Kef": 21,
    "Gafsa": 22,
    "Siliana": 23,
    "Beja": 24,
}


tunis_villes_dict = {
    "Bardo": "47",
    "Carthage": "52",
    "Cite Intilaka": "341",
    "Cité Olympique": "53",
    "Djebel Jelloud": "38",
    "El Kabaria": "56",
    "El Khadra": "54",
    "El Kram": "42",
    "El Marsa": "46",
    "El Mourouj": "347",
    "El Omrane": "51",
    "El Omrane supérieur": "55",
    "El Ouardia": "45",
    "Elmanar": "58",
    "Elmanzah": "57",
    "Ettahrir": "50",
    "Ezzouhour": "40",
    "Goulette": "43",
    "Harairia": "41",
    "Khaznadar": "342",
    "Lafayette": "60",
    "Laouina": "59",
    "Les Berges du Lac": "344",
    "Moncef Bey": "345",
    "Mont Plaisir": "346",
    "Mutuelleville": "62",
    "Sidi Bou Said": "65",
    "Sidi Daoud": "64",
    "Sidi El Bechir": "48",
    "Sidi Hassine": "49",
    "Sijoumi": "44",
    "Tunis Medina": "348",
    "autres villes": "37",
    "ksar Said": "343",
    "selectionnez votre ville": "0",
}


PROPERTY_MAPPING = {
	'maison-villa': 53,
    'appartement': -1
}


TRANSACTION_MAPPING = {
    'Vente': 10934,
    'Location': 10933
}