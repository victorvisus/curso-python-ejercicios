import random
import string
import sys

"""
Ejercicios: Nivel 1
1 Escribe una función que genere un random_user_id de seis caracteres/dígitos.
    print(random_user_id());
    '1ee33d'
2 Modifica la tarea anterior. Declara una función llamada user_id_gen_by_user. No acepta argumentos, pero pide dos entradas: una es la cantidad de caracteres por ID y la otra es cuántos IDs generar.
    print(user_id_gen_by_user()) # entrada del usuario: 5 5
    #salida:
    #kcsy2
    #SMFYb
    #bWmeq
    #ZXOYh
    #2Rgxf

    print(user_id_gen_by_user()) # 16 5
    #1GCSgPLMaBAVQZ26
    #YD7eFwNQKNs7qXaT
    #ycArC5yrRupyG00S
    #UbGxOFI7UXSWAyKN
    #dIV0SSUTgAdKwStr
3 Escribe una función llamada rgb_color_gen. Debe generar un color RGB (cada valor en el rango 0-255).
    print(rgb_color_gen())
    # rgb(125,244,255) - la salida debe estar en este formato
"""
"""
Ejercicios: Nivel 2
1 Escribe una función list_of_hexa_colors que devuelva una lista con cualquier cantidad de colores hexadecimales (seis dígitos hexadecimales después de #; el sistema hex usa 0-9 y a-f).
2 Escribe una función list_of_rgb_colors que devuelva una lista con cualquier cantidad de colores RGB.
3 Escribe una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o RGB.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""
"""
Ejercicios: Nivel 3
1 Llama a tu función shuffle_list, que recibe una lista y devuelve la lista mezclada.
2 Escribe una función que devuelva una lista de siete números aleatorios únicos en el rango 0-9.
"""


# 1 Escribe una función que genere un random_user_id de seis caracteres/dígitos.
def random_user_id(raiz):
    raiz = str(raiz)
    num = random.randint(
        1, 999999
    )  # hay que convertirlo a string para concatenar con la raíz
    user_id = raiz + str(num)
    return user_id


print("El ID de usuario es: ", random_user_id("usr_"))


# 2 Modifica la tarea anterior. Declara una función llamada user_id_gen_by_user. No acepta argumentos, pero pide dos entradas: una es la cantidad de caracteres por ID y la otra es cuántos IDs generar.
# programa para generar contraseñas: puede ser entre 5 y 10 caracteres
# pudiendo ser numeros o letras (mayusculas o inusculas)
# el usuario puede elegir la longitud entre 5 y 10, el paso se hace por terminal
def user_id_gen_by_user():

    pass


print(user_id_gen_by_user())  # entrada del usuario: 5 5


# programa para generar contraseñas: puede ser entre 5 y 10 caracteres
# pudiendo ser numeros o letras (mayusculas o inusculas)
# el usuario puede elegir la longitud entre 5 y 10, el paso se hace por terminal
def pass_gen_by_user():
    # numDig = int(input("Ingrese la cantidad de caracteres por ID (entre 5 y 10): "))
    # print("Longitud de la contraseña a generar {}".format(sys.argv[1]))
    pwd = ""
    listDig = (
        string.digits + string.ascii_letters
    )  # lista de caracteres a usar para generar la contraseña

    for i in range(int(sys.argv[1])):
        # pwd = pwd + random.choice(listDig)
        digito = random.randint(0, len(listDig) - 1)
        pwd = pwd + listDig[digito]
    return pwd


def pass_multi_gen_by_user():
    print("Cantidad de contraseñas a generar {}".format(sys.argv[2]))
    listPwd = []
    for i in range(int(sys.argv[2])):
        listPwd.append(pass_gen_by_user())
    return listPwd


print("las contraseñas son: ", pass_multi_gen_by_user())


# 3 Escribe una función llamada rgb_color_gen. Debe generar un color RGB (cada valor en el rango 0-255).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


print(rgb_color_gen())  # rgb(125,244,255) - la salida debe estar en este formato


# 4 Escribe una función list_of_hexa_colors que devuelva una lista con cualquier cantidad de colores hexadecimales (seis dígitos hexadecimales luego de #; el sistema hex usa 0-9 y a-f).
def list_of_hexa_colors():
    listHexa = string.digits + "abcdef"
    hexa = "#"

    for i in range(6):
        digito = random.randint(0, len(listHexa) - 1)
        hexa = hexa + listHexa[digito]
    return hexa


print(list_of_hexa_colors())
