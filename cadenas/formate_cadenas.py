"""
Formateo clásico (% operador)
En Python existen varias maneras de formatear cadenas. En esta sección veremos algunas de ellas. El operador '%' se usa para formatear una tupla de variables dentro de una cadena de formato, usando especificadores como '%s', '%d', '%f' y '%.nf'.

%s - cadena (o cualquier objeto representable como cadena)
%d - entero
%f - punto flotante
"%.nf" - punto flotante con precisión fija (n decimales)
"""

print('\n""" Formateo clásico (% operador) """')
# Solo cadenas
first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am %s %s. I teach %s" % (first_name, last_name, language)
print(formated_string)

# Cadenas y números
radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of circle with a radius %d is %.2f." % (
    radius,
    area,
)  # 2 indica 2 decimales

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formated_string = "The following are python libraries:%s" % (python_libraries)
print(
    formated_string
)  # imprime "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"


"""
Formateo moderno (str.format)
Este método de formateo se introdujo en Python 3.
"""
print('\n""" Formateo moderno (str.format) """')
first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am {} {}. I teach {}".format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))  # limitar a dos decimales
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a**b))

# Salida
"""
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64
"""

# Cadenas y números
radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of a circle with a radius {} is {:.2f}.".format(
    radius, area
)  # mantener dos decimales
print(formated_string)


"""
Interpolación / f-Strings (Python 3.6+)
Otra forma moderna de formatear cadenas es la interpolación con f-strings. Las cadenas empiezan con f y se insertan expresiones entre llaves.
"""
print('\n""" Interpolación / f-Strings (Python 3.6+) """')
a = 4
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a**b}")
