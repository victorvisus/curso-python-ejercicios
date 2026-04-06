"""
1 Usa una comprensión de listas para filtrar los números negativos y ceros de la siguiente lista:
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

2 Aplana la siguiente lista de listas a una lista unidimensional:
    list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

    Salida:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

3 Crea la siguiente lista de tuplas usando una comprensión de listas:
    [(0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (2, 1, 2, 4, 8, 16, 32),
    (3, 1, 3, 9, 27, 81, 243),
    (4, 1, 4, 16, 64, 256, 1024),
    (5, 1, 5, 25, 125, 625, 3125),
    (6, 1, 6, 36, 216, 1296, 7776),
    (7, 1, 7, 49, 343, 2401, 16807),
    (8, 1, 8, 64, 512, 4096, 32768),
    (9, 1, 9, 81, 729, 6561, 59049),
    (10, 1, 10, 100, 1000, 10000, 100000)]

4 Aplana la siguiente estructura en una nueva lista:
    countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
    Salida:
    [['Finlandia', 'FIN', 'Helsinki'], ['Suecia', 'SWE', 'Estocolmo'], ['Noruega', 'NOR', 'Oslo']]

5 Convierte la siguiente lista en una lista de diccionarios:
    countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
    Salida:
    [{'País': 'Finlandia', 'Ciudad': 'Helsinki'},
    {'País': 'Suecia', 'Ciudad': 'Estocolmo'},
    {'País': 'Noruega', 'Ciudad': 'Oslo'}]

6 Convierte la siguiente lista en una lista de cadenas concatenadas:
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    Salida:
    ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

7 Escribe una función lambda que calcule la pendiente o la ordenada al origen de una función lineal.
"""

"""
Producto escalar
                 3
                 1
(3, 2, 0, -1, 5) -5
                 0
                 4

= 3*3 + 2*1 + 0*(-5) + (-1)*0 + 5*4
= 9 + 2 + 0 + 0 + 20
= 31
"""
listUno = [3, 2, 0, -1, 5]
listDos = [3, 1, -5, 0, 4]


def productoEscalar():
    res = 0
    for i in range(0, len(listUno)):
        # print(res, "+=", listUno[i], "*", listDos[i])
        res += listUno[i] * listDos[i]
    return res


print(productoEscalar())

matriz = [[3, 2, 0, -1, 5], [3, 1, -5, 0, 4]]
listCompre = [num for row in matriz for num in row]
# number for row in list_of_lists for number in row
print(listCompre)
