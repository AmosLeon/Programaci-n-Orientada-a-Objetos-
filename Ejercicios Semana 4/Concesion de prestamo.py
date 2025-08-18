salario = float(input("Ingrese su salario mensual: "))
años = int(input("Ingrese los años trabajados: "))

if salario > 30000 or años >= 2:
    print("Prestamo aprobado.")
else:
    print("Prestamo denegado.")