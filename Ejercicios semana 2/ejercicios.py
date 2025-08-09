# # Crea un programa que solicite al usuario ingresar su edad.
# # Luego, comprueba si es mayor o igual a 18 años y muestra un mensaje
# # indicando si es apto para votar en las elecciones

# try:    
#     edad = int(input("Ingresa tu edad: "))

#     if edad >= 18:
#         print("Puedes votar en las elecciones")
#     else:
#         print("Lo siento no eres apto para votar en las elecciones")
# except:
#     print("Error debes ingresar un numero valido")


# # Escribe un programa que solciite al usuario ingresar un numero entero
# # Luego, verifica si el numero es par o impar y muestra un mensaje
# # indicando el resultado

# try:
#     while True: # bucle infinito
#         numero = int(input("Ingresa un numero entero positivo: "))    
        
#         if numero > 0:
#             if numero % 2 == 0:
#                 print(f"{numero} es par")
#             else:
#                 print(f"{numero} es impar") 
#             break           
#         else:
#             print("Favor ingrese un numero positivo")
    
# except:
#     print("Ocurrio un error")


# # Crea un programa que solcite al usuario ingresar una calificacion numerica (0 - 100)
# # Luego mostrar un mensaje indicando la clasificacion de la calificacion segun la
# # siguiente escala: A (90-100), B (80-89), C (70-79), D (60-69) F (0 - 59)

# try:
#     calificacion = int(input("Ingrese una calificacion del 0 al 100: "))
    
#     # validacion de los datos
#     if  0 <= calificacion <= 100: # calificacion > 0 and calificacion <= 100:
#         if 90 <= calificacion <= 100: # calificacion >= 90 and calificacion <= 100
#             print("Obtuviste una A")
#         elif 80 <= calificacion <= 89: # calificacion >= 80 and calificacion <= 89
#             print("Obtuviste una B")
#         elif 70 <= calificacion <= 79: # calificacion >= 70 and calificacion <= 79
#             print("Obtuviste una C")
#         elif 60 <= calificacion <= 69: # calificacion >= 60 and calificacion <= 60
#             print("Obtuviste una D")
#         else:
#             print("Obtuviste una F")
    
#     else:
#         print("El numero ingresado esta fuera del rango permitido")
    
# except:
#     print("Debe ingresar un numero entero")


# Desarrolla un programa que pida al usuario ingresar una contraseña.
# Si la contraseña ingresada es "secreto123", muestre un mensaje de "Acceso permitido"; de lo contrario, muestre un mensaje de "Acceso denegado".

password = input("Ingrese la contraseña: ")

if password == "secreto123":
    print("Acceso permitido")
else:
    print("Acceso denegado")