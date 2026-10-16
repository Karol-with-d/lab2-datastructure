"""
Laboratorio 2 — Terminal de buses.

Un menú reúne la pila de salidas, la cola de pasajeros y el árbol de destinos.
"""

import ejb
import ejc
import lab2


def mostrar_menu():
    print()
    print("===== TERMINAL CENTRAL =====")
    print("SALIDAS DE BUSES (LIFO)")
    print("1. Registrar salida")
    print("2. Mostrar salidas")
    print("3. Deshacer última salida")
    print("4. Consultar cima sin retirar")
    print("PASAJEROS (FIFO)")
    print("5. Registrar pasajero")
    print("6. Atender pasajero")
    print("7. Mostrar pasajeros en espera")
    print("8. Consultar pasajeros por destino")
    print("DESTINOS")
    print("9. Mostrar árbol de destinos")
    print("10. Buscar destino")
    print("11. Salir")


def salir():
    print("Programa finalizado.")


def main():
    # Se construye una sola vez y se comparte con las funciones de los módulos.
    arbol = ejc.construir_arbol()

    # Las listas se conservan al cambiar de opción dentro de la misma ejecución.
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            lab2.registrar_salida(arbol)
        elif opcion == "2":
            lab2.mostrar_salidas()
        elif opcion == "3":
            lab2.deshacer_salida()
        elif opcion == "4":
            lab2.consultar_cima()
        elif opcion == "5":
            ejb.registrar_pasajero(ejb.cola_pasajeros, arbol)
        elif opcion == "6":
            ejb.atender_pasajero(ejb.cola_pasajeros)
        elif opcion == "7":
            ejb.mostrar_cola(ejb.cola_pasajeros)
        elif opcion == "8":
            ejb.contar_por_destino(ejb.cola_pasajeros, arbol)
        elif opcion == "9":
            ejc.opcion_mostrar_arbol(arbol)
        elif opcion == "10":
            ejc.opcion_buscar_destino(arbol)
        elif opcion == "11":
            salir()
            break
        else:
            print("Opción no válida. Elija un número del 1 al 11.")


if __name__ == "__main__":
    main()
