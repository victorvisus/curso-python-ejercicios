"""
Función range().
La función range() genera una secuencia de números. La forma range(start, end, step) acepta tres parámetros: inicio, fin y paso. Por defecto inicio es 0 y el paso es 1. Se necesita al menos un parámetro (el valor de fin).
"""

# Usando range() para generar secuencias
lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))  # start y stop, paso por defecto 1
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0, 11, 2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)  #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)  # imprime 0 a 10, no incluye 11.
