import json
from operator import indexOf

"""
Ejercicios: Nivel 1
1 Declara una función add_two_numbers. Debe aceptar dos parámetros y devolver su suma.
2 La fórmula del área de un círculo es: area = π x r x r. Escribe una función area_of_circle que la calcule.
3 Escribe una función llamada add_all_nums que acepte un número arbitrario de argumentos y sume todos. Verifica que todos los elementos sean de tipo numérico. Si no, devuelve un mensaje apropiado.
4 La temperatura en Celsius (°C) se puede convertir a Fahrenheit (°F) con: °F = (°C x 9/5) + 32. Escribe una función convert_celsius_to_fahrenheit.
5 Escribe una función llamada check_season que acepte un mes y devuelva la estación: otoño, invierno, primavera o verano.
6 Escribe una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal.
7 La ecuación cuadrática se calcula como: ax² + bx + c = 0. Escribe una función solve_quadratic_eqn que calcule las soluciones.
8 Declara una función llamada print_list que acepte una lista y imprima cada elemento.
9 Declara una función llamada reverse_list que acepte un arreglo y devuelva su reverso (usa un bucle).
    print(reverse_list([1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]
    print(reverse_list1(["A", "B", "C"]))
    # ["C", "B", "A"]
10 Declara una función capitalize_list_items que acepte una lista y devuelva una lista con los elementos en mayúscula.
11 Declara una función add_item que acepte una lista y un ítem. Debe devolver la lista con el ítem agregado al final.
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
    numbers = [2, 3, 7, 9];
    print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
12 Declara una función remove_item que acepte una lista y un ítem. Debe devolver la lista con el ítem eliminado. Si lo encuentra
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    numbers = [2, 3, 7, 9];
    print(remove_item(numbers, 3))  # [2, 7, 9]
13 Declara una función sum_of_numbers que acepte un número y sume todos los números en ese rango.
    print(sum_of_numbers(5))  # 15
    print(sum_all_numbers(10)) # 55
    print(sum_all_numbers(100)) # 5050
14 Declara una función sum_of_odds que acepte un número y sume todos los impares en ese rango.
15 Declara una función sum_of_even que acepte un número y sume todos los pares en ese rango.
"""

"""
Ejercicios: Nivel 2
1 Declara una función evens_and_odds que acepte un entero positivo y calcule la cantidad de pares e impares en ese número.
    print(evens_and_odds(100))
    # La cantidad de números pares es 50.
    # La cantidad de números impares es 50.
2 Llama a tu función factorial que acepte un entero y devuelva su factorial.
3 Llama a tu función is_empty que acepte un argumento y verifique si está vacío.
4 Escribe distintas funciones que acepten listas y calculen: media, mediana, moda, rango, varianza y desviación estándar.
"""

"""
Ejercicios: Nivel 3
1 Escribe una función is_prime que verifique si un número es primo.
2 Escribe una función que verifique si todos los ítems en una lista son únicos.
3 Escribe una función que verifique si todos los ítems en una lista son del mismo tipo de dato.
4 Escribe una función que verifique si una variable proporcionada es un nombre de variable válido en Python.
5 Accede al archivo de datos countries-data.py.
    # Crea una función llamada the_most_spoken_languages que devuelva las 10 o 20 lenguas más habladas en el mundo, ordenadas de mayor a menor.
    # Crea una función llamada the_most_populated_countries que devuelva los 10 o 20 países más poblados del mundo, ordenados de mayor a menor.
"""

"""
El juego de la vida de conway
Juego de tres en raya
"""

# 3.2 Escribe una función que verifique si todos los ítems en una lista son únicos.
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Madrid"]


def comprobarLista(lista):
    for item in lista:
        if (
            lista.count(item) > 1
        ):  # Si el conteo de item es mayor que 1, significa que no es único
            print(f"El ítem '{item}' esta repetido en la lista.")
            return False, item
    return True


def verificaConSet(lista):
    if len(lista) == len(set(lista)):
        return True
    else:
        return False


def eliminarItem(lista, item):
    newLista = lista.copy()
    newLista.remove(item)

    return newLista


if comprobarLista(ciudades):
    print("La lista no es única.", comprobarLista(ciudades)[1])


# Escribe una funcion que verifique que todos los items en una lista son del mismo tipo de dato
def verificarTipo(lista):
    tipo = type(lista[0])  # Tomamos el tipo del primer elemento como referencia
    i = 1
    print(i, type(lista[0]))
    sonIgualesTodos = True
    while type(lista[i]) is tipo and i < len(lista):
        if i < len(lista) - 1:
            print(i, type(lista[i]))
            i = i + 1

        else:
            break
    else:
        sonIgualesTodos = False
    return sonIgualesTodos


lista1 = [False, False, False, False, False, True]
print(verificarTipo(lista1))


# 5 Accede al archivo de datos countries-data.py.
def accederArchivoTxt(dataFile):
    try:
        with open(dataFile, "r", encoding="utf-8") as f:
            contenido = f.read()
        print("lectura ok")
        return contenido
    except FileNotFoundError:
        print(f"El archivo {dataFile} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


rutaArchivo = "./data/countries.py"
contenidoArchivo = accederArchivoTxt(rutaArchivo)


def accederArchivoJson(dataFile):
    try:
        with open(dataFile, "r", encoding="utf-8") as f:
            contenido = json.load(f)
        print("lectura ok")
        return contenido
    except FileNotFoundError:
        print(f"El archivo {dataFile} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


# Crea una función llamada the_most_spoken_languages que devuelva las 10 o 20 lenguas más habladas en el mundo, ordenadas de mayor a menor.
def the_most_spoken_languages():
    # iterar 10 o 20 veces sobre la lista de idiomas más hablados, y extraer en cada iteraccion el idioma más hablado.
    listIdiomas = list(crearListaIdiomas(paises))
    conteoIdiomas = dict()
    for idioma in listIdiomas:
        for pais in paises:
            if idioma in pais["languages"]:
                if (
                    idioma in conteoIdiomas
                ):  # si está ese idioma en el diccionario de conteo, le sumamos 1 al conteo
                    conteoIdiomas[idioma] = conteoIdiomas[idioma] + 1
                else:
                    conteoIdiomas[idioma] = 1
    # ya tengo el dicionario conteoIdiomas con el número de países que hablan cada idioma, ahora busco el idioma con el conteo máximo
    idiomaMax = 0
    listaIdiomasMasHablados = []
    cont = 0
    while cont < 10:
        for idioma in listIdiomas:
            if conteoIdiomas[idioma] > idiomaMax:
                idiomaMax = conteoIdiomas[idioma]
                listaIdiomasMasHablados.append(
                    {"idioma": idioma, "conteo": conteoIdiomas[idioma]}
                )

        listIdiomas.remove(idioma)

        cont += 1
    return listaIdiomasMasHablados


def crearListaIdiomas(paises):
    idiomas = set()  # un set no permite elementos duplicados, así que es ideal para contar idiomas distintos
    for pais in paises:
        for idioma in pais["languages"]:
            idiomas.add(idioma)
    return list(idiomas)


print(crearListaIdiomas(accederArchivoJson("./data/countries-data.json")))
# Crea una función llamada the_most_populated_countries que devuelva los 10 o 20 países más poblados del mundo, ordenados de mayor a menor.
"""
Propuesta de solución:
Propuesta de solución:
1. acceder a través de la llamada a acceder_contenido...
2. comenzar con un máximo = 0.
3. iterar, examinando en cada iteración, el valor de la población para ese país, si es mayor, el máximo se cambia.
4. una vez iterado todo el diccionario, se quita ese país,
5. se repite el proceso con el diccionario modificado, hasta completar 10 iteraciones
"""


def the_most_populated_countries(paises):
    poblacionMax = 0
    listaPaisesMasPoblados = []
    cont = 0
    while cont < 10:
        for pais in paises:
            if pais["population"] > poblacionMax:
                poblacionMax = pais["population"]

        # print("añadimos: ", pais["name"])
        listaPaisesMasPoblados.append(pais)
        paises.remove(pais)
        poblacionMax = 0
        cont += 1
    return listaPaisesMasPoblados


# ejecucion ej. 4 y 5 //////////////////////////////////////////////////////////
rutaArchivo = "./data/countries-data.json"
paises = accederArchivoJson(rutaArchivo)


idiomasMasPoblados = the_most_populated_countries(paises)
for pais in idiomasMasPoblados:
    print(
        indexOf(idiomasMasPoblados, pais) + 1,
        pais["name"],
        "con una población de",
        pais["population"],
        "habitantes",
    )


paisesMasPoblados = the_most_populated_countries(paises)
for pais in paisesMasPoblados:
    print(
        indexOf(paisesMasPoblados, pais) + 1,
        pais["name"],
        "con una población de",
        pais["population"],
        "habitantes",
    )
