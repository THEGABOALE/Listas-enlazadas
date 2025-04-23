'''Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
en ambas direcciones, simulando las acciones de Deshacer y Rehacer'''

from nodo_doble import NodoDoble
from accion import Accion

class Historial:
    def __init__(self):
        self.inicio = None #Primer nodo al historial
        self.actual = None #Nodo donde esta el usuario actualmente (puntero de deshacer/rehacer)

    def agregar(self, accion): #Añade una nueva accion al historial
        nuevo = NodoDoble(accion)
        if self.inicio is None: #Si la lista esta vacia, se asigna el primer nodo
            self.inicio = nuevo
            self.actual = nuevo
        else: #Sin, se conecta el nuevo nodo con el nodo actual y se actualiza el nodo
            if self.actual.anterior is not None:
                self.actual.anterior.siguiente = nuevo
                self.actual.siguiente = nuevo

            nuevo.anterior = self.actual
            self.actual.siguiente = nuevo
            self.actual = nuevo

    def deshacer(self): #Mueve el puntero hacia atras si es posible
        if self.actual is not None:
            self.actual = self.actual.anterior
            return self.actual.accion
        return None

    def rehacer(self): #Mueve el puntero hacia adelante si hay una accion por rehacer
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.accion
        return None

    def mostrar_historial(self): #Recorre toda la lista e imprime las acciones 
        acciones = []
        nodo = self.inicio
        while nodo:
            acciones.append(str(nodo.accion))
            nodo = nodo.siguiente
        return acciones
