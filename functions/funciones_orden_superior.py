"""
En Python, las funciones son tratadas como ciudadanos de primera clase; se pueden hacer las siguientes operaciones con funciones:

Una función puede recibir una o más funciones como parámetros
Una función puede ser el valor de retorno de otra función
Una función puede ser modificada
Una función puede asignarse a una variable
En esta sección discutiremos:

Pasar funciones como parámetros
Devolver funciones como valores de retorno
Usar closures y decoradores en Python
"""


# Funciones como parámetros
def sum_numbers(nums):  # función normal
    return sum(nums)  # usa la función incorporada sum


def higher_order_function(f, lst):  # pasar función como argumento
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # 15


# Funciones como valor de retorno
def square(x):  # función que devuelve el cuadrado
    return x**2


def cube(x):  # función que devuelve el cubo
    return x**3


def absolute(x):  # función que devuelve el valor absoluto
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # función de orden superior que devuelve una función
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute


result = higher_order_function("square")
print(result(3))  # 9
result = higher_order_function("cube")
print(result(3))  # 27
result = higher_order_function("absolute")
print(result(-3))  # 3
"""
En los ejemplos anteriores se observa que la función de orden superior devuelve distintas funciones según el parámetro pasado.
"""

# Closures en Python
"""
Python permite que una función anidada acceda al ámbito de su función envolvente externa. Esto se conoce como closure. Un closure en Python se crea al anidar una función dentro de otra función envolvente y devolver la función interna. Veamos un ejemplo.
"""


def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Decoradores en Python
""" Un decorador es un patrón de diseño que permite añadir nueva funcionalidad a un objeto sin modificar su estructura. Los decoradores normalmente se usan aplicándolos antes de la definición de la función que se desea decorar. """


# Crear decoradores
# Para crear un decorador necesitamos una función externa que contenga una función envoltura interna.
# función normal
def greeting():
    return "Welcome to Python"


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON

# Implementando lo anterior con sintaxis de decorador

"""Esta función decoradora es una función de orden superior que acepta una función como argumento"""


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator  # cada vez que se llame a la funcion greeting se aplica el decorador
def greeting():
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON

# Aplicar varios decoradores a una función
"""Estas funciones decoradoras son funciones de orden superior que reciben funciones como argumento"""


# primer decorador
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# segundo decorador
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string_decorator
@uppercase_decorator  # en este caso el orden importa, ya que .upper() no funciona sobre una lista
def greeting():
    return "Welcome to Python"


print(greeting())  # ['WELCOME', 'TO', 'PYTHON']

# Aceptar parámetros en decoradores
""" A menudo necesitamos que nuestras funciones acepten parámetros; por eso definimos decoradores que también los aceptan."""


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(
        "I am {} {}. I love to teach.".format(
            first_name,
            last_name,
        )
    )


print_full_name("Asabeneh", "Yetayeh", "Finland")
