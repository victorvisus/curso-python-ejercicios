"""
1 Une las cadenas 'Thirty', 'Days', 'Of', 'Python' en 'Thirty Days Of Python'.
2 Une las cadenas 'Coding', 'For', 'All' en 'Coding For All'.
3 Declara la variable company y asígnale el valor inicial "Coding For All".
4 Imprime la variable company usando print().
5 Usa len() y print() para mostrar la longitud de la cadena company.
6 Usa el método upper() para convertir todos los caracteres a mayúsculas.
7 Usa el método lower() para convertir todos los caracteres a minúsculas.
8 Aplica capitalize(), title() y swapcase() sobre la cadena 'Coding For All'.
9 Extrae mediante slicing la primera palabra de 'Coding For All'.
10 Usa index, find u otros métodos para comprobar si la cadena 'Coding For All' contiene la palabra 'Coding'.
11 Reemplaza la palabra 'Coding' por 'Python' en 'Coding For All'.
12 Reemplaza 'Python for Everyone' por 'Python for All' (usa replace() u otro método).
13 Separa la cadena 'Coding For All' usando espacios como separador.
14 Divide la cadena 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' por las comas.
15 ¿Qué carácter está en el índice 0 de 'Coding For All'?
16 ¿Cuál es el índice del último carácter de 'Coding For All'?
17 ¿Qué carácter está en el índice 10 de 'Coding For All'?
18 Crea una sigla (acrónimo) a partir de 'Python For Everyone'.
Hecho - 19 Crea una sigla a partir de 'Coding For All'.
20 Usando index, determina la primera aparición de la letra 'C' en 'Coding For All'.
21 Usando index, determina la primera aparición de la letra 'F' en 'Coding For All'.
22 Usa rfind para determinar la última aparición de 'l' en 'Coding For All People'.
23 Usa index o find para encontrar la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'
24 Usa rindex para encontrar la última aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'.
25 Elimina la frase 'because because because' de: 'You cannot end a sentence with because because because is a conjunction'.
26 Encuentra la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'.
27 Elimina la frase 'because because because' de la oración anterior.
hecho - 28 ¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?
hecho - 29 ¿La cadena 'Coding For All' termina con la subcadena 'coding'?
30 Elimina los espacios en blanco a la izquierda y derecha de la cadena '   Coding For All      '.
31 Usando isidentifier(), ¿cuál de las siguientes devuelve True?
    30DaysOfPython
    thirty_days_of_python
hecho - 32 Dada la lista ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'], únela en una cadena separada por espacios.
33 Usa la secuencia de escape de nueva línea para separar las siguientes oraciones:
    I am enjoying this challenge.
    I just wonder what is next.
34 Usa la secuencia de tabulación para mostrar:
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
35 Usa un método de formateo de cadenas para imprimir:
    radius = 10
    area = 3.14 * radius ** 2
    # The area of a circle with radius 10 is 314 meters square.
36 Usa un método de formateo de cadenas para imprimir:
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144

"""

import os
import subprocess

challenge = "Coding For All"


# 1 Une las cadenas 'Thirty', 'Days', 'Of', 'Python' en 'Thirty Days Of Python'.
def unirCadenas():
    return " ".join(["Thirty", "Days", "Of", "Python"])


# 3 Declara la variable company y asígnale el valor inicial "Coding For All".
company = "Coding For All"


# 5 Usa len() y print() para mostrar la longitud de la cadena company.
def medirCadena():
    return len(company)


# 19 Crea una sigla a partir de 'Coding For All'.
# cortar en " " y añadir cada elemento a un array, despues extraer el primer indice de cada elemento str del array
def crearSiglas():
    # print("\n-- 19 Crea una sigla a partir de 'Coding For All'. ----")

    siglaArray = challenge.split(" ")
    siglas = siglaArray[0][0] + siglaArray[1][0] + siglaArray[2][0]
    return siglas


# 28 ¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?
def comprobarInicioCadena():
    if challenge.startswith("Coding"):
        print("Si")
    else:
        print("No")


# 29 ¿La cadena 'Coding For All' termina con la subcadena 'coding'?
print(
    "\n¿La cadena 'Coding For All' termina con la subcadena 'coding'?",
    challenge.endswith("Coding"),
)


# 32 Dada la lista ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'], únela en una cadena separada por espacios.
print("\n-- 32 Separa la cadena. ----")
palabras = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(f"Cadena: {' '.join(palabras)}")


def appInit():
    op = 99
    while op != 0:
        print(
            "\n-- Ejercicios ---------------------------------------------------------\n",
            "-- Elije una Opcion a ejecutar --\n",
            "-- 1.- Unir cadenas.\n",
            "-- 5.- Usa len() para mostrar la longitud de la cadena company.\n",
            "-- 19.- Crea una sigla a partir de 'Coding For All'.\n",
            "-- 28.- ¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?.\n",
            "--\n",
            "--  0.- Salir\n",
            "-------------------------------------------------------------------------\n",
        )
        try:
            op = int(input("Elije una opcion: "))
            if op == 1:
                limpiar_consola()
                print(
                    "Uniendo 'Thirty', 'Days', 'Of', 'Python' en 'Thirty Days Of Python'...."
                )
                print("La cadena final es: ", unirCadenas())

            elif op == 5:
                limpiar_consola()
                print("Midiendo...")
                print(
                    "La longitud de la cadena company = 'Coding For All' es de: ",
                    medirCadena(),
                )

            elif op == 19:
                limpiar_consola()
                print("Creando siglas de 'Coding For All'...")
                print("las Siglas son:", crearSiglas())

            elif op == 28:
                limpiar_consola()
                print("Comprobando si 'Coding For All' empieza con 'Coding'...")
                print(
                    "¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?\n",
                    comprobarInicioCadena(),
                )

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
