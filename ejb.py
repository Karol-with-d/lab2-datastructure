# Ejercicio B. Cola (FIFO)
# append() agrega al final, pop(0) atiende al primero
# estilo como la guía de turnos de la clase 17

cola = []
numero_turno = 1


def registrar_pasajero():
    # usamos el contador de afuera
    global numero_turno

    nombre = input("Nombre del pasajero: ").strip()
    if nombre == "":
        print("Dato rechazado: el nombre no puede estar vacío.")
        return

    destino = input("Destino: ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    # ticket con 3 dígitos, como en la guía (T001 -> aquí P001)
    turno = f"P{numero_turno:03d}"
    # en la guía el cliente es una lista [turno, nombre]
    pasajero = [turno, nombre, destino]

    cola.append(pasajero)
    numero_turno = numero_turno + 1

    print("Pasajero registrado. Turno:", turno)


def atender_pasajero():
    # pop(0) saca al primero
    if cola:
        pasajero = cola.pop(0)
        print("PASAJERO ATENDIDO")
        print("Turno:", pasajero[0])
        print("Nombre:", pasajero[1])
        print("Destino:", pasajero[2])
    else:
        print("No hay pasajeros en espera. No se puede atender.")


def mostrar_cola():
    print("PASAJEROS EN ESPERA")
    if not cola:
        print("No hay pasajeros en espera.")
        print("Total en espera: 0")
    else:
        for pasajero in cola:
            print(pasajero[0], "-", pasajero[1], "-", pasajero[2])
        print("Total en espera:", len(cola))


# Mejora: pasajeros por destino
def contar_por_destino():
    destino = input("Destino a consultar: ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    contador = 0
    for pasajero in cola:
        if pasajero[2].lower() == destino.lower():
            contador = contador + 1

    print("Pasajeros esperando para", destino + ":", contador)


while True:
    print()
    print("===== COLA DE PASAJEROS (FIFO) =====")
    print("1. Registrar pasajero")
    print("2. Atender pasajero")
    print("3. Mostrar pasajeros en espera")
    print("4. Consultar pasajeros por destino")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        registrar_pasajero()
    elif opcion == "2":
        atender_pasajero()
    elif opcion == "3":
        mostrar_cola()
    elif opcion == "4":
        contar_por_destino()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Elija un número del 1 al 5.")
