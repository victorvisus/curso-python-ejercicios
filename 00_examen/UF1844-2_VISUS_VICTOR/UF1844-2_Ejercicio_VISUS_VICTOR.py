"""
1. Crear una clase en Python llamada Sismo, que tenga por atributos “fecha_y_horaUTC” (tipo datetime), “localización” (tipo str) y magnitud (tipo float) junto con un método de presentación tipo info que devuelva un string patrón como este: “A las 01:15:25 del 18/04/2026 hubo un seísmo de magnitud 1.7 en TORREVIEJA”. Probarla creando un objeto que la instancie y también el método, con datos de tu libre elección.
"""

import datetime
import json
import os
import subprocess

import requests
from bs4 import BeautifulSoup


class Sismo:
    def __init__(
        self, fecha_y_horaUTC: datetime.datetime, localizacion: str, magnitud: float
    ):
        self.fecha_y_horaUTC = fecha_y_horaUTC
        self.localizacion = localizacion
        self.magnitud = magnitud

        # Extraigo la hora y la fecha por separado
        self.hora = self.fecha_y_horaUTC.strftime("%H:%M:%S")
        self.fecha = self.fecha_y_horaUTC.strftime("%d/%m/%Y")

    def info(self):
        return f"A las {self.hora} del {self.fecha} hubo un seismo de magnitud {self.magnitud} en {self.localizacion}"


def crear_sismo():
    sismo = Sismo(datetime.datetime(2026, 4, 18, 1, 15, 25), "TORREVIEJA", 1.7)
    print("-- Ejercicio 1 -----------------------------------------------------\n")
    print(sismo.info())


"""
2. Leer la página https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias y extraer como una lista de diccionarios (Python), cada uno de ellos con claves Localización (valor str), fecha y hora UTC (valor datetime), y magnitud (valor float) de todos los sismos registrados, en formato lista, con técnica de web-scraping en Python. Probar la realización de esta captación, extracción y construcción.
"""


def capturar_sismos():
    url_scrap = "https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        resp = requests.get(url_scrap, headers=headers)
        print(f"El estado de la petición es: {resp.status_code}")

        soup = BeautifulSoup(resp.text, "html.parser")
        tabla = soup.find("table")

        if tabla is None:
            return []

        # Usamos tbody tr para asegurarnos de capturar solo las filas de datos
        tbody = tabla.find("tbody")
        filas = tbody.find_all("tr") if tbody else tabla.find_all("tr")[1:]

        lista_sismos = []

        for fila in filas:
            columnas = fila.find_all("td")

            # Verificamos que sea una fila con datos (suelen tener 10-12 columnas)
            if len(columnas) >= 10:
                try:
                    fecha_str = columnas[1].text.strip()
                    hora_str = columnas[2].text.strip()

                    # CAMBIO DE ÍNDICES:
                    # En la web del IGN, la magnitud suele ser el índice 7
                    # y la localización el índice 9 (ajustado para la versión 30 días)
                    magnitud_raw = columnas[7].text.strip()
                    localizacion_val = columnas[10].text.strip()

                    # Limpieza por si acaso viene el número con el tipo pegado (ej: "3.2 mbLg")
                    magnitud_val = float(magnitud_raw.split()[0].replace(",", "."))

                    fecha_hora_dt = datetime.datetime.strptime(
                        f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M:%S"
                    )

                    sismo_dict = {
                        "Localización": localizacion_val,
                        "fecha y hora UTC": fecha_hora_dt,
                        "magnitud": magnitud_val,
                    }

                    lista_sismos.append(sismo_dict)

                except (ValueError, IndexError):
                    # Si una fila falla (ej. fila de publicidad o formato raro), la saltamos
                    continue

        return lista_sismos

    except Exception as e:
        print(f"Error: {e}")
        return []


def print_sismos():
    print("\n-- Ejercicio 2 -----------------------------------------------------\n")

    resultado = capturar_sismos()

    # Imprimimo los 5 primeros
    for sismo in resultado[:5]:
        print(sismo)


"""
3. Pasar la lista de la pregunta 2. a continuación a formato JSON
"""


def convertir_a_json():
    print("\n-- Ejercicio 3 -----------------------------------------------------\n")
    lista_sismos = capturar_sismos()

    # Convertimos la lista a formato JSON (string)
    sismos_json = json.dumps(lista_sismos, indent=4, default=str, ensure_ascii=False)

    # Imprimimos el resultado
    print(sismos_json)

    # Guardo en un archivo .json
    with open("sismos.json", "w", encoding="utf-8") as f:
        f.write(sismos_json)

    print("Archivo JSON generado.")


"""
4. Crear un objeto que contenga la información del primer diccionario de la pregunta 2 (o primera “representación” JSON -string- equivalente de la pregunta 3), según la clase Sismo de la pregunta 1.
"""


def crear_objeto_sismo():
    print("\n-- Ejercicio 4 -----------------------------------------------------\n")
    sismo_dict = capturar_sismos()[0]
    sismo_obj = Sismo(
        sismo_dict["fecha y hora UTC"],
        sismo_dict["Localización"],
        sismo_dict["magnitud"],
    )
    print("Objeto Creado: ", sismo_obj.info())


def appInit():
    op = 99
    while op != 0:
        print(
            "\n-- Ejercicios ---------------------------------------------------------\n",
            "-- Elije una Opcion a ejecutar --\n",
            "--  1.- Crear Clase Sismo\n",
            "--  2.- Web-scraping Sismos\n",
            "--  3.- Convertir a JSON\n",
            "--  4.- Crear un objeto del primer diccionario de la pregunta 2\n",
            "--\n",
            "--  0.- Salir\n",
            "-------------------------------------------------------------------------\n",
        )
        try:
            op = int(input("Elije una opcion: "))
            if op == 1:
                limpiar_consola()
                print("Ejecutando: Crear Sismo...")
                crear_sismo()

            elif op == 2:
                limpiar_consola()
                print("Ejecutando: Variables complejas...")
                print_sismos()

            elif op == 3:
                limpiar_consola()
                print("Ejecutando: Convertir a JSON...")
                convertir_a_json()

            elif op == 4:
                limpiar_consola()
                print("Ejecutando: Crear un objeto del primer diccionario...")
                crear_objeto_sismo()
            elif op == 0:
                limpiar_consola()
                print("Saliendo...")
            else:
                print("\n[!] Esa opción no existe en el menú.")

            # 3. PAUSA CLAVE
            # Si no es 0, esperamos a que el usuario lea el resultado
            if op != 0:
                input("\nPresiona ENTER para volver al menú...")
        except ValueError as e:
            print("Elije una opcion correcta\n", e)


def limpiar_consola():
    try:
        # 'nt' es el nombre interno de Windows en Python
        if os.name == "nt":
            # Ejecuta 'cls' de forma segura
            subprocess.run("cls", shell=True)
        else:
            # Ejecuta 'clear' para Linux/Mac
            subprocess.run("clear", shell=True)
    except Exception:
        # Si por algo falla, imprimimos saltos de línea para "limpiar" visualmente
        print("\n" * 50)


appInit()
