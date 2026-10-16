"""
Laboratorio 2 — Terminal de buses.

Un menú integra la pila de salidas (LIFO), la cola de pasajeros (FIFO)
y el árbol de destinos. 
"""

pila_salidas = []
capacidad_maxima = 10
cola_pasajeros = []
siguiente_turno = 1


# Ejercicio A: la última salida registrada es la primera que se deshace.
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

    destino = buscar_destino_valido(arbol, destino)
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


# Ejercicio B: los pasajeros se atienden en el orden en que llegaron.
def registrar_pasajero(cola, arbol):
    global siguiente_turno

    nombre = input("Nombre del pasajero: ").strip()
    if nombre == "":
        print("Dato rechazado: el nombre no puede estar vacío.")
        return

    destino = input("Destino: ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    destino = buscar_destino_valido(arbol, destino)
    if destino is None:
        print("Dato rechazado: el destino no existe.")
        return

    turno = "P" + str(siguiente_turno).zfill(3)
    pasajero = {
        "turno": turno,
        "nombre": nombre,
        "destino": destino,
    }
    # append() coloca al pasajero detrás de los que ya están esperando.
    cola.append(pasajero)
    siguiente_turno = siguiente_turno + 1
    print("Pasajero registrado. Turno:", turno)


def atender_pasajero(cola):
    if len(cola) == 0:
        print("No hay pasajeros en espera. No se puede atender.")
        return

    # pop(0) retira al primero de la cola: comportamiento FIFO.
    pasajero = cola.pop(0)
    print("PASAJERO ATENDIDO")
    print("Turno:", pasajero["turno"])
    print("Nombre:", pasajero["nombre"])
    print("Destino:", pasajero["destino"])


def mostrar_cola(cola):
    print("PASAJEROS EN ESPERA")
    if len(cola) == 0:
        print("No hay pasajeros en espera.")
        print("Total en espera: 0")
        return

    for pasajero in cola:
        print(pasajero["turno"], "-", pasajero["nombre"], "-", pasajero["destino"])
    print("Total en espera:", len(cola))


# Mejora: pasajeros por destino.
# Ayuda a organizar los viajes según cuántos pasajeros esperan.
# Prueba: dos pasajeros para San Miguel dan 2; al atender a uno, queda 1.
def contar_por_destino(cola, arbol):
    destino = input("Destino a consultar: ").strip()
    if destino == "":
        print("Dato rechazado: el destino no puede estar vacío.")
        return

    destino = buscar_destino_valido(arbol, destino)
    if destino is None:
        print("Dato rechazado: el destino no existe.")
        return

    # Cuenta sin sacar pasajeros de la cola.
    contador = 0
    for pasajero in cola:
        if pasajero["destino"].lower() == destino.lower():
            contador = contador + 1

    print("Pasajeros esperando para", destino + ":", contador)


# Ejercicio C: cada nodo guarda su nombre y una lista con sus hijos.
class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)


def construir_arbol():
    raiz = NodoDestino("Terminal Central")

    zona_oriental = NodoDestino("Zona Oriental")
    zona_oriental.agregar_hijo(NodoDestino("San Miguel"))
    zona_oriental.agregar_hijo(NodoDestino("La Unión"))
    zona_oriental.agregar_hijo(NodoDestino("Usulután"))

    zona_central = NodoDestino("Zona Central")
    zona_central.agregar_hijo(NodoDestino("San Salvador"))
    zona_central.agregar_hijo(NodoDestino("La Libertad"))

    zona_occidental = NodoDestino("Zona Occidental")
    zona_occidental.agregar_hijo(NodoDestino("Santa Ana"))
    zona_occidental.agregar_hijo(NodoDestino("Ahuachapán"))

    raiz.agregar_hijo(zona_oriental)
    raiz.agregar_hijo(zona_central)
    raiz.agregar_hijo(zona_occidental)
    return raiz


def mostrar_jerarquia(nodo, nivel=0):
    # Recorrido recursivo en preorden: primero el nodo y después sus hijos.
    sangria = "  " * nivel
    print(sangria + "- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_jerarquia(hijo, nivel + 1)


def buscar_destino(nodo, nombre_buscado):
    if nodo.nombre.lower() == nombre_buscado.lower():
        return nodo

    # Cada llamada busca en una rama; None indica que no hubo coincidencia.
    for hijo in nodo.hijos:
        encontrado = buscar_destino(hijo, nombre_buscado)
        if encontrado is not None:
            return encontrado

    return None


def buscar_destino_valido(arbol, nombre):
    # Pasajeros y buses consultan el mismo árbol, sin repetir las ciudades.
    encontrado = buscar_destino(arbol, nombre)
    if encontrado is not None:
        # Solo las ciudades son destinos, no la terminal ni las zonas.
        if len(encontrado.hijos) == 0:
            return encontrado.nombre
    return None


def opcion_mostrar_arbol(arbol):
    print("Árbol de destinos:")
    mostrar_jerarquia(arbol)


def opcion_buscar_destino(arbol):
    nombre = input("Destino a buscar: ").strip()
    if nombre == "":
        print("Dato rechazado: el nombre del destino no puede estar vacío.")
        return

    encontrado = buscar_destino(arbol, nombre)
    if encontrado is None:
        print("El destino no existe:", nombre)
    else:
        print("Destino encontrado:", encontrado.nombre)


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
    # Un único árbol valida los destinos de ambas listas durante la ejecución.
    arbol = construir_arbol()

    while True:
        mostrar_menu()
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
            registrar_pasajero(cola_pasajeros, arbol)
        elif opcion == "6":
            atender_pasajero(cola_pasajeros)
        elif opcion == "7":
            mostrar_cola(cola_pasajeros)
        elif opcion == "8":
            contar_por_destino(cola_pasajeros, arbol)
        elif opcion == "9":
            opcion_mostrar_arbol(arbol)
        elif opcion == "10":
            opcion_buscar_destino(arbol)
        elif opcion == "11":
            salir()
            break
        else:
            print("Opción no válida. Elija un número del 1 al 11.")


if __name__ == "__main__":
    main()