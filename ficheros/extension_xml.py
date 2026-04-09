"""
Archivos con extensión xml
XML es un lenguaje de marcado similar a HTML. Permite etiquetas personalizadas y se usa para datos estructurados. En Python hay varias librerías; aquí usamos xml.etree.ElementTree.
"""

import xml.etree.ElementTree as ET

datos = ET.parse("./files/xml_example.xml")
print(f"Tipo: {type(datos)}")

raiz = datos.getroot()
print(f"Nombre de la raiz: {raiz.tag}")

for hijo in raiz:
    print(hijo.tag, ":")
    if hijo.tag != "skills":
        print(hijo.text)
    else:
        for habilidad in hijo:
            print("\t", habilidad.text)

# TAREA: Sacar las tag de nivel 2
print("\nTAREA: Sacar las tag de nivel 2")
for hijo in raiz:
    if hijo.tag == "skills":
        for habilidad in hijo:
            print("\t", habilidad.text)

""" nodo_skills = raiz.findall(".//skills")
nodo_idiomas: list = raiz.findall(".//idioma")
for nodo in nodo_skills:
    print(nodo.text)
    if nodo.text == "Idiomas":
        for idioma in nodo_idiomas:
            print("\t", idioma.text)
 """


# Buscamos todos los nodos <skill> (que son los que contienen la info)
nodos_skill = raiz.findall(".//skill")

for nodo in nodos_skill:
    # Limpiamos el texto para quitar espacios y saltos de línea
    texto_skill = nodo.text.strip() if nodo.text else ""

    if texto_skill:
        print(texto_skill)

    # Si este nodo skill contiene idiomas, los buscamos dentro de él
    if "Idiomas" in texto_skill:
        idiomas = nodo.findall("idioma")
        for idioma in idiomas:
            print("\t-", idioma.text)
