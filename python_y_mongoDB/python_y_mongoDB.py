"""
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/Spanish/27_python_with_mongodb_sp.md

MongoDB es una base de datos NoSQL. MongoDB almacena datos en documentos tipo JSON, lo que hace a MongoDB muy flexible y escalable. Veamos la terminología que difiere entre bases de datos SQL y NoSQL. La siguiente tabla mostrará la diferencia entre SQL y NoSQL.

SQL
    Base de datos
    Tabla
    Campo
    Registro
    Clave primaria

NoSQL
    Base de datos
    Colección
    Documento
    Campo
    Clave primaria
    Indice

ngvdKu8AKbtMDuUA
victorvxg_db_user

mongodb+srv://victorvxg_db_user:ngvdKu8AKbtMDuUA@vichox.svkibw2.mongodb.net/

infinityfree: 6HORxnlqKM55CV

https://www.mongodb.com/cloud
"""

from bson import json_util
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Base de datos MongoDB
MONGO_URI = "mongodb+srv://victorvxg_db_user:ngvdKu8AKbtMDuUA@vichox.svkibw2.mongodb.net/?appName=vichox"

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)

# CREAR BASE DE DATOS: db = client["thirty_days_of_python"]
db = client.thirty_days_of_python  # la primera vez se crea la base de datos

# CREAR COLECCIONES/TABLAS: students e insertar un documento
"""
db.students.insert_one({"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "age": 250})
print("Despues de crear tablas: ", client.list_database_names())
"""
# AÑADIR REGISTROS
""" students = [
    {"name": "David", "country": "UK", "city": "London", "age": 34},
    {"name": "John", "country": "Sweden", "city": "Stockholm", "age": 28},
    {"name": "Sami", "country": "Finland", "city": "Helsinki", "age": 25},
    {"name": "Eva", "country": "Spain", "city": "Barcelona", "age": 32},
    {"name": "Lukas", "country": "Lithuania", "city": "Vilnius", "age": 29},
]
for student in students:
    db.students.insert_one(student)
 """
# AÑADIR COLECCION teachers
"""
teachers = [
    {"name": "Mr. Johnson", "country": "USA", "city": "New York", "age": 45},
    {"name": "Ms. Rodriguez", "country": "Mexico", "city": "Mexico City", "age": 38},
    {"name": "Mr. Lee", "country": "South Korea", "city": "Seoul", "age": 42},
    {"name": "Ms. Brown", "country": "UK", "city": "London", "age": 40},
    {"name": "Mr. Patel", "country": "India", "city": "Mumbai", "age": 35},
]
try:
    for teacher in teachers:
        db.teachers.insert_one(teacher)

    print("teachers creado e insertados varios registros")
    print("Despues de crear tablas: ", client.list_database_names())
except Exception as e:
    print(e)
"""

# CONSULTAS de datos:
"""
student = db.students.find_one(
    {"_id": ObjectId("69de2961a08894a7eb124015")}
)  # consulta por ID
print(student)

students = db.students.find()  # todos los registros
print("registros con find(), con todos los campos -------------------")
for student in students:
    print(student)

students = db.students.find(
    {}, {"_id": 0, "name": 1, "country": 1}
)  # 0 excluir, 1 incluir
print("registros con find(), con campos seleccionados -------------------")
for student in students:
    print(student)
"""
# ACTUALIZAR REGISTROS
"""
db.students.update_one(
    {"name": "Asabeneh"}, {"$set": {"country": "Finland"}}
)  # actualizar un registro, segun el FILTER/WHERE
"""
# db.students.update_many({"city": "Stockholm"}, {"$set": {"city": "Madrid"}})
# ELIMINAR REGISTROS
"""
db.students.delete_one({"name": "David"})  # eliminar un registro
db.students.delete_many({"name": "Asabeneh"})  # eliminar varios
"""
#
# CONSULTAS de datos, WHERE "name": "Asabeneh"
"""
consulta = {"name": "Asabeneh"}
students = db.students.find(
    consulta, {"_id": 0, "name": 1, "country": 1}
)  # 0 excluir, 1 incluir
print(
    "registros con find(), name: Asabeneh con campos seleccionados -------------------"
)
for student in students:
    print(student)
"""
""" cadena = {"age": {"$gt": 30, "$lt": 42}}
teachers = db.teachers.find(cadena, {"_id": 0, "name": 1, "country": 1, "age": 1}).sort(
    "age", -1
)  # 0 excluir, 1 incluir, -1 descendente, 1 ascendente
for teacher in teachers:
    print(teacher)

 """


#
#
#
##############################################################################################3
# backup a json
def backup_a_json(_db_name, _col_name, _client):
    collection = _client[_db_name][_col_name]
    data = list(collection.find())

    with open(f"./ficheros/{_db_name}_{_col_name}.json", "w") as f:
        f.write(json_util.dumps(data, indent=4))

    print("✅ Archivo JSON generado.")


# backup_a_json("thirty_days_of_python", "students", client)
# backup_a_json("thirty_days_of_python", "teachers", client)


# resturar un backup a partir de un json
def restaurar_a_json(_json_file, _db_name, _col_name, _client):
    try:
        with open(_json_file, "rt", encoding="utf-8") as f:
            file_data = f.read()
            f_content = json_util.loads(file_data)
    except FileNotFoundError:
        print("El archivo no se ha encontrado. Asegúrate de que el path es correcto.")
    except Exception as e:
        print(e)

    db = _client[_db_name]
    coleccion = db[_col_name]

    try:
        for reg in f_content:
            if "_id" in reg:
                del reg["_id"]  # Borramos el ID conflictivo
            coleccion.insert_one(reg)
            print(f"Insertado: {reg}")
    except Exception as e:
        print(e)

    """
    # 2. Ahora f_content tiene Objetos reales, no diccionarios con "$"
    if isinstance(f_content, list):
        coleccion.insert_many(f_content)
        print(f"✅ Insertados {len(f_content)} registros.")
    else:
        coleccion.insert_one(f_content)
        print("✅ Insertado 1 registro.")
    """

    print("✅ Archivo JSON restaurado.")


# db.teachers.delete_many({})
""" restaurar_a_json(
    "./ficheros/thirty_days_of_python_teachers.json",
    "thirty_days_of_python",
    "teachers",
    client,
)
 """
