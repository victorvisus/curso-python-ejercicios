"""
Funciones lambda
Las funciones lambda son pequeñas funciones anónimas sin nombre. Pueden aceptar cualquier número de argumentos, pero solo una expresión. Las funciones lambda son similares a las funciones anónimas en JavaScript. Son útiles cuando necesitamos una función anónima dentro de otra función.

Crear una función lambda
Para crear una función lambda usamos la palabra clave lambda, seguido de uno o más parámetros y luego una expresión. La función lambda no usa return explícito; devuelve la expresión implícitamente.

# sintaxis
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
"""


# función nombrada
def add_two_nums(a, b):
    return a + b


print(add_two_nums(2, 3))  # 5

# con lambda
add_two_nums_lambda = lambda a, b: a + b
print(add_two_nums_lambda(2, 3))  # 5

# lambda autoejecutable
print((lambda a, b: a + b)(2, 3))  # 5

square = lambda x: x**2
print(square(3))  # 9
cube = lambda x: x**3
print(cube(3))  # 27

# múltiples variables
multiple_variable = lambda a, b, c: a**2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22

"""
Funciones lambda dentro de otra función
Uso de lambda dentro de otra función:
"""


def power(x):
    return lambda n: x**n


cube = power(2)(3)  # la función power ahora se usa con dos pares de paréntesis
print(cube)  # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32
