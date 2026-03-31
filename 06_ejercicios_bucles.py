"""
Ejercicios: Nivel 1
1 Implementa iteraciones de 0 a 10 usando while y for.
2 Implementa iteraciones de 10 a 0 usando while y for.
3 Escribe un bucle que llame a print() 7 veces para producir este triángulo:

    #
    ##
    ###
    ####
    #####
    ######
    #######

4 Usa bucles anidados para producir la siguiente salida:

    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #

5 Usando un bucle, produce la siguiente salida:

    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100

6 Recorre con for la lista ['Python', 'Numpy','Pandas','Django', 'Flask'] e imprime cada elemento.
7 Recorre con for de 0 a 100 e imprime todos los números pares.
8 Recorre con for de 0 a 100 e imprime todos los números impares.
"""

"""
Ejercicios: Nivel 2
1 Usa un for para sumar los números de 0 a 100.
    The sum of all numbers is 5050.
2 Usa un for para sumar por separado los impares y los pares de 0 a 100.
    The sum of all odd numbers is 2500. And the sum of all even numbers is 2550.
"""

"""
Ejercicios: Nivel 3
1 Ve a la carpeta data y usa el archivo countries.py. Itera los países y extrae aquellos que contienen la cadena land.
2 Dada la lista fruits = ['banana', 'orange', 'mango', 'lemon'], invierte los elementos usando un bucle.
3 Ve a la carpeta data y usa el archivo countries-data.py.
    - ¿Cuántos idiomas distintos hay en los datos?
    - ¿Cuál es el idioma usado por más países?
    - Encuentra los diez países con mayor población.
"""
"""
# Bucle for para diccionarios Al iterar, se recorrerán las claves del diccionario.
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for key in person:
    print(key)  # sólo imprime las claves

for key, value in person.items():
    print(key, value)  # así podemos acceder a claves y valores durante la iteración
"""

# bucles anidados
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for key in person:
    if (
        type(person[key]) in (list, tuple, set) and key == "skills"
    ):  # comprueba que sea de tipo lista, tupla o set y que la clave sea skills
        # if key == "skills":
        print("estamos en skills")
        for skill in person["skills"]:
            print(skill)
