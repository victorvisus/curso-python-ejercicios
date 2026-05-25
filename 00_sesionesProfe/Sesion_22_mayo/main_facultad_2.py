"""
Es crucial que importes tus modelos (Alumno, Asignatura, etc.) antes
 de ejecutar la creación de tablas; 
de lo contrario, SQLModel no sabrá qué tablas tiene que generar.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
# esta Aplicación se encarga de inicializar la base de datos al arrancar el servidor FastAPI
from BBDD.Conexion.database_facultad import inicializar_base_de_datos, create_db_and_tables, session_dep


# ¡IMPORTANTE! Importa aquí tus modelos para que SQLModel los registre
#from models import Alumno, Asignatura, Matricula 
# Importar la clase `Alumno` desde el submódulo donde está definida
from BBDD.Modelo.Alumno import Alumno, AlumnoBase



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Esto se ejecuta al arrancar el servidor FastAPI antes de recibir peticiones
    print("Reiniciando el servidor FastAPI... Verificando/Creando base de datos y tablas...")
    inicializar_base_de_datos()
    create_db_and_tables()  # Crea las tablas basándose en los modelos importados
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def inicio():
    return {"mensaje": "Servidor listo y base de datos verificada/creada"}


@app.post("/alumnos/", response_model=Alumno)
def crear_alumno(alumno: AlumnoBase, session: session_dep):
    # FastAPI ya valida y convierte la entrada a una instancia de `Alumno`.
    # No es necesario llamar a `model_validate` (esa es una API de pydantic v2
    # y además aquí `Alumno` podría referirse al módulo si se importó mal).
    try:
        print(f"****************************NIF: {alumno.NIF}")
        print(alumno.email)
        if alumno.validar_NIF(alumno.NIF) and alumno.validar_correo_regex(alumno.email):  # Valida el NIF y el correo antes de guardar
            # ¿****devuelve un alumno*****?
            #Alumno alumno_db = alumnoBase + id
            session.add(alumno)
            session.commit()
            session.refresh(alumno)
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
    return alumno
