from Herramienta import Herramienta
class Pala(Herramienta):
    """Clase concreta para la Pala."""

    @property
    def nombre(self) -> str:
        return "Pala"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"¡La {self.nombre} de {self._material} está rota! No puedes usarla."
        
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usaste la {self.nombre} de {self._material} para cavar en {objetivo}, causando {daño} de daño."
