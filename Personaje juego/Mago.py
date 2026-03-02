from Personaje import Personaje
class Mago(Personaje): #se importa personaje
    def __init__(self, nombre, nivel, hechizo):    
        super().__init__(nombre,nivel)
        self.hechizo=hechizo

    def usar_habilidad(self):
        print(f"{self.nombre} usa el hechizo {self.hechizo} para ganar experiencia lo que sube a nivel {self.nivel}")
    
mago1= Mago("makuin",40,"recuperacion")
mago1.usar_habilidad()
print("kalajooooo!")