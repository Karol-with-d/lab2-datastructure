# Ejercicio B. Cola (FIFO)
# append() agrega al final, pop(0) atiende al primero

# cola de pasajeros en espera
cola_pasajeros = []
siguiente_turno = 1


def registrar_pasajero(cola):
    # encola un pasajero al final
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
    cola.append(pasajero)
    siguiente_turno = siguiente_turno + 1
    print("Pasajero registrado. Turno:", turno)


def atender_pasajero(cola):
    # atiende al que llego primero con pop(0)
    if len(cola) == 0:
        print("No hay pasajeros en espera. No se puede atender.")
        return

    pasajero = cola.pop(0)
    print("PASAJERO ATENDIDO")
    print("Turno:", pasajero["turno"])
    print("Nombre:", pasajero["nombre"])
    print("Destino:", pasajero["destino"])


def mostrar_cola(cola):
    # muestra el orden de llegada y el total en espera
    print("PASAJEROS EN ESPERA")
    if len(cola) == 0:
        print("No hay pasajeros en espera.")
        print("Total en espera: 0")
        return

    for pasajero in cola:
        print(pasajero["turno"], "-", pasajero["nombre"], "-", pasajero["destino"])
    print("Total en espera:", len(cola))


def mostrar_menu():
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
