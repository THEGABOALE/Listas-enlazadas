'''Una escuela de educacion primaria requiere un algoritmo que muestre los datos de los estudiantes de un salon de clase ordenados de forma ascendente, segun un parametro indicado; 
este parametro puede ser cualquiera de los siguientes campos: carnet, nombres, apellidos, peso, estatura, sexo, promedio'''

#Crear una clase Nodo que almacene un estudiante y un puntero al siguiente nodo
class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante #Contiene los datos del estudiante
        self.siguiente = None #Puntero al siguiente nodo (inicialmente es None)