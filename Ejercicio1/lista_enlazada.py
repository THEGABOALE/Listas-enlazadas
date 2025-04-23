'''Una escuela de educacion primaria requiere un algoritmo que muestre los datos de los estudiantes de un salon de clase ordenados de forma ascendente, segun un parametro indicado; 
este parametro puede ser cualquiera de los siguientes campos: carnet, nombres, apellidos, peso, estatura, sexo, promedio'''
#Se importan las clases necesarias
from nodo import Nodo
#La clase listaEnlazada gestiona la estructura de datos basada en nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None #El primer nodo de la lista
    #Inserta un nuevo estudiante en la lista al final
    def insertar(self, estudiante):
        nuevo_nodo = Nodo(estudiante) #Crea un nuevo nodo con el estudiante proporcionado
        if not self.cabeza: #Si la lista esta vacia, el nuevo nodo se convierte en la cabeza
            self.cabeza = nuevo_nodo
        else: #Si la lista ya tiene nodos, recorre hasta el final y agrega el nuevo nodo
            actual = self.cabeza
            while actual.siguiente: #Recorre la lista hasta encontrar el ultimo nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    #Recorre la lista y devuelve una lista con los datos de los estudiantes
    def recorrer(self):
        actual = self.cabeza
        estudiantes = [] #Lista para almacenar los datos de los estudiantes
        while actual: #Mientras la lista no este vacia recorre la lista hasta el final
            estudiantes.append(actual.estudiante) #Agrega los datos del estudiante al final de la lista
            actual = actual.siguiente
        return estudiantes #Se devuelve la lista de estudiantes
    #Ordenar los nodos de la lista segun un atributo (parametro indicado)
    def ordenar_por(self, atributo):
        estudiantes = self.recorrer() #Obtener lista de estudiantes
        estudiantes.sort(key=lambda estudent: getattr(estudent, atributo)) #Ordenar la lista por el atributo indicado
        self.cabeza = None #Reiniciar la lista enlazada
        for est in estudiantes: #Insertar los estudiantes ordenados 
            self.insertar(est)
    #Mostrar los estudiantes en la lista de forma legible
    def mostrar(self):
        estudiantes = self.recorrer() #Recorrer la lista y obtener los datos de los estudiantes
        for est in estudiantes:
            print(est) #Mostrar cada estudiante con su representacion de texto