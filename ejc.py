"""
Laboratorio 2 — Ejercicio C.

NodoDestino representa un punto de la jerarquía (terminal, zona o ciudad) y guarda a sus hijos en una lista
Mostrar y buscar se hacen con recursión: cada nodo resuelve su parte y delega el resto a sus hijos
"""

class NodoDestino:
    """Un nodo del árbol: nombre del destino y lista de hijos"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)


def construir_arbol():
    """Crea el árbol de destinos con Terminal Central como raíz, las zonas como sus hijos y las ciudades dentro de cada zona"""
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
    """
    Recorre el árbol de forma recursiva en preorden
    imprimiendo cada nodo antes que sus hijos y aumentando la sangría según el nivel
    """
    sangria = "  " * nivel
    print(sangria + "- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_jerarquia(hijo, nivel + 1)


def buscar_destino(nodo, nombre_buscado):
    """
    Busca el destino de forma recursiva, sin distinguir mayúsculas
    Devuelve el nodo encontrado o None si no existe
    """
    if nodo.nombre.lower() == nombre_buscado.lower():
        return nodo

    for hijo in nodo.hijos:
        encontrado = buscar_destino(hijo, nombre_buscado)
        if encontrado is not None:
            return encontrado

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


def salir():
    print("Programa finalizado.")


def mostrar_menu():
    print()
    print("===== ÁRBOL DE DESTINOS =====")
    print("1. Mostrar jerarquía")
    print("2. Buscar destino")
    print("3. Salir")


def main():
    arbol = construir_arbol()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opcion_mostrar_arbol(arbol)
        elif opcion == "2":
            opcion_buscar_destino(arbol)
        elif opcion == "3":
            salir()
            break
        else:
            print("Opción no válida. Elija un número del 1 al 3.")


main()
