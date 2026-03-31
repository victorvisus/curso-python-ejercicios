"""
Ejercicios: Nivel 1
1 Implementa iteraciones de 0 a 10 usando while y for.
2 Implementa iteraciones de 10 a 0 usando while y for.
3 Escribe un bucle que llame a print() 7 veces para producir este triángulo:
    #
    ##
    ###
    ####
    #####
    ######
    #######

4 Usa bucles anidados para producir la siguiente salida:
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #

5 Usando un bucle, produce la siguiente salida:
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100

6 Recorre con for la lista ['Python', 'Numpy','Pandas','Django', 'Flask'] e imprime cada elemento.
7 Recorre con for de 0 a 100 e imprime todos los números pares.
8 Recorre con for de 0 a 100 e imprime todos los números impares.
"""

"""
Ejercicios: Nivel 2
1 Usa un for para sumar los números de 0 a 100.
    The sum of all numbers is 5050.
2 Usa un for para sumar por separado los impares y los pares de 0 a 100.
    The sum of all odd numbers is 2500. And the sum of all even numbers is 2550.
"""
"""
Ejercicios: Nivel 3
1 Ve a la carpeta data y usa el archivo countries.py. Itera los países y extrae aquellos que contienen la cadena land.
2 Dada la lista fruits = ['banana', 'orange', 'mango', 'lemon'], invierte los elementos usando un bucle.
3 Ve a la carpeta data y usa el archivo countries-data.py.
    - ¿Cuántos idiomas distintos hay en los datos?
    - ¿Cuál es el idioma usado por más países?
    - Encuentra los diez países con mayor población.
"""
"""
Ejercicios: Nivel 4
1 Multiplicar dos matrices usando bucles anidados. (pista: hacn falta 3 for anidados - para comprobar el resultado: https://matrixcalc.org/es/)
"""

"""
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

# bucles anidados
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
    if (
        type(person[key]) in (list, tuple, set) and key == "skills"
    ):  # comprueba que sea de tipo lista, tupla o set y que la clave sea skills
        # if key == "skills":
        print("estamos en skills")
        for skill in person["skills"]:
            print(skill)
"""

# 1 Implementa iteraciones de 0 a 10 usando while y for.
print("-- # 1 Implementa iteraciones de 0 a 10 usando while y for. --")
contador = 0
while contador <= 10:
    print(contador)
    contador += 1

# 2 Implementa iteraciones de 10 a 0 usando while y for.
print("-- # 2 Implementa iteraciones de 10 a 0 usando while y for. --")
for i in range(10, 0, -1):
    print(i)

# 3 Escribe un bucle que llame a print() 7 veces para producir este triángulo:
print(
    "-- # 3 Escribe un bucle que llame a print() 7 veces para producir este triángulo: --"
)
for i in range(1, 8):
    print("# " * i)

# 4 Usa bucles anidados para producir la siguiente salida:
print("-- # 4 Usa bucles anidados para producir la siguiente salida: --")


# 5 Usando un bucle, produce la siguiente salida:
print("-- # 5 Usando un bucle, produce la tabla de cuadrados: --")
for i in range(0, 11):
    print(f"{i} x {i} = {i * i}")

"""
Ejercicios: Nivel 2
"""
# 1 Usa un for para sumar los números de 0 a 100.
print("-- # 1 Usa un for para sumar los números de 0 a 100. --")
suma = 0
for i in range(101):
    suma += i
print(f"La suma de todos los números de 0 a 100 es: {suma}")

# Variante: sumar solo los pares
suma_pares = 0
for i in range(0, 101, 2):
    suma_pares += i
print(f"La suma de todos los números pares de 0 a 100 es: {suma_pares}")

# Variante: sumar solo los impares
suma_impares = 0
for i in range(1, 101, 2):
    suma_impares += i
print(f"La suma de todos los números impares de 0 a 100 es: {suma_impares}")

# Variante: sumar los multiplos de 3
suma_tres = 0
for i in (0, 101, 3):
    suma_tres += i
print(f"La suma de todos los números múltiplos de 3 de 0 a 100 es: {suma_tres}")


# 2 Usa un for para sumar por separado los impares y los pares de 0 a 100.


"""
Ejercicios: Nivel 3
"""

countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]
# 1 Ve a la carpeta data y usa el archivo countries.py. Itera los países y extrae aquellos que contienen la cadena land.
listaLand = list()
for pais in countries:
    if "land" in pais.lower():
        listaLand.append(pais)
print(
    ", ".join(listaLand), end=".\n"
)  # imprime los países separados por coma y espacio, y al final un punto


# 2 Dada la lista fruits = ['banana', 'orange', 'mango', 'lemon'], invierte los elementos usando un bucle.
fruits = ["banana", "orange", "mango", "lemon"]
fruits_invertida = list()

for i in range(
    len(fruits) - 1, -1, -1
):  # el bucle empieza en el último índice de la lista (len(fruits) - 1) y termina en -1 (no incluido), con un paso de -1 (decremento)
    fruits_invertida.append(fruits[i])

print(fruits_invertida)

print(fruits[::-1])  # otra forma de invertir la lista usando slicing


# 3 Ve a la carpeta data y usa el archivo countries-data.py.
"""
Lo hago en ficheros.py
"""
