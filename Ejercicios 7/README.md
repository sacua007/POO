


Manejo de Excepciones en Python 🐍
Este repositorio contiene ejemplos prácticos y sencillos sobre cómo gestionar errores en Python utilizando bloques try, except, else y finally. El objetivo es evitar que el programa se detenga abruptamente cuando el usuario ingresa datos inesperados.

📁 Contenido del Repositorio
El proyecto se divide en dos partes fundamentales:



Validaciones incluidas:

ValueError: Se activa si el usuario ingresa texto en lugar de números.

ZeroDivisionError: Se activa si el usuario intenta dividir entre cero (el famoso "K ase loko").

Bloques adicionales:

else: Muestra el resultado solo si la operación fue exitosa.

finally: Un mensaje de despedida que se ejecuta siempre, sin importar si hubo error o no.

2. Acceso a Estructuras de Datos (Ecepciones 2.py)
Este script demuestra cómo manejar múltiples excepciones al trabajar con listas y selección de índices.

Validaciones incluidas:

ValueError: Captura errores cuando el índice ingresado no es un entero.

IndexError: Captura errores cuando el usuario busca un índice fuera del rango de la lista (ej. buscar el índice 5 en una lista de 4 elementos).

Uso de alias: Emplea as e para imprimir el mensaje de error técnico específico generado por Python.