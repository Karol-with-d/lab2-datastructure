# Ejercicio B. Cola (FIFO)
# append() agrega al final, pop(0) atiende al primero
# estilo como la guía de turnos de la clase 17

# para la fecha y hora del turno
from datetime import datetime

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
    # Mejora: fecha y hora del turno
    fecha_hora = datetime.now().strftime('%d/%m/%Y %H:%M')
    # en la guía el cliente es una lista [turno, nombre]
    pasajero = [turno, nombre, destino, fecha_hora]

    cola.append(pasajero)
    numero_turno = numero_turno + 1

    print("Pasajero registrado. Turno:", turno, "-", fecha_hora)


def atender_pasajero():
    # pop(0) saca al primero
    if cola:
        pasajero = cola.pop(0)
        print("PASAJERO ATENDIDO")
        print("Turno:", pasajero[0])
        print("Nombre:", pasajero[1])
        print("Destino:", pasajero[2])
        print("Llegó:", pasajero[3])
    else:
        print("No hay pasajeros en espera. No se puede atender.")


def mostrar_cola():
    print("PASAJEROS EN ESPERA")
    if not cola:
        print("No hay pasajeros en espera.")
        print("Total en espera: 0")
    else:
        for pasajero in cola:
            print(pasajero[0], "-", pasajero[1], "-", pasajero[2], "-", pasajero[3])
        print("Total en espera:", len(cola))


while True:
    print()
    print("===== COLA DE PASAJEROS (FIFO) =====")
    print("1. Registrar pasajero")
    print("2. Atender pasajero")
    print("3. Mostrar pasajeros en espera")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        registrar_pasajero()
    elif opcion == "2":
        atender_pasajero()
    elif opcion == "3":
        mostrar_cola()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Elija un número del 1 al 4.")
