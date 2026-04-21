"""
Ejercicio 2: Web Scraping de terremotos del IGN
Extrae datos de la página de últimos terremotos del IGN y crea una lista de diccionarios
con Localización, fecha y hora UTC (datetime), y magnitud (float).
"""

from datetime import datetime
from typing import Any, Dict, List

import requests
from bs4 import BeautifulSoup


def obtener_terremotos_ign() -> List[Dict[str, Any]]:
    """
    Extrae los datos de terremotos de los últimos 30 días desde la página del IGN.

    Returns:
        Lista de diccionarios con claves:
        - Localización (str): ubicación del sismo
        - fecha_y_hora_utc (datetime): fecha y hora del sismo en UTC
        - magnitud (float): magnitud del sismo
    """
    url = "https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias"

    try:
        # Hacer petición HTTP
        print(f"Realizando petición a: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"Petición exitosa. Código de estado: {response.status_code}")

        # Parsear HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Encontrar la tabla de terremotos
        # Buscar la tabla que contiene los datos
        tabla = soup.find("table")
        if not tabla:
            print("No se encontró tabla en la página")
            return []

        terremotos = []

        # Procesar filas de la tabla (saltar encabezado)
        filas = tabla.find_all("tr")[1:]  # Saltar la fila de encabezado

        print(f"Se encontraron {len(filas)} registros de terremotos")

        for idx, fila in enumerate(filas, 1):
            try:
                celdas = fila.find_all("td")

                if len(celdas) < 11:  # Asegurar que hay suficientes columnas
                    continue

                # Extraer datos según la estructura de la tabla
                # Evento: celdas[0]
                fecha_str = celdas[1].text.strip()  # Fecha (DD/MM/YYYY)
                hora_utc_str = celdas[2].text.strip()  # Hora UTC (HH:MM:SS)
                # Saltar celdas intermedias (Hora Local, Latitud, Longitud, Profundidad)
                magnitud_str = celdas[7].text.strip()  # Magnitud
                # Saltar Tipo Mag, Int. max
                localizacion = celdas[10].text.strip()  # Localización

                # Validar y procesar datos
                if (
                    not fecha_str
                    or not hora_utc_str
                    or not magnitud_str
                    or not localizacion
                ):
                    continue

                try:
                    # Combinar fecha y hora UTC en un datetime
                    fecha_hora_utc = datetime.strptime(
                        f"{fecha_str} {hora_utc_str}", "%d/%m/%Y %H:%M:%S"
                    )

                    # Convertir magnitud a float
                    magnitud = float(magnitud_str)

                    # Crear diccionario con los datos
                    sismo = {
                        "Localización": localizacion,
                        "fecha_y_hora_utc": fecha_hora_utc,
                        "magnitud": magnitud,
                    }

                    terremotos.append(sismo)

                except (ValueError, IndexError) as e:
                    print(f"Error procesando fila {idx}: {e}")
                    continue

            except IndexError as e:
                print(f"Error extrayendo celdas de fila {idx}: {e}")
                continue

        print(f"\nTotal de terremotos procesados exitosamente: {len(terremotos)}")
        return terremotos

    except requests.RequestException as e:
        print(f"Error en la petición HTTP: {e}")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []


def mostrar_terremotos(terremotos: List[Dict[str, Any]]) -> None:
    """
    Muestra los terremotos de forma formateada.

    Args:
        terremotos: Lista de diccionarios con datos de terremotos
    """
    if not terremotos:
        print("No hay terremotos para mostrar")
        return

    print("\n" + "=" * 100)
    print("TERREMOTOS DE LOS ÚLTIMOS 30 DÍAS (IGN)")
    print("=" * 100)

    for idx, sismo in enumerate(terremotos, 1):
        print(f"\n{idx}. Localización: {sismo['Localización']}")
        print(
            f"   Fecha y Hora UTC: {sismo['fecha_y_hora_utc'].strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"   Magnitud: {sismo['magnitud']}")


def main():
    """Función principal para probar la captación, extracción y construcción."""

    print("Iniciando web scraping de terremotos del IGN...")
    print("-" * 100)

    # Obtener datos de terremotos
    terremotos = obtener_terremotos_ign()

    # Mostrar resultados
    if terremotos:
        mostrar_terremotos(terremotos)

        # Mostrar estadísticas
        print("\n" + "=" * 100)
        print("ESTADÍSTICAS")
        print("=" * 100)
        print(f"Total de terremotos: {len(terremotos)}")

        magnitudes = [t["magnitud"] for t in terremotos]
        print(f"Magnitud mínima: {min(magnitudes)}")
        print(f"Magnitud máxima: {max(magnitudes)}")
        print(f"Magnitud promedio: {sum(magnitudes) / len(magnitudes):.2f}")

        # Mostrar primeros 5 en formato de lista de diccionarios
        print("\n" + "=" * 100)
        print("PRIMEROS 5 TERREMOTOS (Formato lista de diccionarios)")
        print("=" * 100)
        for sismo in terremotos[:5]:
            print(f"\n{sismo}")
    else:
        print("No se pudieron obtener los datos de terremotos")


if __name__ == "__main__":
    main()
