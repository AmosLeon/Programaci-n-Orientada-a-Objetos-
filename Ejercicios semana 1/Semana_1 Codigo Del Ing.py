def menu():
    continuar = True
    
    while continuar:
        print("=== Bienvenidos a los Ejercicios de la Semana 1 ===")
        print("Elija un ejercicio a resolver")
        print("1. Ejercicio 1\n2. Ejercicio 2\n0. Salir")
        
        opcion = int(input())
        
        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 0:
            print("=== Hasta luego ====")
            continuar = False
        else:
            print("La opcion ingresa es invalida.")

def ejercicio_1(): # () aca indicamos que la funcion no recibe ningun parametro
    #Escribe un programa en Python que declare 
    #tres variables: nombre (texto), edad (entero), y estatura (decimal). 
    # Luego imprime sus valores en pantalla.
    
    nombre = "Francisco"
    edad = 26
    estatura = 1.71
    
    print(f"Nombre: {nombre}\nEdad: {edad}\nEstatura: {estatura}")

def ejercicio_2():
    #Declara dos números y muestra en pantalla:
    #Su suma, Su diferencia, Su producto, Su división, ¿Cuál es mayor?
    num1, num2 = 10, 0
    
    print(f"La suma es: {num1 + num2}")
    print(f"La diferencia es: {num1 - num2}")
    print(f"El producto es: {num1 * num2}")
    
    if num2 != 0:
        print(f"La división es: {num1 / num2}")     
    else:
        print("La division entre cero no existe.")  
    
    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num1 < num2:
        print(f"{num2} es mayor que {num1}")
    else:
        print("Ambos numeros son iguales")
    

if __name__ == "__main__":
    menu()
    
    
    
    
# Funciones

# 1. funcion que no recibe ningun valor y no retorna un resultado
def mostrar_mensaje():
    print("Hola mundo desde python")
    
# 2. funcion que recibe uno o mas valores como parametros y no retorna un resultado
def mostrar_mensaje_dinamico(nombre, carrera): # francisco, Ingeniera en Sistemas
    print(f"Bivenido {nombre} a la carrera de {carrera} ")
    
# 3. funcion que no recibe ningun valor y devuelve un resultado
def devolver_valor_PI():
    return 3.1416

# 4. funcion que recibe un valor y devuelve un resultado
def calcular_area(base, altura):
    return base * altura


