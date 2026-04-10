"""
Leer datos desde una URL

pip install requests

En requests veremos métodos y atributos como get(), status_code, headers, text, json():
    · get(): solicita una URL y devuelve un objeto Response
    · status_code: código HTTP de la respuesta
    · headers: cabeceras de la respuesta
    · text: contenido en texto
    · json(): parsea JSON y devuelve estructuras de Python
"""

from pprint import pp  # pretty print para mostrar resultados legibles

import requests  # importar requests

url = "https://www.ietf.org/rfc/rfc6763.txt"  # URL con texto

response = requests.get(url)  # solicitar URL
print(response)
print(response.status_code)  # código de estado, 200 indica éxito
print(response.headers)  # cabeceras de la respuesta
# print(response.text)  # contenido en texto


# https://restcountries.com/v3.1/all?fields=name,flags

url = "http://api.worldbank.org/countries/et?format=json"  # API del Banco Mundial para Etiopía
response = requests.get(url)
print(response)  # objeto Response
print(response.status_code)  # 200 indica éxito
ethiopia_data = response.json()
pp(ethiopia_data)
