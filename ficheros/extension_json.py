"""
Archivos con extensión json
JSON significa JavaScript Object Notation. Es básicamente una representación en cadena de un objeto JavaScript o de un diccionario Python.
"""

import json

# diccionario
person_dct = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"],
}
# JSON: la forma en cadena del diccionario
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
# Usamos triple comillas para que sea multilínea y más legible, esto se llama f-string
person_json = """{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}"""

"""
Convertir JSON a diccionario
Para convertir JSON a diccionario importamos el módulo json y usamos loads.
"""
# JSON
person_json = """{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}"""
# Convertir la cadena JSON a diccionario
person_dct = json.loads(person_json)
print("Imprimo el tipo: ", type(person_dct))
print("Imprimo el diccionario: ", person_dct)
print("Imprimo una clave del diccionario: ", person_dct["name"])


# TAREA: llevar el contenido de person_json a un fichero y desde ahi leerlo. ##########
try:
    with open("./ficheros/person_json.json", "rt", encoding="utf-8") as f:
        f_content = f.read()

    txt_dct = json.loads(f_content)
    print("Imprimo el tipo del contenido traido del archivo json: ", type(txt_dct))
    print("Imprimo el diccionario creado desde el archivo json: ", txt_dct)
    print("Imprimo una clave del diccionario: ", txt_dct["name"])

except FileNotFoundError:
    print("El archivo no se ha encontrado. Asegúrate de que el path es correcto.")
except json.JSONDecodeError:
    print("El archivo no es un JSON válido. Verifica su contenido.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")


# Convertir diccionario a JSON
# Para convertir un diccionario a JSON usamos dumps.

coche = {
    "marca": "Audi",
    "modelo": "A3",
    "color": "Negro",
    "motor": "1.4 TDI",
}

coche_json = json.dumps(coche, indent=4)  # dumps (con s) devuelve un string
print(type(coche_json))
print(coche_json)

# opcion con write, y se guarda en un archivo
with open("./ficheros/coche_json.json", "w", encoding="utf-8") as f:
    f.write(coche_json)

# opcion directa con dump()
mi_diccionario = {
    "nombre": "Juan",
    "apellido": "Pérez Nuñio",
    "edad": 25,
    "hobbies": ["futbol", "leer", "programar"],
}
with open("./ficheros/mi_diccionario.json", "w", encoding="utf-8") as f:
    json.dump(
        mi_diccionario, f, ensure_ascii=False, indent=4
    )  # dump() (sin s) no devuelve un string, escribe datos serializados en un archivo

# cargamos el archivo json creado en la linea anterior
with open("./ficheros/mi_diccionario.json", "r", encoding="utf-8") as f:
    persona = json.load(f)
    print(persona)
