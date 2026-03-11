class Mascota:
    def __init__(self, nombre, animal, color):
        self.nombre = nombre
        self.animal = animal
        self.color = color
    def mostrar(self):
        print(f"mi mascota se llama: {self.nombre}, es un: {self.animal}, de color {self.color}")
    
    def accion(self, accion):
        print(f"mi mascota {self.nombre} esta {accion}")

mascota1 = Mascota("firulais", "perro", "marron") 
mascota1.mostrar() 
mascota1.accion("ladrando")     


mascota2 = Mascota("michi", "gato", "negro")
mascota2.mostrar()
mascota2.accion("ronroneando")