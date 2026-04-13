import math
import os
import subprocess

"""
💻 Ejercicios - Día 3
1 Declara una variable entera que represente tu edad
2 Declara una variable float que represente tu altura
3 Declara una variable compleja
4 Escribe un script que pida al usuario la base y la altura de un triángulo y calcule su área (Área = 0,5 x b x h).
    Entrada base: 20
    Entrada altura: 10
    El área del triángulo es 100
5 Escribe un script que pida al usuario los lados a, b y c de un triángulo y calcule su perímetro (Perímetro = a + b + c).
    Entrada lado a: 5
    Entrada lado b: 4
    Entrada lado c: 3
    El perímetro del triángulo es 12
6 Pide al usuario la longitud y la anchura de un rectángulo. Calcula su área (Área = largo x ancho) y su perímetro (Perímetro = 2 x (largo + ancho)).
7 Pide al usuario el radio de un círculo. Calcula su área (Área = pi x r x r) y su circunferencia (Circunferencia = 2 x pi x r), con pi = 3.14.
"""

"""
8 Calcula la pendiente, la intersección en x y la intersección en y de y = 2x - 2.
9 La pendiente se calcula como (m = (y2 - y1) / (x2 - x1)). Encuentra la pendiente y la distancia euclídea entre los puntos (2, 2) y (6, 10).
10 Compara las pendientes obtenidas en los ejercicios 8 y 9.
11 Calcula el valor de y para y = x^2 + 6x + 9. Prueba con distintos valores de x y encuentra cuándo y es 0.
"""
""" Ejercicios normales
12 Encuentra la longitud de 'python' y 'dragon', y realiza una comparación ficticia.
13 Usa el operador and para comprobar si tanto 'python' como 'dragon' contienen 'on'.
14 En la oración I hope this course is not full of jargon, usa el operador in para comprobar si contiene la palabra jargon.
15 Comprueba que ni 'dragon' ni 'python' contienen 'on'.
16 Encuentra la longitud de 'python', conviértela a float y luego a string.
17 Los números pares son divisibles por 2 con resto 0. ¿Cómo comprobar en Python si un número es par o impar?
18 Comprueba si la división entera de 7 entre 3 es igual al valor entero de 2.7.
19 Comprueba si el tipo de '10' es igual al tipo de 10.
20 Comprueba si int('9.8') es igual a 10.
21 Escribe un script que solicite las horas trabajadas y la tarifa por hora al usuario y calcule el salario.
   Introduce horas trabajadas: 40
   Introduce tarifa por hora: 28
   Tu salario semanal es 1120
22 Escribe un script que pida al usuario los años vividos y calcule cuántos segundos ha vivido una persona (supongamos que puede vivir 100 años).
   Introduce cuántos años has vivido: 100
   Has vivido 3153600000 segundos.
23 Escribe un script en Python que muestre la siguiente tabla
   1 1 1 1 1
   2 1 2 4 8
   3 1 3 9 27
   4 1 4 16 64
   5 1 5 25 125
"""

"""
Supongamos que me dan una hora, ejemplo: 14:04 y una cantidad de minutos:
dar la hora que supone sumar a la hora inicial la cantidad de minutos.
Tanto hora inicial como minutos se piden al usuario.
"""
# Paso 1: entender qué es una hora en el contexto: "una hora es 14 por un lado + : dos puntos + 04 por otro lado"
# Paso 1.1: como del usuario por defecto se toma str: se requiere separar la hora y los minutos de las hora que nos dan


def sumarHoras():
    horaInicial = input("Introduce la hora inicial (formato hh:mm): ")

    horaInicialSeparada = horaInicial.split(":")

    horas = int(horaInicialSeparada[0])  # horaInicialSeparada[0]
    minutos = int(horaInicialSeparada[1])  # horaInicialSeparada[1]

    # Paso 2: convertir la hora inicial a minutos
    minutosIniciales = horas * 60 + minutos

    # Paso 3: pedir los minutos a sumar
    minutosAsumar = int(input("Introduce los minutos a sumar: "))

    # Paso 3.1: sumar los minutos a los minutos iniciales
    minutosFin = minutosIniciales + minutosAsumar
    # print("Minutos finales: ", minutosFin)

    # Paso 4: convertir los minutos finales a horas y minutos
    horaFinal = minutosFin / 60
    # print("hora final: ", horaFinal)

    """ Opcion larga
   minutosFinal = horaFinal - int(horaFinal)
   print("minutos finales: ", int(minutosFinal * 60))
   """
    """ Opcion con % """
    minutosFinal = minutosFin % 60
    # print("hora final: ", int(horaFinal), ":", minutosFinal)

    """Cambiamos de dia"""
    # Cambiamos las horas para que sean de 0 a 23
    horaFinal = int(horaFinal) % 24
    # print("hora final: ", int(horaFinal), ":", minutosFinal)

    horaInicialSeparada[0] = str(horaFinal)
    horaInicialSeparada[1] = str(minutosFinal)  # minutosFinal
    print(
        f"la hora es: {':'.join(horaInicialSeparada)}"
    )  # ":".join(horaInicialSeparada)


# print("\n-- Ejercicio 1, 2 y 3 ------------------------------------------------")
def ej02():
    # 1 Declara una variable entera que represente tu edad
    edad = 48
    # 2 Declara una variable float que represente tu altura
    altura = 1.78
    # 3 Declara una variable compleja
    complejo = 3 + 4j
    print(f"edad: {edad}, altura: {altura}, complejo: {complejo}")


"""
4 Escribe un script que pida al usuario la base y la altura de un triángulo y calcule su área (Área = 0,5 x b x h).
    Entrada base: 20
    Entrada altura: 10
    El área del triángulo es 100
"""


# print("\n-- Ejercicio 4 -------------------------------------------------------")
def calculaAreaTriangulo():
    print("---- Calcula el área de un triángulo")
    base = int(input("Introduce la base: "))
    altura = int(input("Introduce la altura: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es {area}")


"""
5 Escribe un script que pida al usuario los lados a, b y c de un triángulo y calcule su perímetro (Perímetro = a + b + c).
    Entrada lado a: 5
    Entrada lado b: 4
    Entrada lado c: 3
    El perímetro del triángulo es 12
"""


# print("\n-- Ejercicio 5 -------------------------------------------------------")
def calculaPrimetroTriangulo():
    print("---- Calcula el perímetro de un triángulo")
    ladoA = int(input("Introduce el lado A: "))
    ladoB = int(input("Introduce el lado B: "))
    ladoC = int(input("Introduce el lado C: "))
    perimetro = ladoA + ladoB + ladoC
    print(f"El perímetro del triángulo es {perimetro}")


"""
6 Pide al usuario la longitud y la anchura de un rectángulo. Calcula su área (Área = largo x ancho) y su perímetro (Perímetro = 2 x (largo + ancho)).
"""


def calculaAreaRectangulo():
    print("---- Calcula el área de un rectángulo")
    largo = int(input("Introduce el largo del rectangulo: "))
    ancho = int(input("Introduce el ancho del rectangulo: "))
    area = largo * ancho
    # print(f"El area del rectangulo es {area}")
    return area


"""
7 Pide al usuario el radio de un círculo. Calcula su área (Área = pi x r x r) y su circunferencia (Circunferencia = 2 x pi x r), con pi = 3.14.
"""


def calculaAreaCirculo():
    radio = int(input("Introduce el radio del circulo: "))
    area = math.pi * pow(radio, 2)
    return area


"""
8 Calcula la pendiente, la intersección en x y la intersección en y de y = 2x - 2.
"""


def calculaCosas():
    return "pa rato...., vengo a aprender programación, no matemáticas profundas..."


"""
12 Encuentra la longitud de 'python' y 'dragon', y realiza una comparación ficticia.
"""


def comparacionFicticia():
    print("No entiendo para que sirve esto...")

    palabra1 = "Python"
    palabra2 = "Dragon"
    res = len(palabra1) != len(palabra2)
    return res


"""
13 Usa el operador and para comprobar si tanto 'python' como 'dragon' contienen 'on'.
"""


def buscarOn():
    cad = "on"
    if cad in "python" and cad in "dragon":
        return True
    return False


"""
14 En la oración I hope this course is not full of jargon, usa el operador in para comprobar si contiene la palabra jargon.
"""


def buscarJArgon():
    frase = "I hope this course is not full of jargon"
    if "jargon" in frase:
        return True
    return False


"""
15 Comprueba que ni 'dragon' ni 'python' contienen 'on'.
"""


def noContienenOn():
    if "on" not in "dragon" and "on" not in "python":
        return False
    return True


"""
16 Encuentra la longitud de 'python', convierte la longitud a float y luego a string.
"""


def longitudPython():
    long = len("python")
    long = float(long)
    long = str(long)
    return "El type de la longitud es: " + str(type(long))


"""
17 Los números pares son divisibles por 2 con resto 0. ¿Cómo comprobar en Python si un número es par o impar?
"""


def esParOImpar():
    resp = "Para comprobar si un número es par o impar en Python, la forma más común es utilizar el operador módulo (%), que devuelve el residuo de una división; si el resultado de numero % 2 es 0, el número es par, y si es distinto de 0, es impar. "
    return resp


"""
18 Comprueba si la división entera de 7 entre 3 es igual al valor entero de 2.7.
"""


def divisionEntera():
    a = 7
    b = 3
    res = a // b
    print(f"El resultado de la division entera es: {res}")
    if res == 2.7:
        return True
    return False


"""
19 Comprueba si el tipo de '10' es igual al tipo de 10.
"""


def comprobarTipo():
    if type("10") is type(10):
        return True
    return False


"""
20 Comprueba si int('9.8') es igual a 10.
"""


def esIgual():
    if int(9.8) == 10:
        return True
    return False


def appInit():
    op = 99
    while op != 0:
        print(
            "\n-- Ejercicios ---------------------------------------------------------\n",
            "-- Elije una Opcion a ejecutar --\n",
            "--  1.- Sumar horas\n",
            "--  2.- Decalarar variables complejas\n",
            "--  4.- Calcular area triangulo\n",
            "--  5.- Calcular perimetro triangulo\n",
            "--  6.- Calcular área de un rectángulo\n",
            "--  7.- Calcular área de un círculo\n",
            "--  8.- Calcular la pendiente y demás cosas... (incluyo 9, 10 y 11)\n",
            "-- 12.- Comparación ficticia\n",
            "-- 13.- ¿Esta 'on' en 'python' y en 'dragon'?\n",
            "-- 14.- ¿Contiene 'jargon'?\n",
            "-- 15.- Comprobar que ni 'dragon' ni 'python' contienen 'on'\n",
            "-- 16.- Encuentra la longitud de 'python', convierte la longitud a float y luego a string\n",
            "-- 17.- Los números pares son divisibles por 2 con resto 0. ¿Como comprobar en Python si un número es par o impar?\n",
            "-- 18.- Comprueba si la divisió entera de 7 entre 3 es igual al valor entero de 2.7\n",
            "-- 19.- Comprueba si el tipo de '10' es igual al tipo de 10\n",
            "-- 20.- Comprueba si int('9.8') es igual a 10\n",
            "--\n",
            "--  0.- Salir\n",
            "-------------------------------------------------------------------------\n",
        )
        try:
            op = int(input("Elije una opcion: "))
            if op == 1:
                limpiar_consola()
                print("Ejecutando: Sumar horas...")
                sumarHoras()

            elif op == 2:
                limpiar_consola()
                print("Ejecutando: Variables complejas...")
                ej02()

            elif op == 4:
                limpiar_consola()
                print("Ejecutando: Área triángulo...")
                calculaAreaTriangulo()

            elif op == 5:
                limpiar_consola()
                print("Ejecutando: Perímetro triángulo...")
                calculaPrimetroTriangulo()

            elif op == 6:
                limpiar_consola()
                print("Ejecutando: Área de rectangulo...")
                print(f"El area del rectangulo es {calculaAreaRectangulo()}")

            elif op == 7:
                limpiar_consola()
                print("Ejecutando: Área de círculo...")
                print(f"El area del rectangulo es {calculaAreaCirculo()}")

            elif op == 8:
                limpiar_consola()
                print("Calculando la pendiente, la intersección, etc..etc...")
                print(f"La pendiente, la intersección, estarán {calculaCosas()}")

            elif op == 12:
                limpiar_consola()
                print("Ejecutando: Comparación ficticia")
                print(
                    f"La comparación ficticia de las longitudes de 'python' y 'dragon' es {comparacionFicticia()}"
                )

            elif op == 13:
                limpiar_consola()
                print("Buscando 'on' en 'python' y en 'dragon'")
                print(f"¿Esta 'on' en 'python' y en 'dragon'? {buscarOn()}")

            elif op == 14:
                limpiar_consola()
                print("Buscando 'jargon' en 'I hope this course is not full of jargon'")
                print(f"¿Contiene 'jargon'? {buscarJArgon()}")

            elif op == 15:
                limpiar_consola()
                print("Buscando 'on' en 'python' y 'dragon'")
                print(f"¿Ni 'dragon' ni 'python' contienen 'on'? {noContienenOn()}")

            elif op == 16:
                limpiar_consola()
                print("Buscando la longitud de 'python'")
                print(f"La longitud de 'python' es {longitudPython()}")

            elif op == 17:
                limpiar_consola()
                print("Comprobando si un número es par o impar")
                print(f"¿Es par o impar? {esParOImpar()}")

            elif op == 18:
                limpiar_consola()
                print(
                    "Comprobando si la divisió entera de 7 entre 3 es igual al valor entero de 2.7"
                )
                print(f"¿Es igual? {divisionEntera()}")

            elif op == 19:
                limpiar_consola()
                print("Comprobando si el tipo de '10' es igual al tipo de 10")
                print(f"¿Es igual? {comprobarTipo()}")

            elif op == 20:
                limpiar_consola()
                print("Comprobando si int('9.8') es igual a 10")
                print(f"¿Es igual? {esIgual()}")

            elif op == 0:
                limpiar_consola()
                print("Saliendo...")
            else:
                print("\n[!] Esa opción no existe en el menú.")

            # 3. PAUSA CLAVE
            # Si no es 0, esperamos a que el usuario lea el resultado
            if op != 0:
                input("\nPresiona ENTER para volver al menú...")
        except ValueError as e:
            print("Elije una opcion correcta\n", e)


def limpiar_consola():
    try:
        # 'nt' es el nombre interno de Windows en Python
        if os.name == "nt":
            # Ejecuta 'cls' de forma segura
            subprocess.run("cls", shell=True)
        else:
            # Ejecuta 'clear' para Linux/Mac
            subprocess.run("clear", shell=True)
    except Exception:
        # Si por algo falla, imprimimos saltos de línea para "limpiar" visualmente
        print("\n" * 50)


appInit()
