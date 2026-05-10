from Jugador import Jugador
class Observador(Jugador):
    def __init__(self, nombre, numero_de_control, nivel,partidas_vistas=0):
        super().__init__(nombre, numero_de_control, nivel,)
        self.partidas_vistas = partidas_vistas

    def vistas(self):

        # Aumenta partidas vistas
        self.partidas_vistas += 1

        # Gana 5 puntos automáticamente
        self.ganar_puntos(5)

        print(f"{self.nombre} lleva {self.partidas_vistas} partidas vistas.")
    
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print(f"Partidas Vistas: {self.partidas_vistas}")
        