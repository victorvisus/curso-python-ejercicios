import re

"""
Función que cuenta las palabras en un archivo, excluyendo las que contienen números,
y agrega el conteo al final del archivo.
"""


def cuentaPalabras(fichero):
    # Bloque try para manejar excepciones, como si el archivo no existe
    try:
        # Abrir el archivo en modo lectura para obtener su contenido
        with open(fichero, "r", encoding="utf-8") as f:
            contenido = f.read()

        # Usar expresiones regulares para encontrar todas las secuencias de caracteres alfanuméricos (palabras)
        palabras = re.findall(r"\b\w+\b", contenido)

        # Filtrar la lista para excluir palabras que contengan dígitos (números)
        palabras_filtradas = [
            palabra for palabra in palabras if not any(c.isdigit() for c in palabra)
        ]

        # Calcular el número de palabras filtradas
        conteo = len(palabras_filtradas)

        # Abrir el archivo en modo append para añadir la línea con el conteo al final
        with open(fichero, "a", encoding="utf-8") as f:
            f.write(f"\nNúmero de palabras: {conteo}")

        # Retornar el conteo de palabras
        return conteo
    except FileNotFoundError:
        # Manejar el caso en que el archivo no se encuentre
        print(f"El archivo {fichero} no se encontró.")
        return 0


# Llamada de prueba a la función con el archivo especificado
resultado = cuentaPalabras("./ficheros/econom.txt")
print(f"Conteo de palabras: {resultado}")
