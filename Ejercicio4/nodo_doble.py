'''Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
en ambas direcciones, simulando las acciones de Deshacer y Rehacer'''

class NodoDoble: #Se define un nodo doble para almacenar la informacion de cada accion
    def __init__(self, accion): #Se define un constructor que recibe una accion
        self.accion = accion #se almacena la accion dentro del nodo actual
        self.anterior = None #Nodo anterior en la lista. Esto permite recorrer la lista en ambas direcciones (en un inicio es None porque aun no esta conectado)
        self.siguiente = None #Nodo siguiente en la lista. Esto permite recorrer la lista en ambas direcciones (tmb es None)