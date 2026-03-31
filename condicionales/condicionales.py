# Sintaxis
a = 3
if a > 0:
    print("A es un número positivo")
# A es un número positivo

# If Else
a = 3
if a < 0:
    print("A es un número negativo")
else:
    print("A es un número positivo")

# If Elif Else
a = 0
if a > 0:
    print("A es un número positivo")
elif a < 0:
    print("A es un número negativo")
else:
    print("A es cero")

# Abreviación
a = 3
print("A es positivo") if a > 0 else print(
    "A es negativo"
)  # Se cumple la primera condición, imprimirá 'A es positivo'

# Condicionales anidados
a = 0
if a > 0:
    if a % 2 == 0:
        print("A es un número positivo y par")
    else:
        print("A es un número positivo")
elif a == 0:
    print("A es cero")
else:
    print("A es un número negativo")

# If y operadores lógicos
a = 0
if a > 0 and a % 2 == 0:
    print("A es un número positivo y par")
elif a > 0 and a % 2 != 0:
    print("A es un número positivo")
elif a == 0:
    print("A es cero")
else:
    print("A es un número negativo")
