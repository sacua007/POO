# Proyecto Restaurante 

Este es un programa hecho en **Python** usando **Programación Orientada a Objetos (POO)**.
El programa representa diferentes **platillos de un restaurante** como comida, bebidas, aperitivos y postres.

## Descripción

Se creó una clase principal llamada `Platillo` que contiene la información básica de cualquier platillo:

* nombre
* precio

Después se crean otras clases que **heredan** de `Platillo`.

## Clases del proyecto

### Platillo

Es la clase base.
Contiene:

* `nombre`
* `precio`
* método para mostrar la información del platillo.

### Comida

Hereda de `Platillo`.
Agrega:

* categoría de la comida (ejemplo: mexicana).

### Bebida

Hereda de `Platillo`.
Agrega:

* temperatura de la bebida.

### Aperitivo

Hereda de `Platillo`.
Agrega:

* tamaño del aperitivo.

### Postre

Hereda de `Platillo`.
Agrega:

* si el postre tiene gluten o no.

## Archivo principal

El archivo `main.py` crea algunos ejemplos de platillos:

* Chile Relleno (comida)
* Chocoflan (postre)
* Guacamole (aperitivo)

Después muestra la información de cada uno.

## Ejemplo de salida

Platillo: Chile Relleno, Precio: $150.00
Tipo de comida: Mexicana

Platillo: Chocoflan, Precio: $80.00

Platillo: Guacamole, Precio: $60.00

## Tecnologías usadas

* Python
* Programación Orientada a Objetos

