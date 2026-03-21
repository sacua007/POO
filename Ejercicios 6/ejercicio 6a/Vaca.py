from Mob import Mob

class Vaca(Mob):
    """Mob pasivo, suena 'Muuuu', camina lento."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    

    def hacer_sonido(self) -> str:
        return "Muuuu"
    def comportamiento(self) -> str:
        return "Pasivo"
    def moverse(self) -> str:
        return "Camina lentamente por la calle"
    
