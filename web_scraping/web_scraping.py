"""
¿Qué es el web scraping?
Internet está lleno de datos que pueden utilizarse para distintos fines. Para recopilar esos datos necesitamos saber cómo extraerlos de sitios web.

El web scraping es el proceso de extraer y recopilar datos de sitios web y almacenarlos en una máquina local o en una base de datos.

En esta sección usaremos los paquetes requests y BeautifulSoup (versión 4).

"""

# Para empezar necesitas requests,beautifulsoup4 y un sitio web:  ---  https://archive.ics.uci.edu/dataset/53/iris.php
import json

import requests
from bs4 import BeautifulSoup

url_scrap = "https://archive.ics.uci.edu/dataset/53/iris.php"
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

    contenido = resp.content  # obtenemos todo el contenido del sitio
    soup = BeautifulSoup(
        contenido, "html.parser"
    )  # BeautifulSoup nos permite parsear el HTML
    print(soup.title)  # <title>UCI Machine Learning Repository: Data Sets</title>
    if soup.title:
        print(soup.title.get_text())  # UCI Machine Learning Repository: Data Sets
    else:
        print("No se pudo obtener el título de la página")
        raise Exception("No se pudo obtener el título de la página")

    # print(soup.body)  # muestra el cuerpoypo de la página


except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Error de conexión: {e}")
except requests.exceptions.Timeout as e:
    print(f"Tiempo de espera agotado: {e}")
except Exception as e:
    print(e)


try:
    tablas = soup.find_all("table")
    print(f"-- Se encontraron {len(tablas)} tablas ------------------------------")
    tabla = tablas[0]  # el resultado es una lista; tomamos el primer elemento

    # buscar las cabeceras de las tablas y las guardamos en una array
    t_head = tabla.find("thead")
    if t_head:
        # print("Las cabeceras de la tabla ------------------------------------")
        t_row = t_head.find("tr")
        cabeceras = []
        if t_row:
            for t_d in t_row.find_all("th"):
                cabeceras.append(t_d.text.strip())
                # print("\n", t_d.text)
        # print(cabeceras)
    #
    # Extraer el pay-load de esa tabla de modo ordenado
    t_body = tabla.find("tbody")
    if t_body:
        print("Aqui vienen los datos de la tabla ----------------------------")
        lista_final_objetos = []  # Aquí guardaremos todos los diccionarios
        for t_fila in t_body.find_all("tr"):
            # Creamos una lista vacía para guardar los datos de ESTA fila
            fila_objeto = {}
            # Recorremos las celdas, extraemos los datos y los guardamos en el diccionario
            t_datos = t_fila.find_all("td")
            for i, t_celda in enumerate(t_datos):
                # Verificamos que exista una cabecera para este índice
                if i < len(cabeceras):
                    clave = cabeceras[i]
                    valor = t_celda.text.strip()

                    # Añadimos el par clave-valor al diccionario
                    fila_objeto[clave] = valor

            # Si el diccionario tiene datos, lo añadimos a nuestra lista global
            if fila_objeto:
                lista_final_objetos.append(fila_objeto)
    # Suponiendo que 'lista_final_objetos' es la lista que llenamos en el paso anterior
    if lista_final_objetos:
        # 1. Convertir la lista de objetos a una cadena de texto JSON
        # indent=4 hace que el JSON sea legible para humanos (con saltos de línea y espacios)
        # ensure_ascii=False permite que se vean bien las tildes y la 'ñ'
        datos_json = json.dumps(lista_final_objetos, indent=4, ensure_ascii=False)

        # 2. Imprimir el resultado por consola
        print("\nPayload en formato JSON ----------------------------")
        print(datos_json)

    # Guarda los datos en un archivo físico .json
    with open("./web_scraping/datos_tabla.json", "w", encoding="utf-8") as archivo:
        archivo.write(datos_json)
        print("\nArchivo 'datos_tabla.json' guardado con éxito.")
except Exception as e:
    print(e)
