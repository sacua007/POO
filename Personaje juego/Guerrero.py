from Personaje import Personaje
class Guerrero(Personaje):   #Se importa la clase padre
    def __init__(self, nombre, nivel, arma):
        super().__init__(nombre, nivel)
        self.arma = arma                    
    def usar_habilidad(self):
        print(f"{self.nombre} ataca con nievl: {self.nivel}. Procede a atacar con {self.arma}.")   

g1=Guerrero("goku",100,"espada")
g1.usar_habilidad()
print("k lokotee!")