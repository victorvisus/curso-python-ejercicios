"""
Bucle for
La palabra clave for se usa para crear bucles for. Es similar a otros lenguajes, pero con diferencias sintácticas. Se usa para iterar sobre secuencias (listas, tuplas, diccionarios, conjuntos, cadenas, etc.).
"""

# Bucle for para listas
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number es un nombre temporal que referencia el elemento de la lista dentro del bucle
    print(number)  # number se imprimirá línea por línea, de 0 a 5

# Bucle for para cadenas
language = "Python"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# Bucle for para tuplas
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# Bucle for para diccionarios Al iterar, se recorrerán las claves del diccionario.
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for key in person:
    print(key)  # sólo imprime las claves

for key, value in person.items():
    print(key, value)  # así podemos acceder a claves y valores durante la iteración

# Bucle for para conjuntos
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
    print(company)


"""
break y continue - parte 2
"""
# Pista: break: cuando queremos terminar el bucle antes de completarlo usamos break.
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)  # imprime 0, 1, 2, 3
    if number == 3:
        break

# En el ejemplo anterior, cuando number sea 3 el bucle terminará.

# continue: cuando queremos saltarnos la iteración actual y continuar con la siguiente usamos la palabra clave continue.
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print(
        "loop's end"
    )  # En resumen: para condiciones cortas se puede usar if y else en línea
print("outside the loop")
# En el ejemplo anterior, cuando number es 3, las instrucciones posteriores dentro del bucle se saltan y si hay más elementos por recorrer, continúa con la siguiente iteración.


# Bucles for anidados
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

# for y else
# Si queremos ejecutar un bloque de código al terminar el bucle, podemos usar la palabra clave else.
for number in range(11):
    print(number)  # prints 0 to 10, not including 11
else:
    print("The loop stops at", number)

# Sentencia pass
# En Python, cuando se requiere una instrucción (por ejemplo después de :) pero no queremos ejecutar código, usamos pass para evitar errores. También sirve como marcador para rellenar más adelante.
for number in range(6):
    pass
