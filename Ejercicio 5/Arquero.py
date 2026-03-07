from Personaje import Personaje
class Arquero(Personaje):
    def __init__(self, nombre, nivel, flechas):
        super().__init__(nombre,nivel)
        self.flechas=flechas

    def usar_habilidad(self):
        print(f"{self.nombre} usa su habilidad flecha venenosa para atacar al enemigo.") 
        print(f"Le quedan {self.flechas} flechas.")
        self.flechas -= 1
arquero1= Arquero ("aladino",30,10)
arquero1.usar_habilidad()
arquero1.usar_habilidad()
arquero1.usar_habilidad()
if arquero1.flechas == 0:
    print("No te quedan flechas, recarga para seguir atacando.")
print("le dio venenuuus al enemy!")