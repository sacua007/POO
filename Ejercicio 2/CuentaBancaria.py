class cuentaBancaria:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        print(f"Se ingresan {cantidad} a la cuenta de {self.titular}")
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad 

cuentq1= cuentaBancaria("makuin", 1000)
cuentq1.mostrar()
cuentq1.ingresar(500)
cuentq1.mostrar()