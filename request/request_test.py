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

import requests  # importar requests

url = "https://www.ietf.org/rfc/rfc6763.txt"  # URL con texto

response = requests.get(url)  # solicitar URL
print(response)
print(response.status_code)  # código de estado, 200 indica éxito
print(response.headers)  # cabeceras de la respuesta
# print(response.text)  # contenido en texto


https://restcountries.com/v3.1/all?fields=name,flags