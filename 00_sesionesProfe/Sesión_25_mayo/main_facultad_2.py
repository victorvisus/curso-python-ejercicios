"""
Es crucial que importes tus modelos (Alumno, Asignatura, etc.) antes
 de ejecutar la creación de tablas; 
de lo contrario, SQLModel no sabrá qué tablas tiene que generar.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
# esta Aplicación se encarga de inicializar la base de datos al arrancar el servidor FastAPI
from BBDD.Conexion.database_facultad import inicializar_base_de_datos, create_db_and_tables, session_dep
from fastapi.templating import Jinja2Templates


# ¡IMPORTANTE! Importa aquí tus modelos para que SQLModel los registre
#from models import Alumno, Asignatura, Matricula 
# Importar la clase `Alumno` desde el submódulo donde está definida
from BBDD.Modelo.Alumno import Alumno, AlumnoBase
from BBDD.Modelo.Asignatura import Asignatura, AsignaturaBase
from BBDD.Modelo.Profesor import Profesor, ProfesorBase
from BBDD.Modelo.Matricula import Matricula, MatriculaBase
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Esto se ejecuta al arrancar el servidor FastAPI antes de recibir peticiones
    print("Reiniciando el servidor FastAPI... Verificando/Creando base de datos y tablas...")
    inicializar_base_de_datos()
    create_db_and_tables()  # Crea las tablas basándose en los modelos importados
    yield

app = FastAPI(lifespan=lifespan)
# una vez que el servidor esté arrancado, la base de datos y 
# las tablas estarán listas para usarse en los endpoints de la API.
# Por lo tanto, puedes definir tus endpoints aquí sin preocuparte por la 
# inicialización de la base de datos, siendo inncesario para el uso del API Rest 
# el reinicio del servidor tras la invocación de un endpoint.

templates = Jinja2Templates(directory="templates")

@app.get("/")
def inicio():
    return {"mensaje": "Servidor listo y base de datos verificada/creada"}



@app.post("/alumnos/", response_model=Alumno)
def crear_alumno(alumnoBase: AlumnoBase, session: session_dep):
    # FastAPI ya valida y convierte la entrada a una instancia de `Alumno`.
    # No es necesario llamar a `model_validate` (esa es una API de pydantic v2
    # y además aquí `Alumno` podría referirse al módulo si se importó mal).
    alumnoInvalido = False
    try:
        print(f"***************************")
        print(f"****************************NIF: {alumnoBase.NIF}")
        print(alumnoBase.email)
        if alumnoBase.validar_NIF(alumnoBase.NIF) and alumnoBase.validar_correo_regex(alumnoBase.email):  # Valida el NIF y el correo antes de guardar
            # ¿****devuelve un alumno*****?
            #Alumno alumno_db = alumnoBase + id
            print(f"Alumno válido: {alumnoBase.NIF} y {alumnoBase.email} han pasado las validaciones.")
            db_alumno = Alumno.model_validate(alumnoBase)  # Convierte el AlumnoBase a Alumno para la base de datos
            print(f"id de Alumno: {db_alumno.id}")
            session.add(db_alumno)
            session.commit()
            session.refresh(db_alumno) # esto es necesario para que `db_alumno` tenga el ID 
    # generado por la base de datos después de la inserción
            return db_alumno
        else:
            alumnoInvalido = True
            print(f"-----------------Alumno no válido: {alumnoBase.NIF} o {alumnoBase.email} han fallado las validaciones.")
            raise ValueError("Alumno no válido: NIF o correo electrónico no cumplen con las validaciones.")
    except (Exception, ValueError) as e:
        print(f"+++++++++++++++++++++Error al crear alumno: {e}")
        session.rollback()
        raise e
    finally:
        if alumnoInvalido:
            print(f"Alumno no válido: {alumnoBase.NIF} o {alumnoBase.email} han fallado las validaciones. No se ha guardado en la base de datos.")
        else:
            print(f"****Alumno creado exitosamente: {alumnoBase.NIF} y {alumnoBase.email} han pasado las validaciones y se han guardado en la base de datos.")
        session.close()

