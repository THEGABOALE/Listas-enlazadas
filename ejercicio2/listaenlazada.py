from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def agregar_estacion(self, nombre, tiempo):
        nueva = Nodo(nombre, tiempo)
        if not self.inicio:
            self.inicio = nueva
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva

    def calcular_tiempo(self, origen, destino):
        actual = self.inicio
        tiempo_total = 0
        en_ruta = False

        while actual:
            if actual.nombre == origen:
                en_ruta = True
            if en_ruta:
                if actual.nombre == destino:
                    return tiempo_total
                tiempo_total += actual.tiempo
            actual = actual.siguiente

        return None  # No se encontró origen o destino en orden correcto

    def imprimir_ruta(self):
        actual = self.inicio
        print("Ruta de estaciones:")
        while actual:
            print(f"{actual.nombre} ({actual.tiempo} min) →", end=" ")
            actual = actual.siguiente
        print("Fin")

    def buscar_estacion(self, nombre):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None