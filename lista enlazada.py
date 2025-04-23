class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #None significa nulo

class ListaEnlazada:
    def __init__(self):
        self.inicio = None
        
def insertar_al_inicio(self, dato):
    nuevo = Nodo(dato)
    nuevo.siguiente = self.cabeza
    self.cabeza = nuevo

def insertar_al_final(self, dato):
    nuevo = Nodo(dato)
    if not self.cabeza:
        self.cabeza = nuevo
    else:
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

def buscar(self, valor):
    actual = self.cabeza
    while actual:
        if actual.dato == valor:
            return True
        actual = actual.siguiente
    return False

def actualizar(self, viejo, nuevo):
    actual = self.cabeza
    while actual:
        if actual.dato == viejo:
            actual.dato = nuevo
            return True
        actual = actual.siguiente
    return False

def eliminar_al_inicio(self):
    if self.cabeza:
        self.cabeza = self.cabeza.siguiente

def eliminar_al_final(self):
    if not self.cabeza:
        return
    if not self.cabeza.siguiente:
        self.cabeza = None
        return
    actual = self.cabeza
    while actual.siguiente.siguiente:
        actual = actual.siguiente
    actual.siguiente = None

def imprimir(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía")
        else:
            print("Elementos de la Lista Enlazada")
            while actual:
                print(f" -> {actual.dato}")
                actual = actual.siguiente

