def ejercicio07():
    try:
        with open("datos.txt", "r") as f:
            contenido = f.read()
            print("Lectura completada")
    except FileNotFoundError:
        print("Archivo no encontrado")

    print(f"¿Fichero cerrado? {f.closed if 'f' in locals() else 'No existe f'}")


ejercicio07()
