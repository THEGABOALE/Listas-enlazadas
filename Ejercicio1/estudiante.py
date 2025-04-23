'''Una escuela de educacion primaria requiere un algoritmo que muestre los datos de los estudiantes de un salon de clase ordenados de forma ascendente, segun un parametro indicado; 
este parametro puede ser cualquiera de los siguientes campos: carnet, nombres, apellidos, peso, estatura, sexo, promedio'''

#Definir una clase Estudiante, en la que cada instancia representara a un alumno con atributos como carnet, nombres, apellidos, peso, estatura, sexo y promedio
class Estudiante:
    def __init__(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombres = nombres
        self.apellidos = apellidos
        self.peso = peso
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio

    def __str__(self): #Representacion en texto de los datos del estudiante
        return (f"Carnet: {self.carnet}, Nombre: {self.nombres} {self.apellidos}, "
                f"Peso: {self.peso}, Estatura: {self.estatura}, Sexo: {self.sexo}, Promedio: {self.promedio}")
