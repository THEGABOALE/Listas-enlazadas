'''Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
en ambas direcciones, simulando las acciones de Deshacer y Rehacer'''
#Se importan clases necesarias
from nodo_doble import NodoDoble #El nodo de la lista doblemente enlazada
from accion import Accion #Representa una accion como "escribir", "borrar", etc

class Historial: #Se crea la clase historial, que administra la lista doblemente enlazada de acciones
    def __init__(self):
        self.inicio = None #Primer nodo del historial (inicio de la lista)
        self.actual = None #Es el puntero donde el usuario se encuentra actualmente (como un editor, si se deshace o rehace algo)

    def agregar(self, accion): #Añade una nueva accion al historial
        nuevo = NodoDoble(accion) #Se crea un nuevo nodo con la accion recibida
        if self.inicio is None: #Si la lista esta vacia, se asigna el primer nodo
            self.inicio = nuevo #Si no hay ninguna accion previa, este nuevo nodo se vuelve al inicio y el nodo actual
            self.actual = nuevo
        else: #Si no, se conecta el nuevo nodo con el nodo actual y se actualiza el nodo
            if self.actual.anterior is not None: #(Esta parte peude ser un poco confusa)
                self.actual.anterior.siguiente = nuevo
                self.actual.siguiente = nuevo 

            nuevo.anterior = self.actual #El nuevo nodo se enlaza hacia atras en con el nodo actual
            self.actual.siguiente = nuevo #Luego el nodo actual apunta hacia adelante de nuevo
            self.actual = nuevo #Se actualiza self.actual para que apunte al nuevo nodo

    def deshacer(self): #Mueve el puntero hacia atras si es posible
        if self.actual is not None: #Si existe un nodo anterior, se mueve hacia atras y se deuelve la accion correspondiente
            self.actual = self.actual.anterior #Esto simula ctrl + z (deshacer)
            return self.actual.accion #Se devuelve la accion
        return None #Si no se puede rehacer, se devuelve None

    def rehacer(self): #Mueve el puntero hacia adelante si hay una accion por rehacer
        if self.actual and self.actual.siguiente: #Si existe una accion que fue deshecha antes, se puede rehacer
            self.actual = self.actual.siguiente  #Se mueve el puntero hacia adelante y se devuelve la accion
            return self.actual.accion #Se devuelve la accion
        return None #Si no se puede rehacer, se devuelve None

    def mostrar_historial(self): #Recorre toda la lista e imprime las acciones 
        acciones = [] #Se crea una lista para almacenar las acciones
        nodo = self.inicio #Se inicializa el puntero al inicio de la lista
        while nodo: #Mientras exista un nodo, se imprime la accion y se avanza
            acciones.append(str(nodo.accion)) #Se agrega la accion al final de la lista
            nodo = nodo.siguiente #Se avanza al siguiente nodo
        return acciones #se devuelve la lista de acciones
