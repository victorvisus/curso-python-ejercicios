from functools import reduce

# Funciones integradas de orden superior
"""En esta sección veremos algunas funciones integradas de orden superior como map(), filter() y reduce(). Las funciones lambda se pueden pasar como argumentos; su caso de uso ideal es con map, filter y reduce."""

# Python - función map

""" map() es una función integrada que recibe una función y un iterable como parámetros."""

# Ejemplo 1 -----------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x**2


numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
# Usemos lambda
numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# Ejemplo 2 -----------------------------------------------------------------
numbers_str = ["1", "2", "3", "4", "5"]  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))  # [1, 2, 3, 4, 5]

# Ejemplo 3 -----------------------------------------------------------------
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]  # iterable


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Usemos lambda
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

""" map itera sobre el iterable y devuelve un nuevo iterable transformado. """

# Python - función filter
""" filter() llama a la función especificada que retorna un valor booleano para cada elemento del iterable y filtra los elementos que cumplen la condición. """

# Ejemplo 1 -----------------------------------------------------------------
# filtremos solo los pares
numbers = [1, 2, 3, 4, 5]  # iterable


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4]

# Ejemplo 2
numbers = [1, 2, 3, 4, 5]  # iterable


def is_odd(num):
    if num % 2 != 0:
        return True
    return False


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # [1, 3, 5]

# filtrar nombres largos
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]  # iterable


def is_name_long(name):
    if len(name) > 7:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))  # ['Asabeneh']


# Python - función reduce
""" reduce() se define en el módulo functools; es necesario importarla desde allí. Al igual que map y filter, recibe una función y un iterable. Sin embargo, no devuelve otro iterable sino un único valor acumulado."""
# Ejemplo 1
numbers_str = ["1", "2", "3", "4", "5"]  # iterable


def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)  # 15
