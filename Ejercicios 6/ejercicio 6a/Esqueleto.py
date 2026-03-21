from Mob import Mob
class Esqueleto(Mob):
    """Mob agresivo, suena '¡Rattle!', dispara flechas a distancia."""
    def hacer_sonido(self) -> str:
        return "¡Rattle!"
    def comportamiento(self) -> str:
        return "Agresivo"
    def moverse(self) -> str:
        return "Dispara flechas a distancia desde lejos"