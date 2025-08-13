# Crear un bucle para validar la entrada de datos y utilizar un try-except para manejar errores
numero_secreto = 7
# Crear un contador para saber cuantos intentos me tarde
intentos = 1

while True:
    try:
        # Solicitar al usuario que ingrese un numero entre el 1 y el 10
        numero = int(input("Ingrese un numero entre el 1 y el 10: "))
        
        # Validar que el numero se encuentre en el rango solicitado
        if 1 <= numero <= 10: # Numero >= 1 and numero <= 10
            
            # Verificar si el numero es igual al numero secreto
            if numero == numero_secreto:
                print(f"Felicidades, encontraste el numero.\nIntentos: {intentos}")
                break
            else: 
                print("Ups fallaste, vuelve a intentarlo")
        else:
            print("Favor ingresar un numero entre 1 y 10")

    except:
        print("Ocurrio un error, favor ingresar un valor numerico")
    finally:
        intentos += 1
        