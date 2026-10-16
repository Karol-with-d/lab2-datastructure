# Ejercicio C. Árbol de destinos
# NodoDestino: nombre + lista de hijos (lo pide el laboratorio)

class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre
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
    # recursivo: imprime el nodo y luego cada hijo
    print("  " * nivel + "- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_jerarquia(hijo, nivel + 1)


def buscar_destino(nodo, nombre_buscado):
    # recursivo: regresa el nodo o None (lo pide la guía del lab)
    # comparamos en minúsculas para que no importe mayúscula o minúscula
    if nodo.nombre.lower() == nombre_buscado.lower():
        return nodo
    for hijo in nodo.hijos:
        encontrado = buscar_destino(hijo, nombre_buscado)
        if encontrado is not None:
            return encontrado
    return None


arbol = construir_arbol()

while True:
    print()
    print("===== ÁRBOL DE DESTINOS =====")
    print("1. Mostrar jerarquía")
    print("2. Buscar destino")
    print("3. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        print("Árbol de destinos:")
        mostrar_jerarquia(arbol)
    elif opcion == "2":
        nombre = input("Destino a buscar: ").strip()
        if nombre == "":
            print("Dato rechazado: el nombre del destino no puede estar vacío.")
        else:
            encontrado = buscar_destino(arbol, nombre)
            if encontrado is None:
                print("El destino no existe:", nombre)
            else:
                print("Destino encontrado:", encontrado.nombre)
    elif opcion == "3":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Elija un número del 1 al 3.")
