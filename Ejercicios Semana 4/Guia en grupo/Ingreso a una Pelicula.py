# Solicita al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Si la edad es 18 o más, permite el ingreso sin más preguntas
if edad >= 18:
    print("Puedes ingresar a ver la pelicula.")
else:
    # Si es menor de 18, pregunta si viene con un adulto acompañante
    adulto_acompañante = input("Vienes con un adulto acompañante? (si/no): ").lower()
    # Si viene con acompañante, permite el ingreso
    if adulto_acompañante == "si":
        print("Puedes ingresar a ver la pelicula.")
    else:
        # Si no viene con acompañante, no permite el ingreso
        print("No tienes permitido ingresar a ver la pelicula.")