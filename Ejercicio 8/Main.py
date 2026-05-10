from Competidor import Competidor
from Observador import Observador
 
# Crear un competidor
competidor1 = Competidor(
    nombre="Juan Pérez",
    numero_de_control="12345",
    nivel="Avanzado",
    equipo="AlfaBetaDinamita",)

# Crear un observador
observador1 = Observador(
    nombre="María García",
    numero_de_control="67890",
    nivel="Intermedio",
    )

# Mostrar perfiles
print("Perfil del Competidor:")
competidor1.mostrar_perfil()

print("\nPerfil del Observador:")   
observador1.mostrar_perfil()


# Simular que el competidor gana puntos
print("\nSimulando que el competidor gana puntos...")
competidor1.ganar_puntos(50)
competidor1.perder_puntos(20)

# Simular que el observador ve partidas
observador1.vistas()
observador1.vistas()
observador1.vistas()

print("\nPerfil actualizado del observador:")
observador1.mostrar_perfil()