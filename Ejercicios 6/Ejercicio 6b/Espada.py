from Herramienta import Herramienta
class Espada(Herramienta):
    """Clase concreta para la Espada."""

    @property
    def nombre(self) -> str:
        return "Espada"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"¡La {self.nombre} de {self._material} está rota! No puedes usarla."
        
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usaste la {self.nombre} de {self._material} para atacar a {objetivo}, causando {daño} de daño."