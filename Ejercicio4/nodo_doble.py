'''Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
en ambas direcciones, simulando las acciones de Deshacer y Rehacer'''

class NodoDoble:
    def __init__(self, accion):
        self.accion = accion #Lo que hizo el usuario
        self.anterior = None #Nodo anterior en la lista
        self.siguiente = None #Nodo siguiente en la lista. Esto permite recorrer la lista en ambas direcciones