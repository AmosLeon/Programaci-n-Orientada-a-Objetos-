while True:
    try:
        # Entrada de datos
        lado1 = float(input("Ingrese el primer lado del triángulo: "))
        lado2 = float(input("Ingrese el segundo lado del triángulo: "))
        lado3 = float(input("Ingrese el tercer lado del triángulo: "))

        # Validar que los lados sean positivos
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            print("Los lados de un triángulo deben ser positivos.\n")
            continue

        # Verificar desigualdad triangular
        if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
            # Clasificación
            if lado1 == lado2 == lado3:
                print("El triángulo es equilátero")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("El triángulo es isósceles")
            else:
                print("El triángulo es escaleno")
            break  # Salir del ciclo si todo está correcto
        else:
            print("Los lados ingresados NO forman un triángulo.\n")

    except ValueError:
        print("Error: Ingrese solo valores numéricos.\n")
