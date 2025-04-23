class Paciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
    
    def imprimirInformacion(self):
        return f"Nombre: {self.nombre}\tEdad: {self.edad}\tSíntoma: {self.sintoma}\tPrioridad: {self.prioridad}"