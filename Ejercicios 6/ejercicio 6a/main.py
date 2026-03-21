from Vaca import Vaca
vaca1 = Vaca("Pintona", 10)
vaca1.presentarse()

from Creeper import Creeper
creeper1 = Creeper("Cañon", 20)
creeper1.presentarse()

from Enderman import Enderman
enderman1 = Enderman("Sombra", 15)
enderman1.presentarse()

from Esqueleto import Esqueleto
esqueleto1 = Esqueleto("Huesitos", 12)
esqueleto1.presentarse()

if __name__ == "__main__":
    mobs = [vaca1, creeper1, enderman1, esqueleto1]
    for mob in mobs:
        mob.presentarse()


   

   