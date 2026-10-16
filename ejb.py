"""
Laboratorio 2 — Ejercicio B. Cola (FIFO)

La lista guarda a los pasajeros en el orden en que llegan.
append() encola al final; pop(0) atiende al primero.
Así se respeta el orden de llegada de la terminal.
"""

# Cola FIFO de pasajeros. El índice 0 es quien lleva más tiempo esperando.
cola_pasajeros = []
# El turno identifica el orden de llegada (P001, P002, ...).
siguiente_turno = 1


def registrar_pasajero(cola):
    """
    Encola un pasajero al final con append().
    Rechaza un nombre o un destino vacío.
    """
    global siguiente_turno

    nombre = input("Nombre del pasajero: ").strip()
    if nombre == "":
        print("Dato rechazado: el nombre no puede estar vacío.")
        return

    destino = input("Destino: ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    turno = "P" + str(siguiente_turno).zfill(3)
    pasajero = {
        "turno": turno,
        "nombre": nombre,
        "destino": destino,
    }
    # append coloca al pasajero al final: entra de último y sale de último.
    cola.append(pasajero)
    siguiente_turno = siguiente_turno + 1
    print("Pasajero registrado. Turno:", turno)


def atender_pasajero(cola):
    """
    Atiende al pasajero que llegó primero con pop(0).
    Si la cola está vacía, avisa y no interrumpe el programa.
    """
    if len(cola) == 0:
        print("No hay pasajeros en espera. No se puede atender.")
        return

    # pop(0) retira el frente de la cola: el primero que se registró.
    pasajero = cola.pop(0)
    print("PASAJERO ATENDIDO")
    print("Turno:", pasajero["turno"])
    print("Nombre:", pasajero["nombre"])
    print("Destino:", pasajero["destino"])


def mostrar_cola(cola):
    """Muestra el orden de llegada y cuántos pasajeros siguen en espera."""
    print("PASAJEROS EN ESPERA")
    if len(cola) == 0:
        print("No hay pasajeros en espera.")
        print("Total en espera: 0")
        return

    for pasajero in cola:
        print(pasajero["turno"], "-", pasajero["nombre"], "-", pasajero["destino"])
    print("Total en espera:", len(cola))


def mostrar_menu():
    """Presenta las opciones."""
    print()
    print("===== COLA DE PASAJEROS (FIFO) =====")
    print("1. Registrar pasajero")
    print("2. Atender pasajero")
    print("3. Mostrar pasajeros en espera")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_pasajero(cola_pasajeros)
        elif opcion == "2":
            atender_pasajero(cola_pasajeros)
        elif opcion == "3":
            mostrar_cola(cola_pasajeros)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Elija un número del 1 al 4.")


main()
