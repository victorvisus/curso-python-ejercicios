import webbrowser  # módulo para abrir sitios web

# lista de URLs de ejemplo
url_lists = [
    "http://www.python.org",
    "https://www.linkedin.com/in/asabeneh/",
    "https://github.com/Asabeneh",
    "https://twitter.com/Asabeneh",
]

# abrir cada URL en una nueva pestaña
for url in url_lists:
    webbrowser.open_new_tab(url)


# Desinstalar paquetes: pip uninstall packagename
# Lista de paquetes: pip list
# Mostrar información del paquete: pip show packagename
# Actualizar paquetes: pip install --upgrade packagename
# PIP Freeze, Genera una lista de paquetes instalados y sus versiones (útil para requirements.txt): pip freeze
"""
Desinstalar paquetes
Para eliminar un paquete instalado:

pip uninstall packagename
"""
"""
Lista de paquetes
Para listar los paquetes instalados en tu entorno:

pip list
"""
"""
Mostrar información del paquete
Para ver información de un paquete:

pip show nombre_de_paquete
"""
"""
PIP Freeze
Genera una lista de paquetes instalados y sus versiones (útil para requirements.txt):

pip freeze
"""
