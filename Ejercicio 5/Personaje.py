class Personaje:
    def __init__(self, nombre, nivel): #define el contructor de la clase Personaje, que recibe dos parámetros: nombre y nivel. Estos parámetros se asignan a los atributos de instancia self.nombre y self.nivel.
        self.nombre = nombre
        self.nivel = nivel

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo nivel {self.nivel}.")  
    
    def usar_habilidad(self):
        print(f"{self.nombre} ataca con magia chocarrera.")
    
