"""
💻 Ejercicios - Día 3
1 Declara una variable entera que represente tu edad
2 Declara una variable float que represente tu altura
3 Declara una variable compleja
4 Escribe un script que pida al usuario la base y la altura de un triángulo y calcule su área (Área = 0,5 x b x h).
    Entrada base: 20
    Entrada altura: 10
    El área del triángulo es 100
5 Escribe un script que pida al usuario los lados a, b y c de un triángulo y calcule su perímetro (Perímetro = a + b + c).
    Entrada lado a: 5
    Entrada lado b: 4
    Entrada lado c: 3
    El perímetro del triángulo es 12
6 Pide al usuario la longitud y la anchura de un rectángulo. Calcula su área (Área = largo x ancho) y su perímetro (Perímetro = 2 x (largo + ancho)).
7 Pide al usuario el radio de un círculo. Calcula su área (Área = pi x r x r) y su circunferencia (Circunferencia = 2 x pi x r), con pi = 3.14.
8 Calcula la pendiente, la intersección en x y la intersección en y de y = 2x - 2.
9 La pendiente se calcula como (m = (y2 - y1) / (x2 - x1)). Encuentra la pendiente y la distancia euclídea entre los puntos (2, 2) y (6, 10).
10 Compara las pendientes obtenidas en los ejercicios 8 y 9.
11 Calcula el valor de y para y = x^2 + 6x + 9. Prueba con distintos valores de x y encuentra cuándo y es 0.
12 Encuentra la longitud de 'python' y 'dragon', y realiza una comparación ficticia.
13 Usa el operador and para comprobar si tanto 'python' como 'dragon' contienen 'on'.
14 En la oración I hope this course is not full of jargon, usa el operador in para comprobar si contiene la palabra jargon.
15 Comprueba que ni 'dragon' ni 'python' contienen 'on'.
16 Encuentra la longitud de 'python', conviértela a float y luego a string.
17 Los números pares son divisibles por 2 con resto 0. ¿Cómo comprobar en Python si un número es par o impar?
18 Comprueba si la división entera de 7 entre 3 es igual al valor entero de 2.7.
19 Comprueba si el tipo de '10' es igual al tipo de 10.
20 Comprueba si int('9.8') es igual a 10.
21 Escribe un script que solicite las horas trabajadas y la tarifa por hora al usuario y calcule el salario.
   Introduce horas trabajadas: 40
   Introduce tarifa por hora: 28
   Tu salario semanal es 1120
22 Escribe un script que pida al usuario los años vividos y calcule cuántos segundos ha vivido una persona (supongamos que puede vivir 100 años).
   Introduce cuántos años has vivido: 100
   Has vivido 3153600000 segundos.
23 Escribe un script en Python que muestre la siguiente tabla
   1 1 1 1 1
   2 1 2 4 8
   3 1 3 9 27
   4 1 4 16 64
   5 1 5 25 125
"""

"""
Supongamos que me dan una hora, ejemplo: 14:04 y una cantidad de minutos:
dar la hora que supone sumar a la hora inicial la cantidad de minutos.
Tanto hora inicial como minutos se piden al usuario.
"""
# Paso 1: entender qué es una hora en el contexto: "una hora es 14 por un lado + : dos puntos + 04 por otro lado"
# Paso 1.1: como del usuario por defecto se toma str: se requiere separar la hora y los minutos de las hora que nos dan


horaInicial = input("Introduce la hora inicial (formato hh:mm): ")

horaInicialSeparada = horaInicial.split(":")

horas = int(horaInicialSeparada[0])  # horaInicialSeparada[0]
minutos = int(horaInicialSeparada[1])  # horaInicialSeparada[1]

# Paso 2: convertir la hora inicial a minutos
minutosIniciales = horas * 60 + minutos

# Paso 3: pedir los minutos a sumar
minutosAsumar = int(input("Introduce los minutos a sumar: "))

# Paso 3.1: sumar los minutos a los minutos iniciales
minutosFin = minutosIniciales + minutosAsumar
print("Minutos finales: ", minutosFin)

# Paso 4: convertir los minutos finales a horas y minutos
horaFinal = minutosFin / 60
print("hora final: ", horaFinal)

""" Opcion larga
minutosFinal = horaFinal - int(horaFinal)
print("minutos finales: ", int(minutosFinal * 60))
"""
""" Opcion con % """
minutosFinal = minutosFin % 60
print("minutos finales: ", minutosFinal)

print("hora final: ", int(horaFinal), ":", minutosFinal)

"""Cambiamos de dia"""
# Cambiamos las horas para que sean de 0 a 23
horaFinal = int(horaFinal) % 24
print("hora final: ", int(horaFinal), ":", minutosFinal)

horaInicialSeparada[0] = str(horaFinal)
horaInicialSeparada[1] = str(minutosFinal)  # minutosFinal
print(f"la hora es: {':'.join(horaInicialSeparada)}")  # ":".join(horaInicialSeparada)
