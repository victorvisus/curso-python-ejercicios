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
