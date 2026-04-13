"""
Ejercicios: Nivel 1
1 Declara una lista vacía
2 Declara una lista con más de 5 elementos
3 Encuentra la longitud de la lista
4 Obtén el primer, medio y último elemento de la lista
5 Declara una lista llamada mixed_data_types que contenga tu nombre, edad, altura, estado civil y dirección
6 Declara una lista it_companies e inicialízala con: Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
7 Imprime la lista usando print()
8 Imprime el número de empresas en la lista
9 Imprime la primera, la del medio y la última empresa
10 Cambia el nombre de una de las empresas y vuelve a imprimir la lista
11 Agrega una empresa IT a it_companies
12 Inserta una empresa IT en la mitad de la lista
13 Cambia el nombre de una empresa en it_companies a mayúsculas (¡excepto IBM!)
14 Une it_companies en una cadena usando la cadena '#;  '
15 Verifica si una empresa existe en it_companies
16 Ordena la lista usando el método sort()
17 Invierte la lista en orden descendente usando reverse()
18 Corta (slice) las primeras 3 empresas de la lista
19 Corta (slice) las últimas 3 empresas de la lista
20 Corta la(s) empresa(s) del medio de la lista
21 Elimina la primera empresa IT de la lista
22 Elimina la(s) empresa(s) del medio de la lista
23 Elimina la última empresa IT de la lista
24 Elimina todas las empresas IT de la lista
25 Destruye la lista it_companies
26 Concatena las siguientes listas:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
27 Inserta 'Python' y 'SQL' después de full_stack en la lista concatenada.
"""

"""
Ejercicios: Nivel 2
1 A continuación, una lista con las edades de 10 estudiantes:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    1 Ordena la lista y encuentra la edad máxima y mínima
    2 Agrega la edad mínima y máxima nuevamente a la lista
    3 Encuentra la mediana de las edades (un elemento medio o el promedio de dos elementos medios)
    4 Encuentra la edad promedio (suma de todos los elementos dividida por su cantidad)
    5 Encuentra el rango de edades (máximo - mínimo)
    6 Compara |min - promedio| y |max - promedio| usando la función abs()
2 Encuentra el país del medio en la lista de países (https://github.com/Taki-Ta/30-Days-Of-Python-Simplified_Chinese_Version/blob/master/data/countries.py)
3 Divide la lista de países en dos listas iguales (si es par; si no, la primera lista tendrá un país más)
4 Para la lista ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'], separa los tres primeros países de los países nórdicos restantes.
"""
# 3 Encuentra la mediana de las edades (un elemento medio o el promedio de dos elementos medios)
# 1.- Ordenar la lista
# 2.- Contar el numero de elementos
# 2.1.- Si es impar: sacar el del medio


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 15, 19, 14, 33, 22, 16]
edades = sorted(ages)
numElementos = len(edades)
print("Edades ordenadas: ", edades, "\ntiene ", numElementos, " elementos")

if numElementos % 2 != 0:
    print("la lista es impar")
    mediana = int(numElementos / 2)
    print("La mediana es: ", edades[mediana])
else:
    print("la lista es par")
    pos1 = int(numElementos / 2) - 1
    pos2 = int(numElementos / 2)
    mediana = (edades[pos1] + edades[pos2]) / 2
    print("La mediana es:  {mediana:.3f}".format(mediana=mediana))
