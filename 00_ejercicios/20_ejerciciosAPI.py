"""
Ejercicios: Día 20
1 Lee sobre entornos virtuales, crea uno e instala al menos un paquete dentro del entorno.
2 Usa una API de países para obtener todos los datos y encuentra los 10 países más poblados.
3 Encuentra todos los países cuyo idioma oficial sea inglés (código 'eng') a partir de los datos de la API.
4 A partir de los datos de la API, encuentra los 10 países con mayor superficie.
5 Encuentra todos los países recién listados (o filtrados según la API) y ordénalos por capital.
"""

from package_ejerciciosAPI import accesos, gestion

URL = "https://restcountries.com/v3.1/all?fields=name,population"

accesos.accederAPI(URL)

datos_paises = accesos.accederAPI(URL)
# listaPaisesMasPobladosprint(datos_paises)

listaPaisesMasPoblados = gestion.los10MasPoblados(datos_paises)

# print("Los 10 paíseses con mayor población son: ", listaPaisesMasPoblados)


for i in range(10):
    print(listaPaisesMasPoblados[i]["name"], listaPaisesMasPoblados[i]["population"])
