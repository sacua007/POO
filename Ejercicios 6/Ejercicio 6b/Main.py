from Pico import Pico
from Espada import Espada
from Pala import Pala
from Arco import Arco


pico1 = Pico("diamante", 10)
pico1.estado()

espada1 = Espada("hierro", 15)
espada1.estado()
espada1.usar("zombie")
espada1.estado()

pala1 = Pala("oro", 5)
pala1.estado()

arco1 = Arco("madera", 4)
arco1.estado()
arco1.flechas = 3
print(arco1.usar("esqueleto"))
arco1.estado()
print(arco1.usar("esqueleto"))
arco1.estado()
