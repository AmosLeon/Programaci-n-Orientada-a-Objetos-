# Crea un programna que solicite al usuario ingresar una calificación numerica (0 - 100).
# Luego mostrar un mensaje indicando la clasificación de la calificación segun la siguiente escala : A (90-100), B (80-89), C (70-79), D (60-69), F (0-59).

try:
    calificacion = int(input("Ingrese una calificación (0-100): "))
    
    # Validacion de los datos
    if 0 <= calificacion <= 100: # calificacion > 0 and calificacion <= 100:
        if 90 <= calificacion <= 100: # calificacion >= 90 and calificacion <= 100:
            print("Obtuviste una A")
        elif 80 <= calificacion < 89: # calificacion >= 80 and calificacion <= 89:
            print("Obtuviste una B")
        elif 70 <= calificacion < 79: # calificacion >= 70 and calificacion <= 79:
            print("Obtuviste una D")
        elif 60 <= calificacion < 69: # calificacion >= 60 and calificacion <= 69:
            print("Obtuviste una D")
        else:
            print("Obtuviste una F")
    else:
        print("El numero ingresado esta fuera del rango permitido")
    
except:
    print("Debe ingresar un número entero")