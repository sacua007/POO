
# Proyecto: Clase Estudiante en Python

## Descripción

Este proyecto es un ejemplo sencillo de **Programación Orientada a Objetos (POO)** en Python.
Se crea una clase llamada **Estudiante** que guarda información básica de un alumno y permite que el estudiante se presente.

El programa crea un objeto (instancia de la clase) y muestra un mensaje con sus datos.

---

## Estructura del código

El programa contiene:

* Una **clase** llamada `Estudiante`
* Un **constructor** `__init__` que guarda los datos del estudiante
* Un **método** llamado `presentarse()` que imprime la información
* Un **objeto** llamado `estudiante1` que usa la clase

---

## Código

```python
class Estudiante:
 def __init__(self,nombre,edad,grado):
  self.nombre= nombre
  self.edad= edad
  self.grado= grado

 def presentarse(self):
  print(f"Hola soy {self.nombre}, tengo {self.edad} años y voy en {self.grado} grado")


estudiante1= Estudiante("juan",15,3)
estudiante1.presentarse()
```

---

## Explicación

### Clase

`class Estudiante:`
Define un molde (estructura) para crear estudiantes.

### Constructor

`__init__`
Es un método especial que se ejecuta cuando se crea el objeto.

Guarda:

* nombre
* edad
* grado

### self

`self` representa **al objeto que se está creando**.

Ejemplo:

```
self.nombre
```

significa **el nombre de ese estudiante**.

### Método

`presentarse()`
Es una función dentro de la clase que imprime la información del estudiante.

---

## Ejecución

Cuando se ejecuta el programa, la salida será:

```
Hola soy juan, tengo 15 años y voy en 3 grado
