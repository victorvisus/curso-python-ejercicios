import json

"""
usa el archivo countries-data.py.
    - ¿Cuántos idiomas distintos hay en los datos?
    - ¿Cuál es el idioma usado por más países?
    - Encuentra los diez países con mayor población.
"""

try:
    with open("./data/countries-data.json", "r", encoding="utf-8") as fichero:
        paises = json.load(fichero)
except FileNotFoundError:
    print("El archivo no se ha encontrado. Asegúrate de que el path es correcto.")
