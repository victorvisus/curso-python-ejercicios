"""
1. Crear una clase en Python llamada Sismo, que tenga por atributos “fecha_y_horaUTC” (tipo datetime), “localización” (tipo str) y magnitud (tipo float) junto con un método de presentación tipo info que devuelva un string patrón como este: “A las 01:15:25 del 18/04/2026 hubo un seísmo de magnitud 1.7 en TORREVIEJA”. Probarla creando un objeto que la instancie y también el método, con datos de tu libre elección.
"""

import datetime

import requests


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


sismo = Sismo(datetime.datetime(2026, 4, 18, 1, 15, 25), "TORREVIEJA", 1.7)
print("-- Ejercicio 1 -----------------------------------------------------\n")
print(sismo.info())


"""
2. Leer la página https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias y extraer como una lista de diccionarios (Python), cada uno de ellos con claves Localización (valor str), fecha y hora UTC (valor datetime), y magnitud (valor float) de todos los sismos registrados, en formato lista, con técnica de web-scraping en Python. Probar la realización de esta captación, extracción y construcción.
"""
print("\n-- Ejercicio 2 -----------------------------------------------------\n")

url_scrap = "https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias"
# Estas son las cabeceras que imitan a un navegador Chrome en Windows
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.google.com/",
}
try:
    # Usamos requests.get para obtener datos de la URL
    resp = requests.get(url_scrap, headers=headers)
    # Comprobar el estado
    cod_estado = resp.status_code
    print(
        f"El estado de la petición es: {cod_estado}"
    )  # cod_estado)  # 200 indica éxito
except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Error de conexión: {e}")
except requests.exceptions.Timeout as e:
    print(f"Tiempo de espera agotado: {e}")
except Exception as e:
    print(e)
