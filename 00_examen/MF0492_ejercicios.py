def ejercicio01():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    resultado = d1 | d2
    print(resultado)


# ejercicio01()


from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def ejercicio05():
    # Conexión local
    # cliente = MongoClient("mongodb://localhost:27017/")
    # cliente = MongoClient("vichox.svkibw2.mongodb.net")

    # Base de datos MongoDB
    MONGO_URI = "mongodb+srv://victorvxg_db_user:ngvdKu8AKbtMDuUA@vichox.svkibw2.mongodb.net/?appName=vichox"

    # Create a new client and connect to the server
    cliente = MongoClient(MONGO_URI, server_api=ServerApi("1"))
    try:
        cliente.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")

    except Exception as e:
        print(e)
    db = cliente["tienda"]
    coleccion = db["productos"]
    # Inserción de un documento
    documento = {"nombre": "Laptop", "precio": 1200, "stock": 5}
    coleccion.insert_one(documento)
    # Consulta de búsqueda
    resultado = coleccion.find_one({"nombre": "Laptop"})
    print(resultado)


# ejercicio05()


def ejercicio06():
    x = 10
    try:
        resultado = 10 / 0
        x = 20
    except ZeroDivisionError:
        x = 30
        print("Error Zero detectado")
    except Exception:
        x = 40
        print("Error general")
    else:
        x = 50
        print("Sin errores")
    finally:
        x = x + 1
        print("Bloque final")
    print(f"Valor final: {x}")


# ejercicio06()


def ejercicio07():
    try:
        with open("datos.txt", "r") as f:
            contenido = f.read()
            print("Lectura completada")
    except FileNotFoundError:
        print("Archivo no encontrado")

    print(f"¿Fichero cerrado? {f.closed if 'f' in locals() else 'No existe f'}")


ejercicio07()

import re


def ejercicio10():

    texto = "El código 123 es válido, pero el 456 también lo es."
    patron = r"\d+"

    # Se ejecuta la operación sobre el texto
    resultado = re.findall(patron, texto)

    print(f"Tipo de dato: {type(resultado).__name__}")
    print(f"Contenido: {resultado}")


# ejercicio10()
