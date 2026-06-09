import os

# Primero crear un archivo de prueba
with open("test_file.txt", "w") as f:
    f.write("contenido de prueba")

print("=== CASO 1: Excepción INTERNA (dentro del with) ===")
try:
    with open("test_file.txt", "r") as f:
        print(f"Fichero abierto: {not f.closed}")
        # Excepción interna
        raise ValueError("Error interno")
        contenido = f.read()
except ValueError as e:
    print(f"Excepción capturada: {e}")
    print(f"¿Fichero cerrado? {f.closed}")
    print(f"Variable f existe: {'f' in locals()}")

print("\n=== CASO 2: Excepción al ABRIR (antes de entrar al with) ===")
try:
    with open("datos.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError as e:
    print(f"Excepción capturada: {e}")
    print(f"Variable f existe: {'f' in locals()}")

print("\n=== CASO 3: Excepción interna CON IO ===")
try:
    with open("test_file.txt", "r") as f:
        contenido = f.read()
        print(f"Contenido leído: {contenido}")
        # Error después de operar con el fichero
        x = 1 / 0
except ZeroDivisionError as e:
    print(f"Excepción capturada: {e}")
    print(f"¿Fichero cerrado? {f.closed}")

# Limpiar
os.remove("test_file.txt")
