class Persona:
    nombre:str
    apellido:str
    edad:int
    direcciones:str
    telefono:str

    def __init__(self, nombre, apellido, edad, direcciones, telefono):
        pass


personas = []

for i in range(1, 100):
    personas.append(Persona("Juan Miguel" + str(i), "Cortez" + str(i), i, "San Salvador" + str(i), "123" + str(i)))


# juan = Persona("Juan Miguel", 30, "San Salvador", "123")

# juan.nombre = "Juan Miguel"
# juan.apellido = "Cortez"