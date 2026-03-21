from Herramienta import Herramienta

class Arco(Herramienta):
    @property
    def nombre(self) -> str:
        return "Arco"

    def usar(self, objetivo: str) -> str:
        if self.rota:
            return f"El {self.nombre} de {self._material} está roto y no puede usarse."
        if self.flechas <= 0:
            return f"No tienes flechas para usar el {self.nombre} de {self._material}."
        
        self.desgastar()
        self.flechas -= 1
        daño = self.calcular_daño()
        return f"Disparaste una flecha al {objetivo} causando {daño} de daño. Flechas restantes: {self.flechas}"