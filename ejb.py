"""
Laboratorio 2 — Ejercicio B.

La lista guarda a los pasajeros en el orden en que llegan.
- append() encola al final
- pop(0) retira al primero de la lista

de esta forma los pasajeros salen de la cola en el orden en que llegaron
"""

import ejc


cola_pasajeros = []
# cada pasajero recibe un turno segun el orden de llegada (P001, P002, ...).
siguiente_turno = 1

def registrar_pasajero(cola, arbol):
    # Registra un pasajero con nombre y un destino de la terminal.
    global siguiente_turno

    nombre = input("Nombre del pasajero: ").strip()
    if nombre == "":
        print("Dato rechazado: el nombre no puede estar vacío.")
        return

    destino = input("Destino: ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    destino = ejc.buscar_destino_valido(arbol, destino)
    if destino is None:
        print("Dato rechazado: el destino no existe.")
        return

    turno = "P" + str(siguiente_turno).zfill(3)
    pasajero = {
        "turno": turno,
        "nombre": nombre,
        "destino": destino,
    }
    # el pasajero queda detrás de los que ya están esperando
    cola.append(pasajero)
    siguiente_turno = siguiente_turno + 1
    print("Pasajero registrado. Turno:", turno)


def atender_pasajero(cola):
    """
    Atiende al pasajero que llegó primero y si no hay pasajeros esperando, muestra un aviso
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


# Mejora: pasajeros por destino
# Ayuda a organizar los viajes según cuántos pasajeros esperan.
# Prueba: dos pasajeros para San Miguel dan 2; al atender a uno, queda 1.
def contar_por_destino(cola, arbol):
    destino = input("Destino a consultar: ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    destino = ejc.buscar_destino_valido(arbol, destino)
    if destino is None:
        print("Dato rechazado: el destino no existe.")
        return

    # Cuenta las coincidencias sin sacar pasajeros de la cola.
    contador = 0
    for pasajero in cola:
        if pasajero["destino"].lower() == destino.lower():
            contador = contador + 1

    print("Pasajeros esperando para", destino + ":", contador)


def salir():
    print("Programa finalizado.")


def mostrar_menu():
    print()
    print("===== COLA DE PASAJEROS (FIFO) =====")
    print("1. Registrar pasajero")
    print("2. Atender pasajero")
    print("3. Mostrar pasajeros en espera")
    print("4. Consultar pasajeros por destino")
    print("5. Salir")


def main():
    arbol = ejc.construir_arbol()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_pasajero(cola_pasajeros, arbol)
        elif opcion == "2":
            atender_pasajero(cola_pasajeros)
        elif opcion == "3":
            mostrar_cola(cola_pasajeros)
        elif opcion == "4":
            contar_por_destino(cola_pasajeros, arbol)
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción no válida. Elija un número del 1 al 5.")


if __name__ == "__main__":
    main()
