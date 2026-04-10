from mypackage import arithmetics, greet

print(arithmetics.add_numbers(1, 2, 3, 5))
print(arithmetics.subtract(5, 3))
print(arithmetics.multiple(5, 3))
print(arithmetics.division(5, 3))
print(arithmetics.remainder(5, 3))
print(arithmetics.power(5, 3))
##
print(greet.greet_person("Juan", "Pérez"))


"""
Más información sobre paquetes
    - Python tiene paquetes y módulos incorporados; otros deben instalarse.
    - pip es la herramienta recomendada para instalar y gestionar paquetes desde PyPI.
    - Para capturar las dependencias de un proyecto usa pip freeze > requirements.txt.
    - Para desinstalar: pip uninstall packagename o pip uninstall -r requirements.txt.
    - Virtualenv (y venv) permiten crear entornos aislados:
        - Instalar virtualenv: pip install virtualenv
        - Crear entornos aislados evita conflictos entre proyectos.
"""
