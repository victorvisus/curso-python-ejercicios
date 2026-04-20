"""
¿Qué es un módulo?
Un módulo es un archivo que contiene un conjunto de código o funciones que se pueden incluir en una aplicación. Un módulo puede ser un archivo con una sola variable, una función o una biblioteca de gran escala.

Crear módulos
Para crear un módulo, escribimos código en un script de Python y lo guardamos con extensión .py. En la carpeta del proyecto crea un archivo llamado mymodule.py. Escribamos algo de código en ese archivo.
En la carpeta del modulo poner un archivo __init__.py

Importar módulos
Para importar archivos usamos la palabra clave import y el nombre del archivo.
"""

# archivo main.py
import mymodule
from mymodule import generate_full_name
from mymodule import generate_full_name as fullname

print(mymodule.generate_full_name("Asabeneh", "Yetayeh"))  # Asabeneh Yetayeh

"""
Importar funciones desde un módulo
Podemos tener muchas funciones en un archivo y podemos importar cada una por separado.
"""


print(generate_full_name("Asabeneh", "Yetayeh"))  # Asabeneh Yetayeh

"""
Importar funciones y renombrarlas
Durante la importación también podemos renombrar nombres
"""


print(fullname("Asabeneh", "Yetayeh"))  # Asabeneh Yetayeh

"""
Importar módulos incorporados
Al igual que otros lenguajes, podemos importar módulos usando la palabra clave import. A continuación importamos algunos módulos incorporados que usamos con frecuencia. Algunos módulos comunes son: math, datetime, os, sys, random, statistics, collections, json, re
"""
