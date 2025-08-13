num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("Suma:", num1 + num2)
print("Diferencia:", num1 - num2)
print("Producto:", num1 * num2)
print("División:", num1 / num2)

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Ambos números son iguales")