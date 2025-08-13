# Equilatero 3 lados son iguales
# Isoceles 2 lados son iguales
# Escaleno ningun lado es igual

while True:
    try:
        # entrada de datos
        l1 = float(input("Ingrese el lado 1: ")) # obtener l1
        l2 = float(input("Ingrese el lado 2: ")) # obtener l2
        l3 = float(input("Ingrese el lado 3: ")) # obtener l3
        
        # verificar que las longitudes sean positivas
        if l1 > 0 and l2 > 0 and l3 > 0:
            
            # Comparar los lados
            if l1 == l2 and l1 == l3 and l2 == l3: # Equilatero
                print("Es un triangulo Equilatero")
            elif l1 == l2 or l1 == l3 or l2 == l3: # Isoceles
                print("Es un triangulo Isoceles")
            else:
                print("Es un triangulo Escaleno")
            
            break
        else:
            print("Los datos de un triangulo deben ser positivos")
    except:
        print("Ocurrio un error, favor ingresar datos numericos")
        