try:
    precio = int(input("Ingrese el precio del producto: $"))
    descuento = int(input("Ingrese el porcentaje de descuento: $"))  

    if precio < 0 or descuento < 0:
        print("Error: No se permiten valores negativos.")
    else:
        monto_descuento = (precio * descuento) / 100
        precio_final = precio - monto_descuento

        if precio >= 1000 and descuento >= 10:
            descuento_adicional = precio_final * 0.05
            precio_final -= descuento_adicional
            print(f"Se aplicó un descuento adicional del 5%: {descuento_adicional}")

        print(f"El precio final con descuento es: ${precio_final}")

except:
    print("Error: Debes ingresar un número válido")