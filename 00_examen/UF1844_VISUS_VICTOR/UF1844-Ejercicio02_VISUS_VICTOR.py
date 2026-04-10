"""
2. Programar una función en Python que pida y tome del usuario un conjunto de 3 números enteros, con valoresposibles entre 0 y 99, sin repeticiones, programar también una segunda función en Python que, también tomando del usuario un conjunto de 3 números enteros, calcule y retorne todos los que faltan entre el mayor y el menor de los enteros dados anteriormente (no cuántos faltan, sino una lista con todos los que faltan). Tratar para la segunda de estas funciones las siguientes excepciones:
• Alguno de los números en el argumento de la función es menor que 0 o es mayor que 99.
• Entre los argumentos de la función hay valores que no representan un número entero.
Generar un diccionario con 4 claves y cambios dinámicos en los valores, cada una de las cuales indicará la amplitud de cada uno de los cuatro intervalos en que queda dividido el recorrido 0-99. A modo de ejemplo, si un usuario suministra: 5 45 66 el diccionario será:
{
        “intervalo1”:  5
        “intervalo2”: 40
        “intervalo3”: 21
        “intervalo4”: 34
}
Por último, transformar dicho diccionario a formato JSON.
Invocar las funciones necesarias para poder visualizar los resultados.
Probarlo con dos entradas diferentes de usuario.
(4 puntos)
"""

import json

"""
Pide al usuario 3 números enteros y válidos, sin repeticiones, y los devuelve en un conjunto.
Args: numRepeticiones (int): El número de repeticiones que tiene que hacer la solicitud al usuario, por defecto 3
Returns: set: Un conjunto con los 3 números enteros y válidos.
"""


def solicitaNumeros(numRepeticiones=3):

    conjuntoNumeros = list()

    while len(conjuntoNumeros) < numRepeticiones:
        try:
            numero = int(input("Introduce un número entero: "))
            if validaNumeros(numero) and validarRepeticiones(numero, conjuntoNumeros):
                conjuntoNumeros.append(numero)
        except ValueError as e:
            print(e)

    return conjuntoNumeros


"""
Valida si un número est  entre 0 y 99.
Args: numero (int): El número a validar.

Returns: bool: True si el número es válido, False en caso contrario.
"""


def validaNumeros(numero):

    if 0 <= numero <= 99:
        return True
    else:
        raise ValueError("El número introducido no es válido, debe estar entre 0 y 99")
        return False


"""
Valida si un número ya ha sido introducido anteriormente.
Args:
    numero (int): El número a validar.
    conjuntoNumeros (set): El conjunto de números introducidos anteriormente.
Returns: bool: True si el número no ha sido introducido anteriormente, False en caso contrario.
"""


def validarRepeticiones(numero, conjuntoNumeros):

    if numero not in conjuntoNumeros:
        return True
    else:
        raise ValueError(f"El número {numero} ya ha sido introducido anteriormente")
        return False


"""
Función en Python que, también tomando del usuario un conjunto de 3 números enteros, calcule y retorne todos los que faltan entre el mayor y el menor de los enteros dados anteriormente (no cuántos faltan, sino una lista con todos los que faltan). Tratar para la segunda de estas funciones las siguientes excepciones:
"""

"""
Haciendo nuso de la funcion solicitarNumeros(),
pide al usuario tantos numeros como repeticiones se indique en el argumento de la funcion solicitarNumeros(), en este caso 3
Calcule y devuelve todos los que faltan entre el mayor y el menor de los enteros dados 
anteriormente (no cuántos faltan, sino una lista con todos los que faltan). 

Returns: list: Una lista con todos los números que FALTAN entre el mayor y el menor de los enteros dados.
"""


def faltantes():

    try:
        # declaro el conjunto lista con los 3 números, llamando la funcion solicitaNumeros, que pide una serie de nnumeros al usuario
        conjuntoNumeros = solicitaNumeros(3)

        # creo una lista con todos los números que faltan entre el mayor y el menor de los enteros dados
        numerosFaltantes = list(range(min(conjuntoNumeros) + 1, max(conjuntoNumeros)))

        # recorro ambas listas comparando los numeros de cada una y los remuevo de la lista de numerosFaltantes, eliminando el que coincidan con los de la lista conjuntoNumeros
        for numero in conjuntoNumeros:
            if numero in numerosFaltantes:
                numerosFaltantes.remove(numero)
        return numerosFaltantes

    except ValueError as e:
        print("2--", e)  # lanza el error en la primera funcion solicitaNumeros()


def generarIntervalosYJson(lista):
    # 1. Ordenar la lista para calcular distancias
    n = sorted(lista)
    intervalos = {}

    # 2. Primer intervalo (desde 0 hasta el primer número)
    intervalos["intervalo1"] = n[0]

    # 3. Intervalos intermedios (distancia entre números)
    # Recorremos desde el segundo número hasta el último
    for i in range(1, len(n)):
        intervalos[f"intervalo{i + 1}"] = n[i] - n[i - 1]

    # 4. Último intervalo (desde el último número hasta 100)
    # La clave será "intervalo" + (cantidad de números + 1)
    intervalos[f"intervalo{len(n)}"] = 100 - n[-1]

    # 5. Transformar a JSON
    intervalos_json = json.dumps(intervalos, indent=4)

    return intervalos, intervalos_json


def appIni():
    print(
        "Ejercicio 2: Primera función: ----------------------------\n",
        solicitaNumeros(),
    )
    print("Ejercicio 2: Segunda función: --------------------------\n", faltantes())

    print("Ejercicio 2: Tercera Parte: ----------------------------\n")

    # Invocamos tu función original
    mis_numeros = solicitaNumeros(4)

    print(f"\nNúmeros obtenidos: {mis_numeros}")

    # Calculamos intervalos y JSON
    diccionario, el_json = generarIntervalosYJson(mis_numeros)

    print("\nDiccionario de amplitudes:")
    print(diccionario)

    print("\nResultado en formato JSON:")
    print(el_json)


appIni()
