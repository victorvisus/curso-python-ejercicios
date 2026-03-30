"""
Obtener caracteres por índice. Como un Array
En programación la indexación comienza en cero. Por tanto, la primera letra está en el índice 0 y la última en la longitud de la cadena menos uno.
"""

language = "Python"
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

"""
Slicing de cadenas
En Python podemos obtener subcadenas mediante slicing.
"""
language = "Python"
first_three = language[0:3]  # empieza en índice 0, hasta 3 pero sin incluir 3
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)  # hon
# Otra forma
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon

"""
Invertir cadenas
Podemos invertir fácilmente una cadena.
"""
greeting = "Hello, World!"
print(greeting[::-1])  # !dlroW ,olleH

"""
Saltar caracteres al hacer slicing
Al pasar un parámetro de paso en slicing podemos omitir caracteres al extraer subcadenas.
"""
language = "Python"
pto = language[0:6:2]  #
print(pto)  # Pto


"""
Metodos interesantes
"""
# count(): devuelve el número de ocurrencias de una subcadena: count(subcadena, start=.., end=..). start y end definen el rango de conteo.
challenge = "thirty days of python"
print(challenge.count("y"))  # 3
print(challenge.count("y", 7, 14))  # 1, cuenta entre índices 7 y 14
print(challenge.count("th"))  # 2


# find(): devuelve el índice de la primera aparición de una subcadena; si no se encuentra devuelve -1
challenge = "thirty days of python"
print(challenge.find("y"))  # 5
print(challenge.find("th"))  # 0

# rfind(): devuelve el índice de la última aparición de una subcadena; si no se encuentra devuelve -1
challenge = "thirty days of python"
print(challenge.rfind("y"))  # 16
print(challenge.rfind("th"))  # 17

# index(): devuelve el índice de la primera aparición de una subcadena; acepta parámetros de inicio y fin (por defecto 0 y longitud de la cadena). Si la subcadena no se encuentra, lanza ValueError.
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9))  # error

# rindex(): devuelve el índice de la última aparición de una subcadena; acepta parámetros de inicio y fin (por defecto 0 y longitud de la cadena).
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9))  # error

# islower(): determina si todas las letras de la cadena están en minúsculas
challenge = "thirty days of python"
print(challenge.islower())  # True
challenge = "Thirty days of python"
print(challenge.islower())  # False

# isupper(): determina si todas las letras de la cadena están en mayúsculas
challenge = "thirty days of python"
print(challenge.isupper())  #  False
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())  # True

# join(): devuelve la cadena resultante tras unir los elementos
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = " ".join(web_tech)
print(result)  # 'HTML CSS JavaScript React' (devuelve la cadena unida)

web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = "# ".join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): elimina los caracteres dados del inicio y del final de la cadena
challenge = "thirty days of python"
print(
    challenge.strip("noth")
)  # 'irty days of py' (elimina los caracteres dados del inicio y final)

# replace(): reemplaza una subcadena por otra dada
challenge = "thirty days of python"
print(challenge.replace("python", "coding"))  # 'thirty days of coding'

# split(): divide una cadena usando un separador dado o espacios
challenge = "thirty days of python"
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = "thirty, days, of, python"
print(challenge.split(", "))  # ['thirty', 'days', 'of', 'python']

# startswith(): determina si la cadena comienza con la subcadena especificada
challenge = "thirty days of python"
print(challenge.startswith("thirty"))  # True

# endswith(): determina si la cadena termina con la subcadena dada; devuelve True o False
challenge = "thirty days of python"
print(challenge.endswith("on"))  # True
print(challenge.endswith("tion"))  # False (no termina con 'tion')

challenge = "30 days of python"
print(challenge.startswith("thirty"))  # False (no empieza con 'thirty')

# otros: isalnum(); isalpha(); isdecimal(); isdigit(); isnumeric(); title(); swapcase()
