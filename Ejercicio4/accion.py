class Accion: #Se define la clase que representa una accion como "escribir", "borrar", etc
    def __init__(self, tipo, contenido): #Inicializa los atributos tipo y contenido
        self.tipo = tipo 
        self.contenido = contenido 
    
    def __str__(self): #Permite que al imprimir una accion se vea bonito
        return f"{self.tipo.capitalize()}: '{self.contenido}'"