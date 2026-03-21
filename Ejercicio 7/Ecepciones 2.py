##Execpciones basicas/ capturar multiples excepciones
#parte 2:
print("=="*20)
print("Ejemplo de manejo de excepciones con listas y múltiples except")
print("=="*20)

colores=["rojo","verde","azul","amarillo"]
print(f"Lista de colores{colores}(indice 0,1,2,3)")

try:
    indice= int(input("que color quieres? (0-3): "))
    print((f"El color que elegiste es: {colores[indice]}"))
except ValueError as e:
    print(f"✖️ ValueError: {e}")
except IndexError as e:
    print(f"✖️ IndexError: {e}")
finally:
    print("Gracias por elegir un color.")
    
