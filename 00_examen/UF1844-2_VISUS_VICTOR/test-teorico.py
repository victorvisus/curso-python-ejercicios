a = [1, 2, 3, 4]
print(a[1:3])


""" info = os.uname()
print("Sistema:", info.sysname)
print("Nombre:", info.nodename)
print("Versión Kernel:", info.release) """

import platform

info = platform.uname()
print("Sistema:", info.system)
print("Nombre:", info.node)
print("Versión:", info.release)
print("Arquitectura:", info.machine)
