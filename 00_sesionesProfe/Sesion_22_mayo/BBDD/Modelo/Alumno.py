from datetime import date
from sqlmodel import SQLModel, Field
from pydantic import field_validator
import re

class AlumnoBase(SQLModel):
    nombre: str = Field(max_length=255)
    fechaNacimiento: date = Field(nullable=False,index=True)
    NIF: str = Field(max_length=9, unique=True, nullable=False)  # 8 dígitos + letra, único y no nulo
    apellido1: str = Field(max_length=255, nullable=False)
    apellido2: str = Field(max_length=255, nullable=True)  # Puede ser nulo si el alumno no tiene segundo apellido
    email: str = Field(max_length=255, nullable=False, unique=True)  # Correo electrónico único y no nulo
    direccion: str = Field(max_length=255)
    codigoPostal: str = Field(max_length=10)
    municipio: str = Field(max_length=255)
    provincia: str = Field(max_length=255)
    beca: bool = Field(default=False)  # Indica si el alumno tiene beca, por defecto es False

    @field_validator("NIF")  
    @classmethod
    def validar_NIF(clase, valor: str) -> str:
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        resto = int(valor[:-1]) % 23
        if letras[resto]!=valor[-1].upper():
            raise ValueError(f"NIF inválido: la letra no coincide con el número. Se esperaba '{letras[resto]}', pero se recibió '{valor[-1]}'")
        print(f"NIF válido: {valor[-1]} coincide con la letra '{letras[resto]}'")
        return valor
        

    @field_validator("email") 
    @classmethod
    def validar_correo_regex(clase, correo: str) -> str:
        EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(EMAIL_REGEX, correo):
             raise ValueError(f"email inválido: '{correo}' no coincide con el formato estándar de correo electrónico")
        print(f"email válido: '{correo}' coincide con el formato estándar de correo electrónico")    
        return correo

class Alumno(AlumnoBase, table=True):
    id: int = Field(default=None, primary_key=True)

    
       
    

