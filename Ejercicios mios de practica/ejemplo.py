import math as mt

# Metodos con parametros opcionales 
def calcular_area_circulo(radio: float, pi: float = 3.1416): # Si no se envia el valor de PI por defecto sera 3.1416
    area = pi * mt.pow(radio, 2)
    return area

radio = 5
area_circulo = calcular_area_circulo(radio, 3.1415)
print(f"El area del circulo con radio {radio} es: {area_circulo}")

radio = 5
area_circulo = calcular_area_circulo(radio,)
print(f"El area del circulo con radio {radio} es: {area_circulo}")