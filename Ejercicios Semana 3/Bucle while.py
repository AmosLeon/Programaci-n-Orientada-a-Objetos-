detener = False # Creando una variable booleana asignando el valor de False

while not detener: # Evaluamos la condicion utilizando el operador not para negar el valor por defecto (False)
    
    # Solicitamos al usuario si desea terminar el programa
    print("Desea detener el programa (Si/No)")
    
    # Almacena la respuesta del usuario en una variable
    respuesta = input(": ").lower()
    
    # Verificamos el resultado 
    if respuesta == "si":
        # La respuesta fue si entonces la variable detener se vuelve verdadera
        detener = True
    elif respuesta == "no":
        pass 
    else: 
        print("Favor ingresar una opcion valida")