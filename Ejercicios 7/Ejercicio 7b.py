## Excepción personalizada
class CalificacionFueraDeRangoError(Exception):
    pass


## Función para pedir entero con validación
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar un número entero")


contador = 0  ## contador de estudiantes

try:
    archivo = open("calificaciones.txt", "a")  ## abrir archivo en modo agregar

    while True:
        nombre = input("Nombre del estudiante (o 'salir' para terminar): ")

        if nombre.lower() == "salir":
            break

        calificacion = pedir_entero("Calificación (0-100): ")

        ## validar rango
        if calificacion < 0 or calificacion > 100:
            raise CalificacionFueraDeRangoError(
                "La calificación debe estar entre 0 y 100"
            )

        ## guardar en archivo
        archivo.write(f"{nombre} - {calificacion}\n")

        contador += 1  ## aumentar contador

except CalificacionFueraDeRangoError as e:
    print("Error personalizado:", e)

## manejo de errores de archivo
except FileNotFoundError:
    print("Error: No se encontró el archivo")

except PermissionError:
    print("Error: No tienes permisos para escribir en el archivo")

finally:
    try:
        archivo.close()  ## cerrar archivo siempre
    except:
        pass

    print("Total de estudiantes registrados:", contador)  ## siempre se ejecuta