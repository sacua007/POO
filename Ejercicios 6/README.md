# 🎮 Ejercicio 6 - POO en Python

## 📌 Descripción
Este proyecto contiene dos ejercicios donde se aplica **Programación Orientada a Objetos (POO)** en Python, usando clases, herencia y polimorfismo.

Está inspirado en mecánicas tipo Minecraft, trabajando con mobs y herramientas.

---

## 📂 Estructura del proyecto


Ejercicio 6/
│
├── ejercicio 6a/ # Mobs (criaturas)
│ ├── Mob.py
│ ├── Creeper.py
│ ├── Enderman.py
│ ├── Esqueleto.py
│ ├── Vaca.py
│ └── main.py
│
├── Ejercicio 6b/ # Herramientas y armas
│ ├── Herramienta.py
│ ├── Espada.py
│ ├── Arco.py
│ ├── Pico.py
│ ├── Pala.py
│ └── Main.py


---

## 🧠 Ejercicio 6A: Mobs

### ✔️ Descripción
Se modelan diferentes mobs con comportamientos distintos.

### 🧱 Clases
- `Mob` (clase base)
- `Creeper`
- `Enderman`
- `Esqueleto`
- `Vaca`

Cada clase implementa:
- sonido
- comportamiento
- movimiento

### ▶️ Ejecución
```bash
python main.py
⚔️ Ejercicio 6B: Herramientas
✔️ Descripción

Simulación de herramientas con durabilidad.

🧱 Clases
Herramienta (clase base)
Espada
Arco
Pico
Pala

Cada herramienta:

tiene un uso específico
pierde durabilidad al usarse