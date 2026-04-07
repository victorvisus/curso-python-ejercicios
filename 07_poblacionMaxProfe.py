import json


# Accede al archivo de datos countries-data.py.
def acceder_countries_data():
    archivoPY = "./data/countries-data.py"
    try:
        with open(archivoPY, "r", encoding="utf-8") as f:
            contenido = f.read()
            print("Lectura OK")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


acceder_countries_data()
# Crea una función llamada the_most_populated_countries
# que devuelva los 10 o 20 países más poblados del mundo,
# ordenados de mayor a menor.
"""
Propuesta de solución:
1. acceder a través de la llamada a acceder_contenido...
2. comenzar con un máximo = 0.
3. iterar, examinando en cada iteración, el valor de la población para ese
país, si es mayor, el máximo se cambia.
4. una vez iterado todo el diccionario, se quita ese país,
5. se repite el proceso con el diccionario modificado,
hasta completar 10 iteraciones
"""


# devolver de una lista de países el diccionario
# del más poblado
def maximoPoblacion(paises):  # paises es una lista, cuidado!!!
    max = 0
    elQueMas = {}
    for pais in paises:  # pais es un diccionario. cuidado!!!
        if pais["population"] > max:
            elQueMas = pais
            max = elQueMas["population"]
    return elQueMas  # estructura de diccionario


def los10MasPoblados(paises):
    masPoblados = []
    elPais = {}
    for i in range(10):
        elPais = maximoPoblacion(paises)
        masPoblados.append(elPais)
        paises.remove(elPais)  # se elimina el país con ese nombre
        # de la lista. oJO!!! el remove produce error si no encuentra
    return masPoblados


los10 = los10MasPoblados(json.loads(acceder_countries_data()))
for i in range(10):
    print(los10[i]["name"], los10[i]["population"])
