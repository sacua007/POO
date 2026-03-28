# Excepción personalizada
class CalificacionFueraDeRangoError(Exception):
    pass


# Función para pedir entero
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: debes ingresar un número válido")


contador = 0  # contador de estudiantes

try:
    archivo = open("calificaciones.txt", "a")  # modo agregar

    while True:
        nombre = input("Nombre del estudiante (o 'salir'): ")

        if nombre.lower() == "salir":
            break

        calificacion = pedir_entero("Calificación (0-100): ")

        # Validar rango
        if calificacion < 0 or calificacion > 100:
            raise CalificacionFueraDeRangoError("Calificación fuera de rango (0-100)")

        # Guardar en archivo
        archivo.write(f"{nombre} - {calificacion}\n")

        contador += 1
        print("✅ Registro guardado\n")

except CalificacionFueraDeRangoError as e:
    print("❌ Error:", e)

except FileNotFoundError:
    print("❌ Error: no se encontró el archivo")

except PermissionError:
    print("❌ Error: no tienes permisos para escribir en el archivo")

finally:
    try:
        archivo.close()
    except:
        pass

    print("\n📊 Total de estudiantes registrados:", contador)