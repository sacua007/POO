#Clase padre
class Jugador:
    def __init__(self,nombre, numero_de_control, nivel,puntos=0 ):
        self.nombre = nombre
        self.numero_de_control = numero_de_control
        self.nivel = nivel
        self.puntos = puntos
    
    def ganar_puntos(self, puntos_ganados):
        self.puntos += puntos_ganados
    
    def perder_puntos(self, puntos_perdidos):
        self.puntos -= puntos_perdidos      
    
    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Control: {self.numero_de_control}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos: {self.puntos}")