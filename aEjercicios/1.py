class persona:
        def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad
        
        def presentarse(self):
                print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
# Crear una instancia de la clase persona
persona1 = persona("Juan", 30)
# Llamar al método presentarse


class Estudiante(persona):
        def __init__(self, nombre, edad, carrera):
                super().__init__(nombre, edad)
                self.carrera = carrera
        
        def presentarse(self):
                super().presentarse()
                print(f"Estoy estudiando {self.carrera}.")
# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Ana", 22, "Ingeniería Informática")
# Llamar al método presentarse
estudiante1.presentarse()
persona1.presentarse()