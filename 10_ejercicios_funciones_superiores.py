from functools import reduce

from data.countries import countries as paises

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
Ejercicios: Básico
1. Explica la diferencia entre map, filter y reduce.
2. Explica la diferencia entre función de orden superior, closures y decoradores.
3. Define la función que llama (ver ejemplo).
4. Imprime cada país de la lista countries usando un bucle for.
5. Imprime cada nombre de la lista names usando un bucle for.
6. Imprime cada número de la lista numbers usando un bucle for.
"""

"""
Ejercicios: Intermedio
1. Usa map para convertir cada país en countries a mayúsculas y genera una nueva lista.
2. Usa map para elevar al cuadrado cada número en numbers y genera una nueva lista.
3. Usa map para convertir cada nombre en names a mayúsculas y genera una nueva lista.
4. Usa filter para filtrar países que contienen 'land'.
5. Usa filter para filtrar países con exactamente seis caracteres.
6. Usa filter para filtrar países con seis o más caracteres.
7. Usa filter para filtrar países que comienzan con 'E'.
8. Encadena dos o más iteradores de lista (por ejemplo arr.map(callback).filter(callback).reduce(callback)).
9. Declara una función get_string_lists que reciba una lista y devuelva una lista con solo los elementos de tipo cadena.
10. Usa reduce para sumar todos los números en la lista numbers.
11. Usa reduce para concatenar todos los países en una oración: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
12. Declara una función categorize_countries que retorne una lista de países que siguen un patrón común (puedes ver la lista de países en el archivo countries.js del repositorio, por ejemplo 'land', 'ia', 'island', 'stan').
13. Crea una función que devuelva un diccionario donde las claves sean la primera letra de los nombres de país y el valor sea el número de países que comienzan con esa letra.
14. Declara una función get_first_ten_countries que devuelva los primeros diez países de la lista countries.js en la carpeta data.
15. Declara una función get_last_ten_countries que devuelva los últimos diez países de la lista.
"""

"""
Ejercicios: Avanzado
1. Usando el archivo countries_data.py (data\countries-data.json), completa lo siguiente:
    Ordena los países por nombre, capital y población.
    Ordena y obtiene los diez idiomas más usados.
    Ordena y obtiene los diez países con mayor población.
"""

# 4. Imprime cada país de la lista countries usando un bucle for.
print("\n-- # 4. Imprime cada país de la lista countries usando un bucle for: --")

for i in countries:
    print(i)

# 5. Imprime cada nombre de la lista names usando un bucle for.
print("\n-- # 5. Imprime cada nombre de la lista names usando un bucle for: --")

for i in names:
    print(i)
# 6. Imprime cada número de la lista numbers usando un bucle for.
print("\n-- # 6. Imprime cada número de la lista numbers usando un bucle for: --")
for i in numbers:
    print(i)

# 1. Usa map para convertir cada país en countries a mayúsculas y genera una nueva lista.
print(
    "\n-- # 1. Usa map para convertir cada país en countries a mayúsculas y genera una nueva lista: --"
)


def convertir_mayuscula(txt):
    return txt.upper()


print(list(map(convertir_mayuscula, countries)))


# 4. Usa filter para filtrar países que contienen 'land'.
print("\n-- # 4. Usa filter para filtrar países que contienen 'land': --")


def IsLand(pais):
    pais = pais.lower()
    return "land" in pais


print(list(filter(IsLand, countries)))
print("lambda: ", list(filter(lambda pais: "land" in pais.lower(), countries)))

# 5. Usa filter para filtrar países con exactamente seis caracteres.
print("\n-- # 5. Usa filter para filtrar países con exactamente seis caracteres: --")


def isSIx(pais):
    if len(pais) == 6:
        return True
    return False


print(list(filter(isSIx, countries)))
print("Lambda: ", list(filter(lambda pais: len(pais) == 6, countries)))

# 6. Usa filter para filtrar países con seis o más caracteres.
print("\n-- # 6. Usa filter para filtrar países con seis o más caracteres.: --")


def isSixOrMore(pais):
    if len(pais) >= 6:
        return True
    return False


print(list(filter(isSixOrMore, countries)))
print("Lambda: ", list(filter(lambda pais: len(pais) >= 6, countries)))

# 7. Usa filter para filtrar países que comienzan con 'E'.
print("\n-- # 7. Usa filter para filtrar países que comienzan con 'E': --")


def firstLetter(pais):
    firstLet = pais[0]
    if firstLet == "E":
        return True
    return False


print(list(filter(firstLetter, countries)))

# 8. Encadena dos o más iteradores de lista (por ejemplo arr.map(callback).filter(callback).reduce(callback)).
print(
    "\n-- # 8. Encadena dos o más iteradores de lista (por ejemplo arr.map(callback).filter(callback).reduce(callback)): --"
)
print(list(map(convertir_mayuscula, filter(firstLetter, countries))))

# 9. Declara una función get_string_lists que reciba una lista y devuelva una lista con solo los elementos de tipo cadena.
print(
    "\n-- # 9. Declara una función get_string_lists que reciba una lista y devuelva una lista con solo los elementos de tipo cadena.: --"
)
listaVariada = ["Naranja", "Rojo", "Mercedes", 67, True, 3.7865]


def get_string_lists(e):
    if isinstance(e, str):
        return True
    return False


print(list(filter(get_string_lists, listaVariada)))
print("lambda: ", list(filter(lambda e: isinstance(e, str), listaVariada)))


# 10. Usa reduce para sumar todos los números en la lista numbers.
print("\n-- # 10. Usa reduce para sumar todos los números en la lista numbers: --")


def add_two_nums(x, y):
    return int(x) + int(y)


print("total con reduce(): ", reduce(add_two_nums, numbers))  # 15


# 11. Usa reduce para concatenar todos los países en una oración: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
print("\n-- # 11. Usa reduce para concatenar todos los países en una oración: --")


def juntarPaises(x, y):
    return x + ", " + y


print(reduce(juntarPaises, countries), " are north European countries.")
print(
    "Oración con reduce(): ",
    reduce(lambda x, y: x + ", " + y, countries) + " are north European countries.",
)
""" reduce() no necesita el list()"""

# 12. Declara una función categorize_countries que retorne una lista de países que siguen un patrón común (puedes ver la lista de países en el archivo countries.js del repositorio, por ejemplo 'land', 'ia', 'island', 'stan').
print("\n-- # 11. Usa reduce para concatenar todos los países en una oración: --")


# 1. Función que genera otra función (Valor de retorno)
def buscador_de_patrones(patron):
    """Retorna una función que comprueba si un texto contiene el patrón."""

    def comparar(nombre_pais):
        return patron.lower() in nombre_pais.lower()

    return comparar


# 2. Función principal (Orden Superior)
def categorize_countries(lista, patron):
    """Utiliza la HOF filter para devolver los países que coinciden."""
    # Obtenemos la función de comparación personalizada
    logica_filtro = buscador_de_patrones(patron)

    # filter() es la función de orden superior: recibe una función y un iterable
    resultado = list(filter(logica_filtro, lista))

    return resultado


# Ejemplo con 'land' (Finland, Iceland, Ireland, etc.)
paises_land = categorize_countries(paises, "land")

# Ejemplo con 'stan' (Afghanistan, Kazakhstan, etc.)
paises_stan = categorize_countries(paises, "stan")

# Ejemplo con 'ia' (Albania, Algeria, etc.)
paises_ia = categorize_countries(paises, "ia")

print(f"Países con 'land': {paises_land}")
print(f"\nPaíses con 'stan': {paises_stan}")
print(f"\nPaíses con 'ia': {len(paises_ia)} encontrados.")
