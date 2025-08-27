# crear nuestra clase padre utilizando un tipo de clase abstracta

# importamos ABC y abstractmethod del modulo abc de Python
from abc import ABC, abstractmethod 

# crear la clase abstracta Animal
class Animal(ABC):
    
    # atributos
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    @abstractmethod 
    def hacer_sonido(self):
        pass

    @abstractmethod
    def comer(self):
        pass

# crear las subclases
class Perro(Animal):

    # atributos
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)
        
    # implementando el metodo abstracto hacer_sonido
    def hacer_sonido(self):
        print(f"El perro {self.nombre} dice guau")

    def comer(self):
        print(f"El perro {self.nombre} esta comiendo.")


class Gato(Animal):

     # atributos
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)

    # implementando el metodo abstracto hacer_sonido
    def hacer_sonido(self):
        print(f"El gato {self.nombre} dice miau")

    def comer(self):
        print(f"El gato {self.nombre} esta comiendo.")

class Pajaro(Animal):

    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)

    # implementando el metodo abstracto hacer_sonido
    def hacer_sonido(self):
        print(f"El pajaro {self.nombre} dice cucu cucu")

    def comer(self):
        print(f"El pajaro {self.nombre} esta comiendo.")

    def volar(self):
        print(f"El pajaro {self.nombre} esta volando.")

# Crear nuestros objetos 

perro_1 = Perro("Paco", 3, "Macho")
gato_1 = Gato("Pancho", 2, "Macho")

# interactuar con los metodos
# perro_1.comer()
print()
gato_1.comer()
print()
perro_1.hacer_sonido()
print()
gato_1.hacer_sonido()

# Instanciar la clase padre 
animal = Animal("firulais", 5, "Macho")
# animal.comer()