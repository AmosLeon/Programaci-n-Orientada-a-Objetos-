# Clase Cuenta Bancaria con encapsulamiento y validaciones
class CuentaBancaria:
    
    def __init__(self, titular: str, saldo: float):
        # Atributos privados
        self.__titular = titular
        self.__saldo = saldo

    # Getter para titular
    def get_titular(self):
        return self.__titular

    # Getter para saldo
    def get_saldo(self):
        return self.__saldo

    # Método para depositar dinero con validación
    def depositar(self, monto: float):
        if monto > 0:
            self.__saldo += monto

    # Método para retirar dinero con validación
    def retirar(self, monto: float):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto


# Crear un objeto de prueba
cuenta_1 = CuentaBancaria("Manuel Arevalo", 10)

# Probar operaciones
cuenta_1.depositar(50)
cuenta_1.depositar(-20)  # inválido, no hace nada
cuenta_1.retirar(30)
cuenta_1.retirar(100)    # inválido, no hace nada

# Mostrar solo los resultados finales
print("Titular:", cuenta_1.get_titular())
print("Saldo final:", cuenta_1.get_saldo())