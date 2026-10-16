"""
Laboratorio 2 — Ejercicio C. Árbol de destinos

NodoDestino representa un punto de la jerarquía
(terminal, zona o ciudad) y guarda a sus hijos en una lista.
Mostrar y buscar se hacen con recursión: cada nodo
resuelve su parte y delega el resto a sus hijos.
"""

import sys

# La consola de Windows debe mostrar tildes y la ñ sin alterar el texto.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")


class NodoDestino:
    """Un nodo del árbol: nombre del destino y lista de hijos."""

    def __init__(self, nombre):
        self.nombre = nombre
        # Los hijos permiten armar Terminal -> zona -> ciudad.
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        """Cuelga un destino debajo de este nodo."""
        self.hijos.append(nodo_hijo)


def construir_arbol():
    """
    Arma la jerarquía fija de la terminal.
    La raíz es Terminal Central; debajo van las zonas y, en cada zona, las ciudades.
    """
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
    Recorrido recursivo en preorden.
    Primero imprime el nodo actual y después cada hijo con más sangría,
    para que se vea la jerarquía completa.
    """
    sangria = "  " * nivel
    print(f"{sangria}- {nodo.nombre}")
    for hijo in nodo.hijos:
        mostrar_jerarquia(hijo, nivel + 1)


def buscar_destino(nodo, nombre_buscado):
    """
    Búsqueda recursiva.
    Compara el nodo actual; si no coincide, pregunta a cada hijo.
    Devuelve el nodo encontrado o None si el destino no existe.
    """
    if nodo.nombre.lower() == nombre_buscado.lower():
        return nodo

    for hijo in nodo.hijos:
        encontrado = buscar_destino(hijo, nombre_buscado)
        if encontrado is not None:
            return encontrado

    return None


def opcion_mostrar_arbol(arbol):
    """Muestra la jerarquía completa desde la raíz."""
    print("Árbol de destinos:")
    mostrar_jerarquia(arbol)


def opcion_buscar_destino(arbol):
    """Pide un destino y usa la búsqueda recursiva del árbol."""
    nombre = input("Destino a buscar: ").strip()
    if nombre == "":
        print("Dato rechazado: el nombre del destino no puede estar vacío.")
        return

    encontrado = buscar_destino(arbol, nombre)
    if encontrado is None:
        print(f"El destino '{nombre}' no existe.")
    else:
        print(f"Destino encontrado: {encontrado.nombre}")


def mostrar_menu():
    """Presenta las opciones. Cada número llama a una sola función."""
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


if __name__ == "__main__":
    main()
