from Mob import Mob
class Enderman(Mob):
    """Mob agresivo, suena '...Ssssss', teletransporta cerca del jugador."""
    def hacer_sonido(self) -> str:
        return "...Ssssss"
    def comportamiento(self) -> str:
        return "Agresivo"
    def moverse(self) -> str:
        return "Se teletransporta cerca del jugador para atacarlo"