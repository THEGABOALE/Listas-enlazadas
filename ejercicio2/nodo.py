class Nodo:
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo  # Tiempo hacia la siguiente estación
        self.siguiente = None