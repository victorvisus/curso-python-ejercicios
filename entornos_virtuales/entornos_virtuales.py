"""
Configurar un entorno virtual
Al comenzar un proyecto es recomendable usar un entorno virtual. Un entorno virtual nos permite crear un entorno aislado o independiente, evitando conflictos de dependencias entre proyectos. Si ejecutas pip freeze en la terminal verás todos los paquetes instalados en la máquina. Con virtualenv solo tendrás acceso a los paquetes instalados en ese entorno específico. Abre tu terminal e instala virtualenv:
"""


# pip install virtualenv

"""
Dentro de la carpeta 30DaysOfPython crea un directorio llamado flask_project.

Una vez instalado virtualenv, entra en la carpeta del proyecto y crea el entorno virtual:
"""
# Para Windows:
# python -m venv .venv

"""
A mí me gusta nombrar el entorno como venv, pero puedes elegir otro nombre. Usa ls (o dir en Windows) para comprobar que venv se creó:
"""
# ls

"""
Activa el entorno virtual desde la carpeta del proyecto:

En Windows la activación puede variar según PowerShell o Git Bash.
"""

# Para Windows PowerShell:
# venv\Scripts\activate


# Para Windows Git Bash:
# venv\Scripts\. activate

"""
Tras ejecutar el comando de activación,el prompt mostrará el nombre del entorno (venv) al inicio.Ejemplo:
"""
# (venv) user@host:~/Desktop/30DaysOfPython/flask_project$

"""
Ahora,si ejecutas pip freeze no verás los paquetes globales;solo los del entorno.Instalemos Flask para este proyecto:
"""
# pip install Flask

"""
Después,comprobemos los paquetes instalados:
"""
# pip freeze

"""
Cuando termines,ejecuta deactivate para salir del entorno activo:
"""
# deactivate
