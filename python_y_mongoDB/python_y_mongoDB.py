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


infinityfree: 6HORxnlqKM55CV
"""

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
cadena = {"age": {"$gt": 30, "$lt": 42}}
teachers = db.teachers.find(cadena, {"_id": 0, "name": 1, "country": 1, "age": 1}).sort(
    "age", -1
)  # 0 excluir, 1 incluir, -1 descendente, 1 ascendente
for teacher in teachers:
    print(teacher)
#
#
#
##############################################################################################3
