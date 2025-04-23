'''Una escuela de educacion primaria requiere un algoritmo que muestre los datos de los estudiantes de un salon de clase ordenados de forma ascendente, segun un parametro indicado; 
este parametro puede ser cualquiera de los siguientes campos: carnet, nombres, apellidos, peso, estatura, sexo, promedio'''

#El menu principal gestiona la interaccion del usuario con el sistema
from lista_enlazada import ListaEnlazada
from estudiante import Estudiante


def menu():
    lista = ListaEnlazada() #Crear una lista enlazada para almacenar estudiantes

    while True:
        #Mostrar opciones disponibles al usuario
        print("\n---Sistema de estudiantes---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Ordenar por campo")
        print("4. Salir del programa")
        #Solicitar al usuario que elija una opcion
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            #Solicitar los datos del estudiante
            print("Introduzca los datos del estudiante")
            carnet = input("Carnet: ")
            nombres = input("Nombres: ")
            apellidos = input("Apellidos: ")
            peso = input("Peso(Kg): ")
            estatura = input("Estatura: ")
            sexo = input("Sexo(M/F): ")
            promedio = input("Promedio: ")
            estudiante = Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio)
            lista.insertar(estudiante) #Agregar a la lista
            print("Estudiante agregado con exito")
        elif opcion == "2":
            lista.mostrar() #Mostrar los estudiantes en la lista
        elif opcion == "3":
            #Solicitar al usuario el campo por el cual desea ordenar la lista
            campo = input("Campo por el que deseas ordenar (carnet, nombres, apellidos, peso, estatura, sexo, promedio): ")
            lista.ordenar_por(campo) #Ordenar la lista por el campo indicado
            print("Lista ordenada correctamente")
        elif opcion == "4":
            print("Saliendo del programa") #Finalizar la ejecucion
            break
        else:
            print("Opcion invalida, por favor intentelo de nuevo") #Gestionar errores en la opcion ingresada

if __name__ == "__main__":
    menu() #Ejecutrar el menu