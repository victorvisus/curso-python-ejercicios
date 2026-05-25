"""Código de inicialización (database.py)Primero, 
asegúrate de tener instalado el driver de MySQL 
(por ejemplo: pip install pymysql).
este .py debería residir en el mismo directorio que tu 
main.py o en un subdirectorio accesible.
MiAplicacion|
            |-BBDD|
            |     |-Conexion-|_
            |     |            database_facultad.py
"""
import pymysql
import os
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends

# Cargar variables de entorno
load_dotenv()

# Configuración de la conexión (Asegúrate de cambiar tus credenciales)
USER = os.getenv('USER_DB')
PASSWORD = os.getenv('PASSWORD_DB')
HOST = os.getenv('HOST_DB')
PORT = os.getenv('PORT_DB')
DB_NAME = os.getenv('NAME_DB')

# URL de conexión para SQLModel
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Esta función obtiene la sesión de la base de datos para usarla en los endpoints de FastAPI
def get_session():
    with Session(engine) as session:
        yield session  # Entrega la sesión al endpoint y la cierra al terminar

# esta variable session_dep "empaqueta" 
# la sesión con los datos de la BD 
# necesarios en cada ocasión de invocación. 
# Evita tener que hacer conexiones nuevas con la BD.
session_dep = Annotated[Session, Depends(get_session)]

# Función para inicializar la base de datos y crear tablas
def inicializar_base_de_datos():
# PASO 1: Conectarse al servidor de MySQL sin especificar base de datos para crearla si no existe
    conexion_servidor = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        port=int(PORT)
    )
    try:
        with conexion_servidor.cursor() as cursor:
            # Crea la base de datos solo si no existe en el servidor
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4;")
    finally:
        conexion_servidor.close()
 # PASO 2: Ahora que la base de datos existe, 
 # SQLModel crea todas las tablas 
# basándose en los modelos que hayas importado.
    SQLModel.metadata.create_all(engine)


#Esta función se puede llamar al iniciar el servidor FastAPI para asegurarse 
# de que la base de datos y las tablas estén listas antes de manejar cualquier solicitud.
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)