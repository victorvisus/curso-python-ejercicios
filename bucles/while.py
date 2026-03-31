"""
Bucle while
Usamos la palabra clave while para crear un bucle while. Repite un bloque de código mientras la condición se cumpla. Cuando la condición se vuelve falsa, el bucle termina y se ejecuta el código que sigue.
"""

count = 0
while count < 5:
    print(count)
    count = count + 1
# prints from 0 to 4

"""
En el bucle anterior, cuando count llegue a 5 la condición se vuelve falsa y el bucle se detiene.
Si queremos ejecutar un bloque cuando la condición sea falsa, podemos usar la palabra clave else.
"""
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
"""
Cuando count sea 5 la condición será falsa, el bucle terminará y se ejecutará el bloque else; por tanto se imprimirá 5.
"""

# break y continue - parte 1
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
"""
El while anterior solo imprimirá 0, 1, 2; cuando count llegue a 3 el bucle terminará.
"""

"""
Continue: cuando queremos saltarnos la iteración actual y continuar con la siguiente usamos la palabra clave continue.
"""
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
