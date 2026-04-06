"""
Comprensiones de listas
En Python, las comprensiones de listas son una forma concisa de crear listas a partir de secuencias. Es una manera corta de crear nuevas listas a partir de secuencias. Las comprensiones de listas son más rápidas que iterar sobre listas con un bucle for.

# sintaxis
[i for i in iterable if expresión]

"""

"""
Ejemplo 1

Por ejemplo, si quieres convertir una cadena en una lista de caracteres, puedes hacerlo de varias formas. Veamos algunas:
"""
# un método
language = "Python"
lst = list(language)  # convertir la cadena en lista
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# segunda forma: comprensión de listas
lst = [i for i in language]
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

"""
Ejemplo 2

Por ejemplo, si quieres generar una lista de números:
"""
# generar números
numbers = [i for i in range(11)]  # genera números de 0 a 10
print("numbers: ", numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbersClassic = []
for i in range(11):
    numbersClassic.append(i)  # imprime números de 0 a 10
print("numbersClassic: ", numbersClassic)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# también puedes hacer operaciones matemáticas durante la iteración
squares = [i * i for i in range(11)]
print("squares: ", squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# también se pueden generar listas de tuplas
numbers = [(i, i * i) for i in range(11)]
print("numbers: ", numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

"""
Ejemplo 3

Las comprensiones de listas pueden combinarse con expresiones if:
"""
# generar números pares
even_numbers = [i for i in range(21) if i % 2 == 0]  # genera pares de 0 a 20
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# generar números impares
odd_numbers = [i for i in range(21) if i % 2 != 0]  # genera impares de 0 a 20
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# filtrar números: obtengamos los pares positivos
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# aplanar una lista 2D
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# forma clásica
flattened_list_classic = []
for row in list_of_lists:
    for number in row:
        flattened_list_classic.append(number)
print("flattened_list_classic: ", flattened_list_classic)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
