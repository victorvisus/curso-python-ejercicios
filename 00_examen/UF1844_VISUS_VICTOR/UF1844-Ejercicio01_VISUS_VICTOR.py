# Para el binario 100111, el cálculo es 1*2^5 + 0*2^4 + 0*2^3 + 1*2^2 + 1*2^1 + 1*2^0 = 32+0+0+4+2+1=39.

"""
Convierte un número binario a decimal.
Parámetros:
numBinario (str): número binario a convertir.
Returns:
int: número decimal correspondiente al resultado de convertir el número binario a decimal.
Ejemplo:
binary_to_decimal("100111") -> 39
"""


def conversorBinarioDecimal(numBinario):
    resultado = 0
    for i in range(len(numBinario)):
        resultado += int(numBinario[i]) * (2 ** (len(numBinario) - 1 - i))
    return resultado

    # print(binary_to_decimal("1101"))


"""
Solicita datos al usuario, y evalua que sea un número binario, si no es binario lanza un error.
Returns: string: número binario introducido por el usuario
"""


def solicitaDatos():
    numero = input("Introduce un número binario: ")

    for i in range(len(numero)):
        if numero[i] != "0" and numero[i] != "1":
            raise ValueError
        else:
            return numero


"""
El metodo principal del ejercicio
mientras que el usuario no introduzca un numero binario, sigue solicitandole que intruduzca el dato
Imprime el resultado en consola
"""


def appIni():
    flag = True
    while flag:
        try:
            print(
                f"El numero en decimal es: {conversorBinarioDecimal(solicitaDatos())}"
            )
            flag = False
        except ValueError:
            print("El número introducido no es binario")


# Ejecuta el ejercicio
appIni()
