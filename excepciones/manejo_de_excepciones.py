"""
Manejo de excepciones
Python utiliza try y except para manejar errores de forma elegante. Salir de forma controlada (o manejar errores con elegancia) es una buena práctica: el programa detecta una condición de error y la maneja adecuadamente, normalmente mostrando un mensaje descriptivo en la terminal o en un registro. Las excepciones suelen deberse a factores externos al programa (entrada errónea, nombre de archivo incorrecto, archivo no encontrado, fallos de I/O, etc.). El manejo adecuado de excepciones evita que las aplicaciones se bloqueen.

En la sección anterior hemos cubierto los distintos tipos de errores en Python. Si usamos try y except correctamente, podemos impedir que esos errores hagan que el programa falle.
"""

# Ejemplo:
""" try:
    print(10 + "5")
except Exception:
    print("Ocurrió un error") """

# Ejemplo:
""" try:
    name = input("Introduce tu nombre:")
    year_born = input("¿En qué año naciste?:")
    age = 2026 - year_born
    print(f"Eres {name}. Tu edad es {age}.")
except Exception:
    print("Ocurrió un error") """

"""En el ejemplo anterior, se ejecuta el bloque de excepción, pero no sabemos exactamente qué pasó. Para identificar el problema podemos capturar tipos de excepción concretos. """

# En el siguiente ejemplo capturamos y mostramos el tipo de error:

""" try:
    name = input("Introduce tu nombre:")
    year_born = input("¿En qué año naciste?:")
    age = 2019 - year_born
    print(f"Eres {name}. Tu edad es {age}.")
except TypeError:
    print("Se produjo un error de tipo (TypeError)")
except ValueError:
    print("Se produjo un ValueError")
except ZeroDivisionError:
    print("Se produjo una división por cero (ZeroDivisionError)") """


# En el ejemplo anterior la salida será TypeError. Ahora añadamos bloques adicionales:
try:
    name = input("Introduce tu nombre:")
    year_born = input("¿En qué año naciste?:")
    age = 2019 - int(year_born)
    print(f"Eres {name}. Tu edad es {age}.")
except TypeError as e:
    print("Se produjo un error de tipo (TypeError)")
    print(e)
except ValueError as e:
    print("Se produjo un ValueError")
    print(e)
except ZeroDivisionError as e:
    print("Se produjo una división por cero (ZeroDivisionError)")
    print(e)
else:
    print("Este bloque se ejecuta normalmente después de try")
finally:
    print("Este bloque siempre se ejecuta.")

# También podemos simplificar el manejo de excepción así:
try:
    name = input("Introduce tu nombre:")
    year_born = input("¿En qué año naciste?:")
    age = 2019 - int(year_born)
    print(f"Eres {name}. Tu edad es {age}.")
except Exception as e:
    print(e)


# lanzar la excepcion
def dividir(a, b):
    if b == 0:
        raise Exception("No se puede dividir por 0")
    return a / b


# capturar la excepcion
try:
    raise Exception("Mi propia excepción")
except Exception as e:
    print(e)
