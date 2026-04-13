"""
Ejercicios: Nivel 2
1 Escribe un patrón que valide un nombre de variable válido en Python.
2 Limpia el siguiente texto eliminando etiquetas HTML.
"""

import re

text = """
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
"""

"""
Ejercicios: Nivel 3
Limpia el siguiente texto y, tras limpiarlo, calcula las tres palabras más frecuentes:
"""
paragraph = """I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."""

"""
El siguiente texto contiene varias direcciones de correo electrónico. Escribe un patrón que encuentre o extraiga las direcciones de email válidas:
"""
email_address = """
asabeneh@gmail.com
alex@yahoo.com
kofi@yahoo.com
doe@arc.gov
asabeneh.com
asabeneh@gmail
alex@yahoo
"""


# 1 Escribe un patrón que valide un nombre de variable válido en Python.
def validarNombreVariable(nom):
    patron = r"^[a-zA-Z_$][a-zA-Z0-9_$]*$"
    coincidencia = re.match(patron, nom)

    if coincidencia is not None:
        return True
    return False


nombresVariables = [
    "nombre",
    "_nombre",
    "nombre_completo",
    "edad25",
    "vari_able",
    "variable10",
    "mensaje",
    "edad",
    "a",
    "b",
    "c",
    "x",
    "y",
    "z",
    "nombre_usuario",
    "edad_usuario",
    "peso",
    "altura",
    "datos_aux",
    "lista_aux",
    "2_variable",
    "var-iable",
    "var iable",
    "if",
    "for",
    "while",
    "True",
    "False",
    "None",
    "id",
]
palabras = [
    "if",
    "for",
    "while",
    "True",
    "False",
    "None",
    "id",
]
for i, item in enumerate(nombresVariables):
    print("Nombre de variable: ", item, " - ", validarNombreVariable(item))
