class Estudiante:
 def __init__(self,nombre,edad,grado):
  self.nombre= nombre
  self.edad= edad
  self.grado= grado

 def presentarse(self):
  print(f"Hola soy {self.nombre},tengo{self.edad}años y voy en{self.grado}grado")



estudiante1= Estudiante("juan",15,3)
estudiante1.presentarse()
