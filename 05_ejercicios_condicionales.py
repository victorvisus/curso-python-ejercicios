"""
Ejercicios: Nivel 1
1 Usa input para obtener la edad del usuario (por ejemplo: "Introduce tu edad:"). Si el usuario tiene 18 años o más, muestra: 'Ya tienes la edad suficiente para aprender a conducir.' Si es menor, muestra cuántos años le faltan. Ejemplo de salida:

    Introduce tu edad: 30
    Ya tienes la edad suficiente para aprender a conducir.
    Salida:
    Introduce tu edad: 15
    Aún necesitas esperar 3 años para aprender a conducir.

2 Usa if…else para comparar my_age y your_age. ¿Quién es mayor (yo o tú)? Usa input("Introduce tu edad:") para obtener la edad. Puedes usar condicionales anidados para imprimir 'año' cuando la diferencia sea 1, 'años' para diferencias mayores, y un mensaje personalizado si my_age = your_age. Salida de ejemplo:

    Introduce tu edad: 30
    Tienes 5 años más que yo.

3 Pide al usuario dos números con input. Si a > b, imprime 'a es mayor que b'; si a < b, imprime 'a es menor que b'; si son iguales, imprime 'a es igual a b'.

    Introduce el primer número: 4
    Introduce el segundo número: 3
    4 es mayor que 3
"""

"""
Ejercicios: Nivel 2
1 Escribe un código que asigne una calificación según la nota del estudiante:

    80-100, A
    70-79, B
    60-69, C
    50-59, D
    0-49, F

2 Comprueba si es otoño, invierno, primavera o verano. Si el usuario introduce: Septiembre, Octubre o Noviembre → otoño. Diciembre, Enero o Febrero → invierno. Marzo, Abril o Mayo → primavera. Junio, Julio u Agosto → verano.

3 La siguiente lista contiene algunas frutas:
    fruits = ['banana', 'orange', 'mango', 'lemon']
    · Si una fruta no está en la lista, añádela e imprime la lista modificada. Si ya existe, imprime 'La fruta ya está en la lista'.
"""

frutas = ["banana", "orange", "mango", "lemon"]
nuevaFruta = ""  # Puedes cambiar esto por input("Ingrese una fruta: ") para obtener la fruta del usuario
# nuevaFruta = input("Ingrese una fruta: ")

if nuevaFruta in frutas:
    print("La fruta ya esta en la lista")
else:
    frutas.append(nuevaFruta)
    print("Fruta añadida: ", frutas)


"""
Ejercicios: Nivel 3
1 Aquí hay un diccionario persona. ¡Siéntete libre de modificarlo!
    person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finlandia',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Calle Espacial',
            'zipcode': '02210'
        }
    }

    * Comprueba si existe la clave skills en el diccionario; si existe, imprime la habilidad central de la lista skills.
    * Comprueba si existe la clave skills; si existe, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.
    * Si las habilidades son sólo JavaScript y React, imprime 'Es desarrollador frontend'; si incluyen Node, Python y MongoDB, imprime 'Es desarrollador backend'; si incluyen React, Node y MongoDB, imprime 'Es desarrollador full-stack'; en caso contrario, imprime 'Título desconocido' — puedes anidar más condiciones para mayor precisión.
    * Si la persona está casada y vive en Finlandia, imprime la siguiente línea:
        print('Asabeneh Yetayeh vive en Finlandia. Está casado.')
"""
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finlandia",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Calle Espacial", "zipcode": "02210"},
}
print(person["age"])
print(person["address"]["street"])
print(person["skills"][len(person["skills"]) - 1])
print(person["skills"][-1])

# Comprueba si existe la clave skills en el diccionario; si existe, imprime la habilidad central de la lista skills.
if "skills" in person:
    print(person["skills"][len(person["skills"]) // 2])
    if "Python" in person["skills"]:
        print("La persona tiene la habilidad Python")
    else:
        print("La clave 'skills' no existe en el diccionario.")


# Si las habilidades son sólo JavaScript y React, imprime 'Es desarrollador frontend'; si incluyen Node, Python y MongoDB, imprime 'Es desarrollador backend'; si incluyen React, Node y MongoDB, imprime 'Es desarrollador full-stack'; en caso contrario, imprime 'Título desconocido' — puedes anidar más condiciones para mayor precisión.

frontend = {"JavaScript", "React"}
backend = {"Node", "Python", "MongoDB"}
fullStack = {"React", "Node", "MongoDB"}

if len(person["skills"]) == 2 and frontend.issubset(person["skills"]):
    print("Es desarrollador frontend")
elif backend.issubset(person["skills"]):
    print("Es desarrollador backend")
elif fullStack.issubset(person["skills"]):
    print("Es desarrollador full-stack")
else:
    print("Título desconocido")
