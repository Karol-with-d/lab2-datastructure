"""
Laboratorio 2 — Ejercicio A.

La lista guarda las salidas con append() y deshace la última con pop().
Se usa LIFO porque la salida más reciente es la primera que se puede deshacer.
"""

import ejc


pila_salidas = []
capacidad_maxima = 10


def registrar_salida(arbol):
    print()
    print("Registro de salidas de autobuses")

    if len(pila_salidas) >= capacidad_maxima:
        print("Error: la pila llegó a su límite.")
        return

    # strip() evita guardar campos que solo contienen espacios.
    ruta = input("Número de ruta (ejemplo: Ruta 11): ").strip()
    if ruta == "":
        print("Dato rechazado: la ruta no puede estar vacía.")
        return

    destino = input("Destino (ejemplo: San Miguel): ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    destino = ejc.buscar_destino_valido(arbol, destino)
    if destino is None:
        print("Dato rechazado: el destino no existe.")
        return

    salida = [ruta, destino]
    # El final de la lista es la cima de la pila.
    pila_salidas.append(salida)
    print("Salida registrada:", ruta, "se dirige a", destino)
    print("Salidas guardadas:", len(pila_salidas), "de", capacidad_maxima)


def mostrar_salidas():
    print("Historial de salidas registradas")
    if len(pila_salidas) == 0:
        print("No hay salidas registradas en la pila.")
        return

    numero = 1
    for salida in pila_salidas:
        print(str(numero) + ".", "Ruta:", salida[0], "| Destino:", salida[1])
        numero = numero + 1

    consultar_cima()


# Mejora: consultar la cima sin retirar el registro.
# Permite revisar la última salida sin alterar el historial.
# Prueba: consultar dos veces conserva la misma salida y el tamaño de la pila.
def consultar_cima():
    if len(pila_salidas) == 0:
        print("No hay salidas registradas en la pila.")
        return

    ultima = pila_salidas[-1]
    print("Última salida registrada:", ultima[0], "hacia", ultima[1])


def deshacer_salida():
    if len(pila_salidas) > 0:
        # pop() sin índice retira la última salida: comportamiento LIFO.
        eliminada = pila_salidas.pop()
        print("Se eliminó la última salida:", eliminada[0], "hacia", eliminada[1])
    else:
        print("No hay salidas en la pila que deshacer.")


def ejecutar_sistema_pila():
    arbol = ejc.construir_arbol()
    while True:
        print()
        print("===== SALIDAS DE BUSES (LIFO) =====")
        print("1. Registrar salida de bus")
        print("2. Mostrar salidas y última registrada")
        print("3. Deshacer última salida")
        print("4. Consultar cima sin retirar")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_salida(arbol)
        elif opcion == "2":
            mostrar_salidas()
        elif opcion == "3":
            deshacer_salida()
        elif opcion == "4":
            consultar_cima()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Elija un número del 1 al 5.")


# Al importar este archivo desde main.py no se abre otro menú.
if __name__ == "__main__":
    ejecutar_sistema_pila()