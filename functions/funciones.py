# sin return ----------------------------------------------------------------------
def printNombre():
    nombre = "Victor"
    apellido = "Perez"
    nombre_completo = nombre + " " + apellido
    print(nombre_completo)


printNombre()


# con return ----------------------------------------------------------------------
def decirNombre():
    nombre = "David"
    apellido = "Garcia"
    nombre_completo = nombre + " " + apellido
    return nombre_completo


print(decirNombre())


# con parametros -----------------------------------------------------------------------
nombre = "Carlos"
apellido = "Rodriguez"


def decirNombre(nombre, apellido):
    nombre_completo = nombre + " " + apellido
    return nombre_completo


print(decirNombre(nombre, apellido))


# Pasar argumentos por clave y valor ----------------------------------------------------------------------
def print_fullname(firstname, lastname):
    space = " "
    full_name = firstname + space + lastname
    print(full_name)


print(print_fullname(firstname="Asabeneh", lastname="Yetayeh"))


def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)


print(add_two_numbers(num2=3, num1=2))  # el orden no importa

# Funciones que retornan valores - Parte 2 ----------------------------------------------------------------------


# Devolver booleanos: Ejemplo:
def is_even(n):
    if n % 2 == 0:
        print("even")
        return (
            True  # la instrucción return detiene la ejecución adicional en la función
        )
    return False


print(is_even(10))  # True
print(is_even(7))  # False


# Devolver listas: Ejemplo:
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))


# Funciones con parámetros por defecto -------------------------------------------------------------------------------
def greetings(name="Peter"):
    message = name + ", welcome to Python for Everyone!"
    return message


print(greetings())
print(greetings("Asabeneh"))


def generate_full_name(first_name="Asabeneh", last_name="Yetayeh"):
    space = " "
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
print(generate_full_name("David", "Smith"))


def calculate_age(birth_year, current_year=2021):
    age = current_year - birth_year
    return age


print("Age: ", calculate_age(1821))


def weight_of_object(mass, gravity=9.81):
    weight = (
        str(mass * gravity) + " N"
    )  # gravedad promedio en la superficie de la Tierra
    return weight


print(
    "Weight of an object in Newtons: ", weight_of_object(100)
)  # 9.81 - gravedad promedio en la Tierra
print(
    "Weight of an object in Newtons: ", weight_of_object(100, 1.62)
)  # gravedad en la Luna


"""
Número arbitrario de argumentos
Si no sabemos cuántos argumentos se pasarán a la función, podemos usar un parámetro con * para aceptar un número arbitrario de argumentos
"""


def sum_all_nums(*nums):
    total = 0
    print(type(nums))  # <class 'tuple'>, los argumentos se almacenan en una tupla
    for num in nums:
        total += num  # equivalente a total = total + num
    return total


print(sum_all_nums(2, 3, 5, True))  # 10


# Parámetros por defecto y arbitrarios en funciones
def generate_groups(team, *args):
    print(team, "-------")
    for i in args:
        print(i)


print(generate_groups("Team-1", "Asabeneh", "Brook", "David", "Eyob"))


# Función como parámetro de otra función
# Puedes pasar una función como argumento
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))  # 27
