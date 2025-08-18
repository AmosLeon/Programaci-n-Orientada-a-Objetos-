
# Crear una clase
class Circulo:

    # Crear un constructor y agregar los atributos
    def __init__(self, radio:float):
        self.radio = radio

    # Crear los metodos (comportamiento del objeto)

    # Creo el metodo para calcular el area
    def calcular_area_circulo(self):
        # Area = pi * radio^2
        area = 3.1416 * (self.radio * self.radio)
        return area

    # Creo el metodo para calcular la circunferencia
    def calcular_circunferencia_circulo(self):
        # Circunferencia = 2 * pi * radio
        circunferencia = 2 * 3.1416 * self.radio
        return circunferencia

# self es una palabra contextual en una clase en python 
# que nos ayuda a obtener los atributos de la clase 
# y utilizarlos en los metodos de la misma.

# Crear un objeto - instancia de mi clase
circulo_1 = Circulo(2)
print(circulo_1.calcular_area_circulo())
print(circulo_1.calcular_circunferencia_circulo())

circulo_2 = Circulo(7)
print(circulo_2.calcular_area_circulo())
print(circulo_2.calcular_circunferencia_circulo())

circulo_3 = Circulo(10)
print(circulo_3.calcular_area_circulo())
print(circulo_3.calcular_circunferencia_circulo())