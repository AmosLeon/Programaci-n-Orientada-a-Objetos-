# crear la clase 'Cuenta Bancaria'
class CuentaBancaria:
    
    # Definir los atributos
    def __init__(self, titular:str, saldo:float):
        # Inicializar nuestros atributos
        self.titular = titular
        self.saldo = saldo

    # Crear nuestros metodos
    def deposito(self, monto:float): # monto, cantidad, deposito
        self.saldo += monto

    def retiro(self, monto:float): # monto, cantidad, retiro
        self.saldo -= monto


# Crear un objeto cuenta_1

cuenta_1 = CuentaBancaria("Manuel Arevalo", 10)

# Ocupar nuestro metodo depositar
cuenta_1.deposito(50)
cuenta_1.deposito(50)

# Ocupar nuestro metodo retirar
cuenta_1.retiro(100)

# Mostramos el saldo de la cuenta
print(cuenta_1.saldo)