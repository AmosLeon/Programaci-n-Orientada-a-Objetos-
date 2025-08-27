# Importamos librerias necesarias
from abc import ABC, abstractmethod
import math

# Clase abstracta figura con metodo abstracto de area
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass    # Metodo sin implementacion que sera implementado en las subclases
    
    
# Subclase rectangulo que hereda de figura
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Implementacion del metodo area para rectangulo
    def area(self):
        return self.base * self.altura

# Subclase circulo que hereda de figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    # Implementacion del metodo area para circulo
    def area(self):
        return math.pi * (self.radio ** 2)
    
# Prueba de las clases 
figura1 = Rectangulo(5, 3)  # Base 5, Altura 3
figura2 = Circulo(4)    # Radio 4

# Mostramos el area de cada figura 
print(f"El area del rectangulo es: {figura1.area()}")
print(f"El area del circulo es: {figura2.area()}")