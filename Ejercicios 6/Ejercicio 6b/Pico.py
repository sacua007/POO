from Herramienta import Herramienta 
class Pico(Herramienta):
    """Clase concreta para el Pico."""

    @property
    def nombre(self) -> str:
        return "Pico"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"¡El {self.nombre} de {self._material} está roto! No puedes usarlo."
        
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usaste el {self.nombre} de {self._material} para extraer {objetivo}, causando {daño} de daño."
    
    