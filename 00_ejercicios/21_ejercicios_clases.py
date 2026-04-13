"""
Ejercicios: Nivel 1
Python tiene un módulo llamado statistics que podemos usar para calcular estadísticas. Ahora intentemos desarrollar una clase que calcule count, sum, min, max, range, mean, median, mode, standard deviation, variance, frequency distribution y describe.
"""


class Statistics:
    def __init__(self, data=[]):
        self.data = data

    def count(self):
        # tu propia implementación
        pass

    def sum(self):
        # tu propia implementación
        pass

    def min(self):
        # tu propia implementación
        pass

    def max(self):
        # tu propia implementación
        pass

    def range(self):
        # tu propia implementación
        pass

    def mean(self):
        # tu propia implementación
        pass

    def median(self):
        # tu propia implementación
        pass

    def mode(self):
        # tu propia implementación
        pass

    def standard_deviation(self):
        # tu propia implementación
        pass

    def variance(self):
        # tu propia implementación
        pass

    def frequency_distribution(self):
        # tu propia implementación
        pass

    def describe(self):
        # tu propia implementación
        pass


# código de prueba
data = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]
statistics = Statistics(data)
print("Count:", statistics.count())  # 25
print("Sum: ", statistics.sum())  # 730
print("Min: ", statistics.min())  # 24
print("Max: ", statistics.max())  # 38
print("Range: ", statistics.range())  # 14
print("Mean: ", statistics.mean())  # 29.2
print("Median: ", statistics.median())  # 27
print("Mode: ", statistics.mode())  # {'mode': 26, 'count': 5}
print("Standard Deviation: ", statistics.standard_deviation())  # 4.2
print("Variance: ", statistics.variance())  # 17.5
print(
    "Frequency Distribution: ", statistics.frequency_distribution()
)  # [(24, 2), (25, 1), (26, 5), (27, 4), (29, 1), (31, 2), (32, 3), (33, 2), (34, 2), (37, 2), (38, 1)]


"""
Ejercicios: Nivel 2
Crea una clase llamada PersonAccount. Debe tener firstname, lastname, incomes, expenses como atributos y métodos para añadir ingresos, añadir gastos y calcular el balance.
"""

"""
Ejercicios: Nivel 3
El siguiente código es una función; conviértelo en una clase con comportamiento equivalente.
"""


def print_products(*args, **kwargs):
    for product in args:
        print(product)
    print(kwargs)
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


print_products("apple", "banana", "orange", vegetable="tomato", juice="orange")

"""
En la clase PersonAccount diseña atributos firstname, lastname, incomes y expenses y añade métodos para calcular el ingreso neto de la persona.
"""
