while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        
        if not numero > 0:
            print("Favor ingresar un valor positivo")
        else:
            
            while numero > 0:
                print(numero)
                numero -= 1
            break
        
    except:
        print("Ocurrio un error, favor ingresar un número entero positivo")
        