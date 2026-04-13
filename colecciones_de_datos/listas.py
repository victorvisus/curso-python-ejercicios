"""
Listas
En Python hay cuatro tipos de colecciones:

-List: colección ordenada y mutable. Permite elementos duplicados.
-Tuple: colección ordenada e inmutable. Permite elementos duplicados.
-Set: colección no ordenada e indexable; no permite duplicados (aunque se pueden añadir elementos).
-Dictionary: colección no ordenada, mutable y accesible por clave. No permite claves duplicadas.

Una lista es una colección ordenada y mutable que puede contener elementos de diferentes tipos. Una lista puede estar vacía o contener elementos heterogéneos.

Se puede acceder por indice positivo o por su equivalente en negativo
"""

# Desempaquetado de listas
print("\n-- Desempaquetado de listas ----------------------------------------")
lst = list()
lst = ["item1", "item2", [4, 9.88, True, "amarillo"], "item4", "item5"]
lst.append("item6")
print(lst)
first_item, second_item, third_item, *rest, ultimo = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']
print(ultimo)  # item6

newLst = list()
newLst.append(first_item)
newLst.append(second_item)
newLst.append(third_item)
newLst.append(rest)
newLst.append(ultimo)
print(newLst)
"""
Slicing de listas
Índices positivos: especificando inicio, fin y salto obtenemos una nueva lista. (inicio por defecto 0, fin por defecto len(lst) - 1, salto por defecto 1)
"""
print("\n-- Slicing de listas -----------------------------------------------")
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]  # devuelve todos los elementos
# mismo resultado que arriba
all_fruits = fruits[
    0:
]  # Si no se especifica el índice de fin, devolverá todos los elementos desde el inicio hasta el final
orange_and_mango = fruits[1:3]  # no incluye el índice 3
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[
    ::2
]  # usamos el tercer parámetro (paso). Toma cada 2 elementos - ['banana', 'mango']

"""
Modificar listas
"""
print("\n-- Modificar listas ------------------------------------------------")
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits)
fruits[2] = "kiwi"
print(fruits)

"""
Buscar elementos
"""
print("\n-- Buscar elementos ------------------------------------------------")
does_exist = "banana" in fruits
print(does_exist)  # True
does_exist = "lime" in fruits
print(does_exist)  # False
"""
Agregar elementos
"""
print("\n-- Agregar elementos -----------------------------------------------")
fruits.append("papaya")
print(fruits)

"""
Insertar elementos
 insertar un elemento en un índice específico de la lista
"""
print("\n-- Insertar elementos ----------------------------------------------")
print(fruits)
fruits.insert(2, "apple")  # inserta 'apple' entre 'orange' y 'mango'
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, "lime")  # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

"""
Eliminar elementos
"""
print("\n-- Eliminar elementos ----------------------------------------------")
fruits.remove("banana")
print(
    fruits
)  # ['orange', 'mango', 'lemon', 'banana'] - este método elimina la primera aparición del elemento en la lista
fruits.remove("lemon")
print(fruits)  # ['orange', 'mango', 'banana']

"""
Eliminar con pop()
Usa pop() para eliminar el elemento en el índice dado (si no se indica, elimina el último elemento):
"""
print("\n-- Eliminar con pop() ----------------------------------------------")
fruits.pop()  ## elimina el ultimo elemento
print(fruits)  # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)  # ['orange', 'mango']

"""
Eliminar con del
Usa la palabra clave del para eliminar un índice específico, también puede eliminar un rango de índices o eliminar por completo la lista
"""
print("\n-- Eliminar con del ------------------------------------------------")
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)  # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[
    1:3
]  # elimina elementos en el rango dado; no eliminará el elemento con índice 3!
print(fruits)  # ['orange', 'lime']
# del fruits
# print(fruits)  # Esto producirá: NameError: name 'fruits' is not defined


"""
Vaciar listas
"""
print("\n-- Vaciar listas ---------------------------------------------------")
fruits.clear()
print(fruits)  # []

"""
Copiar listas
list2 = list1. En ese caso list2 referencia el mismo objeto; los cambios se reflejarán en ambos. Si quieres una copia independiente usa el método copy(). Clona el contenido de la lista en una nueva lista
"""
print("\n-- Copiar listas ---------------------------------------------------")

fruits = ["banana", "orange", "mango", "lemon"]
print("frutas original ", fruits)
fruits_copy = fruits.copy()
print(
    "frutas nuevo ", fruits_copy
)  # ['banana', 'orange', 'mango', 'lemon'] (copia de la lista)
fruits_copy[0] = "apple"
print("frutas nuevo modificado ", fruits_copy)  # ['apple', 'orange', 'mango', 'lemon']

"""
Unir listas
"""
print("\n-- Unir listas -----------------------------------------------------")
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Usar el método extend() El método extend() puede anexar una lista a otra.
print("\n-- Unir listas con extends() ---------------------------------------")
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits.extend(vegetables)
print(
    "Fruits and vegetables:", fruits
)  # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']


"""
Contar elementos
count() para devolver el número de veces que aparece un elemento en la lista:
"""
print("\n-- Contar num elementos repetidos ----------------------------------")
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.count("orange"))  # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3


"""
Encontrar el índice de un elemento
"""
print("\n-- Encontrar el índice de un elemento ------------------------------")

fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2, primera aparición
"""
Invertir listas
"""
print("\n-- Invertir listas -------------------------------------------------")

fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]

"""
Ordenar listas
Para ordenar una lista podemos usar el método sort() o la función incorporada sorted(). El método sort() reordena la lista en orden ascendente y modifica la lista original. Si el parámetro reverse de sort() es True, ordenará la lista en orden descendente.
"""
print("\n-- Ordenar listas --------------------------------------------------")
# sort(): Este método modifica la lista original
print("\n-- sort() ----------------------------------------------------------")

lst = ["item1", "item2"]
lst.sort()  # ascending
lst.sort(reverse=True)  # descending

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  #  [26, 25, 25, 24, 24, 24, 22, 19]

# sorted(): No modifica la lista original; devuelve una nueva lista, independiente de la original
print("\n-- sorted() --------------------------------------------------------")

fruits = ["banana", "orange", "mango", "lemon"]
print(sorted(fruits))  # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruitsNew = sorted(fruits, reverse=True)
print("Nueva fruits ordenada: ", fruitsNew)  # ['orange', 'mango', 'lemon', 'banana']
print("fruits original: ", fruits)  # ['orange', 'mango', 'lemon', 'banana']

fruitsNew.append("Hormigon")
print(
    "Nueva fruits modificada: ", fruitsNew
)  # ['orange', 'mango', 'lemon', 'banana', 'Hormigon']
print("fruits original: ", fruits)  # ['orange', 'mango', 'lemon', 'banana']
