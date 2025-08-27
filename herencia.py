# Creamos la clase padre 
class Vehiculo:
    
    # Declaramos los atributos de la clase
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Declarar los compportamientos de la clase (Metodos)
    def describir(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}"
    
    
# Craeamos nuestra subclase
class Coche(Vehiculo): # Aplicando herencia
    
    # Declaramos los atributos de la clase
    def __init__(self, marca:str, modelo:str, color:str, anio:int):
        super().__init__(marca, modelo)
        self.color = color
        self.anio = anio
        
    # declarar los compportamientos de la subclase (Metodos)
    def describir(self): # Aplicando polimorfismo
        print(super().describir() + f"\nColor: {self.color}\nAño: {self.anio}")


# Crear nustros objetos

coche_1 = Coche("Toyota", "Hillux", "Rojo", 2025)
coche_2 = Coche("Nissan", "Frontier", "Blanco", 2025)

# Mostrar la descripcion de cada coche
coche_1.describir()
print("--------------")
coche_2.describir()