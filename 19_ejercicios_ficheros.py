"""
Ejercicios: Nivel 1
1 Escribe una función que reciba un parámetro (nombre de archivo) y cuente el número de palabras del archivo.
2 Lee el archivo obama_speech.txt y cuenta las palabras.
3 Lee michelle_obama_speech.txt y cuenta las palabras.
4 Lee donald_speech.txt y cuenta las palabras.
5 Lee melina_trump_speech.txt y cuenta las palabras.
"""

import json

"""
Ejercicios: Nivel 2
Extrae todos los archivos Python del directorio del curso: a) Recorre la carpeta 30DaysOfPython, extrae todos los archivos .py y guarda sus nombres en files_list.txt b) Crea un script llamado find_python.py que pueda ejecutarse desde la línea de comandos c) Añade una opción --version para manejar argumentos de línea de comandos
"""
"""
Ejercicios: Nivel 3
Crea un archivo JSON a partir del siguiente dataset:
"""
python_libraries = [
    {
        "nombre_librería": "Django",
        "creador": "Adrian Holovaty",
        "primer_año_lanzamiento": 2005,
        "versión": "4.0.2",
        "uso": "Desarrollo web",
        "descripción": "Django permite construir aplicaciones web mejores y más rápido.",
    },
    {
        "nombre_librería": "Flask",
        "creador": "Armin Ronacher",
        "primer_año_lanzamiento": 2010,
        "versión": "2.0.2",
        "uso": "Desarrollo web",
        "descripción": "Flask es un micro framework WSGI para aplicaciones web.",
    },
    {
        "nombre_librería": "NumPy",
        "creador": "Travis Oliphant",
        "primer_año_lanzamiento": 2005,
        "versión": "1.22.0",
        "uso": "Cómputo científico",
        "descripción": "NumPy es la biblioteca fundamental para el cómputo científico en Python.",
    },
    {
        "nombre_librería": "Pandas",
        "creador": "Wes McKinney",
        "primer_año_lanzamiento": 2008,
        "versión": "1.4.0",
        "uso": "Análisis de datos",
        "descripción": "pandas es una librería open source para análisis y manipulación de datos.",
    },
    {
        "nombre_librería": "Matplotlib",
        "creador": "John D. Hunter",
        "primer_año_lanzamiento": 2003,
        "versión": "3.5.1",
        "uso": "Visualización de datos",
        "descripción": "Matplotlib es una librería para crear visualizaciones estáticas, animadas e interactivas en Python.",
    },
]
datos_url = "./files/python_libraries.json"


def crearJson(_datos, _datos_url):
    try:
        with open(_datos_url, "w", encoding="utf-8") as json_file:
            json.dump(_datos, json_file, ensure_ascii=False, indent=4)
    except PermissionError:
        print("No tienes permiso para escribir en el archivo.")
    except IsADirectoryError:
        print("El archivo es un directorio.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    else:
        print("El archivo se ha guardado correctamente.")


# crearJson(python_libraries, datos_url)

nueva_libreria = {
    "nombre_librería": "Pandas333",
    "creador": "Wes McKinney",
    "primer_año_lanzamiento": 2008,
    "versión": "1.4.0",
    "uso": "Análisis de datos",
    "descripción": "pandas es una librería open source para análisis y manipulación de datos.",
}


def agregarDatos(_datos, _datos_url):
    # Usando la funcion creada anteriormente
    with open(_datos_url, "rt", encoding="utf-8") as f:
        datos_py = json.load(f)
        datos_py.append(_datos)

        crearJson(datos_py, datos_url)


agregarDatos(nueva_libreria, datos_url)
