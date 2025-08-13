while True:
    try:
        # Solicita al usuario los dos límites
        a = int(input("Límite inferior: "))
        b = int(input("Límite superior: "))

        # Verifica si los números son iguales
        if a == b:
            print("Por favor, ingrese dos números diferentes.\n")
            continue  # Vuelve a pedir los números

        # Verifica si alguno de los números es impar
        elif a % 2 != 0 or b % 2 != 0:
            print("Por favor, ingrese solo números pares.\n")
            continue  # Vuelve a pedir los números

        else:
            # Si el límite inferior es mayor que el superior, los intercambia
            if a > b:
                a, b = b, a  # Intercambia los valores si es necesario

            # Imprime los números pares en el rango
            for n in range(a, b + 1):
                if n % 2 == 0:
                    print(n)
            break  # Sale del bucle si todo está correcto

    except ValueError:
        # Si el usuario ingresa un valor no entero
        print("Debe ingresar números enteros válidos.")
        