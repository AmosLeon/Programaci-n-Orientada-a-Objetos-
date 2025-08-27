# Definimos la clase persona con atributos nombre y edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodo para mostrar los datos de la persona
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        
    # Metodo para verificar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

# Creamos dos instancias, una mayor y otra menor de edad
persona1 = Persona("Amos", 18)
persona2 = Persona("Luis", 16)

# Mostramos los datos y verificamos si son mayores de edad
persona1.mostrar_datos()
persona1.es_mayor_de_edad()

persona2.mostrar_datos()
persona2.es_mayor_de_edad()