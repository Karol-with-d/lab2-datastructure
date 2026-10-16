# Ejercicio C. Arbol de destinos
# NodoDestino guarda el nombre y una lista de hijos

class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre
        # hijos = zonas o ciudades debajo de este nodo
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)


def construir_arbol():
    # Terminal Central -> zonas -> ciudades
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
    # recursivo: imprime el nodo y luego sus hijos
    sangria = "  " * nivel
    print(sangria + "- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_jerarquia(hijo, nivel + 1)


def buscar_destino(nodo, nombre_buscado):
    # busqueda recursiva: regresa el nodo o None
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
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Elija un número del 1 al 3.")


main()
