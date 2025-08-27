# Definimos la clase CuentaBancaria con encansulamiento del sal,do 
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Saldo privado
        
    # Metodo para depositar dinero en la cuenta, validando que el monto sea positivo
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto a depositar debe ser positivo.")
    
    # Metodo para retirar dinero, validando que no exceda el saldo disponible
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes para el retiro.")
            
    # Metodo para mostrar el saldo actual
    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.__saldo}")
        
# Prueba del funcionamiento de la clase
cuenta = CuentaBancaria("Amos", 100)    # Saldo inicial 

cuenta.mostrar_saldo()
cuenta.depositar(50)    # Deposito valido

cuenta.retirar(30)   # Retiro valido
cuenta.retirar(150)  # Retiro invalido, fondos insuficientes