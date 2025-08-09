lado1 = int(input("Ingrese el primer lado del triángulo: "))
lado2 = int(input("Ingrese el segundo lado del triángulo: "))
lado3 = int(input("Ingrese el tercer lado del triángulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
else:
    print("Los lados ingresados no forman un triángulo")