# 🎮 Sistema de Registro para Torneo de Videojuegos

Proyecto desarrollado en Python usando Programación Orientada a Objetos (POO) y herencia.

El sistema simula el registro de participantes para un torneo de videojuegos del Instituto Tecnológico de Ensenada.

---

# 📚 Características

El sistema maneja dos tipos de jugadores:

## 👨‍💻 Competidor
- Pertenece a un equipo.
- Puede ganar y perder puntos.
- Hereda atributos y métodos de la clase `Jugador`.

## 👀 Observador
- Puede ver partidas.
- Gana 5 puntos automáticamente por cada partida observada.
- Lleva un contador de partidas vistas.
- Hereda atributos y métodos de la clase `Jugador`.

---

# 🧠 Conceptos aplicados

- Clases y objetos
- Herencia
- Sobreescritura de métodos
- Uso de `super()`
- Encapsulamiento básico
- Modularización en múltiples archivos

---

# 📂 Estructura del proyecto

```text
Herencia_1/
│
├── Jugador.py
├── Competidor.py
├── Observador.py
└── Main.py