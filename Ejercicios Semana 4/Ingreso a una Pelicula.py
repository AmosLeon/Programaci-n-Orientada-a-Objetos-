edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Puedes ingresar a ver la pelicula.")
else:
    adulto_acompañante = input("Vienes con un adulto acompañante? (si/no): ").lower()
    if adulto_acompañante == "si":
        print("Puedes ingresar a ver la pelicula.")
    else:
        print("No tienes permitido ingresar a ver la pelicula.")