"""
Ejercicio: Nivel 1
Crea una carpeta day_2 dentro de la carpeta 30DaysOfPython. Dentro de esa carpeta crea un archivo variables.py
Añade un comentario: 'Día 2: 30 Days of Python programming'
Declara una variable first_name y asígnale un valor
Declara una variable last_name y asígnale un valor
Declara una variable full_name y asígnale un valor
Declara una variable country y asígnale un valor
Declara una variable city y asígnale un valor
Declara una variable age y asígnale un valor
Declara una variable year y asígnale un valor
Declara una variable is_married y asígnale un valor
Declara una variable is_true y asígnale un valor
Declara una variable is_light_on y asígnale un valor
Declara múltiples variables en una sola línea
"""

print("\n-- # 1 Declaración de variables: --\n")

first_name = "Brenda"
lasta_name = "García"
full_name = first_name + " " + lasta_name
country = "Colombia"
city = "Bogotá"
age = 21
year = 2021
is_married = False
is_true = True
is_light_on = True
print(
    "Variables definidas: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
        first_name,
        lasta_name,
        full_name,
        country,
        city,
        age,
        year,
        is_married,
        is_true,
        is_light_on,
    )
)
"""
Ejercicio: Nivel 2
"""
print(
    "\n-- # 1 función integrada type() para comprobar el tipo de las variables declaradas: --\n"
)

# 1 Usa la función integrada type() para comprobar el tipo de las variables que declaraste
print(type(first_name))
print(type(lasta_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(
    "\n-- # 2 función len() para calcular la longitud de la variable first_name: --\n"
)
# 2 Usa la función len() para calcular la longitud de la variable first_name
print(len(first_name))

print("\n-- # 3 Compara la longitud de las variables first_name y last_name: --\n")
# 3 Compara la longitud de las variables first_name y last_name
print(len(first_name) > len(lasta_name))

"""
4 Declara las variables num_one = 5 y num_two = 4
---- Suma num_one y num_two y asigna el resultado a la variable total
---- Resta num_two de num_one y asigna el resultado a la variable diff
---- Multiplica num_one y num_two y asigna el resultado a la variable product
---- Divide num_one entre num_two y asigna el resultado a la variable division
---- Usa la operación módulo para obtener el resto de num_two dividido por num_one y asígnalo a remainder
---- Calcula num_one elevado a num_two y asigna el valor a exp
---- Calcula la división entera de num_one entre num_two (operación de floor division) y asigna el resultado a floor_division
"""
print("\n-- # 4 Declara las variables num_one = 5 y num_two = 4: --\n")
a = 5
b = 4
print("---- Suma num_one y num_two y asigna el resultado a la variable total")
total = a + b
"""
6 Usa la función integrada input() para obtener nombre, apellido, país y edad del usuario y almacena los valores en las variables correspondientes
7 Ejecuta help('keywords') en el intérprete de Python o en un archivo para comprobar las palabras reservadas (keywords) de Python
"""

# DIVISION DE MODULO
numero_uno = 85
numero_dos = 6

print("Division: ", numero_uno / numero_dos)  # division
print("El resto es: ", numero_uno % numero_dos)  # me da el resto, el resido
print("El cociente (modulo) es: ", numero_uno // numero_dos)  # me da el modulo


# Ejercicio 5.
print("\n-- Ejercicio 5 -------------------------------------------")
"""
5 El círculo tiene un radio de 30 metros.
---- Calcula el área del círculo y asígnala a la variable _area_of_circle_
---- Calcula la circunferencia del círculo y asígnala a la variable _circum_of_circle_
---- Pide el radio al usuario y calcula el área.
"""
radio = 30
diametro = radio * 2
piValor = 3.1416

_area_of_circle = piValor * radio**2
_circum_of_circle = piValor * diametro
print("El radio es: ", radio)
print("El area es: ", _area_of_circle)
print("La circunferencia es: ", _circum_of_circle)

print("\n-- Ejercicio 6 -------------------------------------------")
usrRadio = float(input("¿Cuál es tu radio?\n"))
_area_of_circle = piValor * pow(float(usrRadio), 2)
_circum_of_circle = piValor * (usrRadio * 2)
print("El nuevo radio es: ", radio)
print("La nueva area es: ", _area_of_circle)
print("La nueva circunferencia es: ", _circum_of_circle)
