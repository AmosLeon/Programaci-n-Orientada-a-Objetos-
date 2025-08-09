# Verificacion de numero par
try:
    numero = int(input("Ingresa un numero entero: "))
    
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
except ValueError:
    print("Error: Debes ingresar un numero entero valido")