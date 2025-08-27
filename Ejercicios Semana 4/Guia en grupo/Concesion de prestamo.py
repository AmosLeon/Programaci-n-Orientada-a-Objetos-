# Solicita el salario mensaual y los años trabajados
salario = float(input("Ingrese su salario mensual: "))
años = int(input("Ingrese los años trabajados: "))

# Verifica si el préstamo puede ser aprobado, si no, lo deniega
if salario > 30000 or años >= 2:
    print("Prestamo aprobado.")
else:
    print("Prestamo denegado.")