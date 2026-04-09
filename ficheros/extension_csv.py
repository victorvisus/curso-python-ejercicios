"""
Archivos con extensión csv
CSV significa Comma Separated Values (valores separados por comas). Es un formato sencillo para datos tabulares (como hojas de cálculo o bases de datos) muy común en ciencia de datos.
"""

import csv

# Lectura de archivos csv para construir "algo" en python, p.ej. un diccionario
with open("./files/csv_example.csv", "r", encoding="utf-8") as fichero:
    datos_csv = csv.reader(fichero, delimiter=",")
    num_fila = 0
    for fila in datos_csv:
        if num_fila == 0:
            print(f"Encabezados: {', '.join(fila)}")
            num_fila += 1

        else:
            print(f"{fila[0]} viene de {fila[1]}, {fila[2]}. Conoce {fila[3]}")
            num_fila += 1
    print(f"Lineas procesadas: {num_fila}")

# escribir csv
with open(
    "./files/csv_example_escrito.csv", "w+", encoding="utf-8", newline=""
) as fichero:
    escribir_csv = csv.writer(fichero, delimiter=",")
    # escribimos los encabezados
    escribir_csv.writerow(["nombre", "apellido", "ciudad", "skills"])
    # escribir datos
    escribir_csv.writerow(
        ["Victor", "Visús García", "Zaraguay", "algo, otra cosa, algo más"]
    )
