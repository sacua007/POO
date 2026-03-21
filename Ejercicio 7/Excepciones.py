#parte 1 con try/except simple

try:
    a=int(input("Ingrese un número: "))
    b=int(input("Ingrese otro número: "))
    total=a/b
except ValueError:
    print("Error: Solo numeros y YAA.")
except ZeroDivisionError:
    print("Error: K ase loko como que un cero.")
else: print(f"El resultado de {a}/{b} es: {total}")
    
finally:
    print("Pero pos gracias por usar el programa.")
