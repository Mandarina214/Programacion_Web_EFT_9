# retrostore/apis_externas.py

import requests

# API 1: RAWG Videojuegos
def buscar_juego(nombre):
    API_KEY = 'b2d8901e16494308ba69cf064182ae61'
    url = f'https://api.rawg.io/api/games'
    params = {'key': API_KEY, 'search': nombre}
    r = requests.get(url, params=params)
    return r.json()

# API 2: Conversión USD a CLP
def usd_a_clp():
    API_KEY = 'b54ee60731768ca998003513'
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/CLP'
    r = requests.get(url)
    return r.json()
