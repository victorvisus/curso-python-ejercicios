import os

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)


# Función de apoyo (basada en tu Ejercicio 2)
def obtener_datos_ign():
    url = "https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        tabla = soup.find("table")
        tbody = tabla.find("tbody") if tabla else None
        filas = tbody.find_all("tr") if tbody else []

        lista_sismos = []
        for fila in filas:
            cols = fila.find_all("td")
            if len(cols) >= 10:
                try:
                    # Extraemos magnitud y localización
                    mag_raw = cols[7].text.strip().split()[0].replace(",", ".")
                    magnitud = float(mag_raw)
                    loc = cols[9].text.strip()
                    fecha_hora = f"{cols[1].text.strip()} {cols[2].text.strip()}"

                    lista_sismos.append(
                        {
                            "localizacion": loc,
                            "fecha_hora": fecha_hora,
                            "magnitud": magnitud,
                        }
                    )
                except:
                    continue
        return lista_sismos
    except Exception as e:
        print(f"Error en scraping: {e}")
        return []


# --- ENDPOINT DE LA API ---


@app.route("/sismos/magnitud/2.6", methods=["GET"])
def get_sismos_especificos():
    """Retorna todos los sismos con magnitud exacta de 2.6"""
    todos_los_sismos = obtener_datos_ign()

    # Filtramos la lista para quedarnos solo con los de 2.6
    filtrados = [s for s in todos_los_sismos if s["magnitud"] == 2.6]

    # Devolvemos la respuesta en formato JSON
    return jsonify(
        {"count": len(filtrados), "resultado": filtrados, "status": "success"}
    )


if __name__ == "__main__":
    # usamos variables de entorno para despliegue
    # funciona tanto para producción como para desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=False)
    # con use_reloader=False para aplicar los cambios hay que reiniciar a mano el servidor
