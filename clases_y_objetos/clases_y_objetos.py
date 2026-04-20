# ver: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/Spanish/21_classes_and_objects_sp.md

# Crear una clase
class Persona:
    # contructor
    def __init__(
        self, firstname: str, lastname: str, age: int, country: str, city: str
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    # metodo de clase
    def person_info(self):
        return f"{self.firstname} {self.lastname} tiene {self.age} años. Vive en {self.city}, {self.country}."


print(Persona)

# Crear un Objeto Persona
p = Persona("Victor", "Perez", 25, "Finland", "Helsinki")
print(p.person_info())
