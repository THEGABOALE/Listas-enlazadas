'''Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
en ambas direcciones, simulando las acciones de Deshacer y Rehacer'''
#Importa las clases necesarias
from accion import Accion #Representa cada accion que el usuario realiza
from historial import Historial #Es la lista doblemente enlazada que almacena esas acciones

def menu(): #Menu de opciones con un while infinito que se ejecuta hasta que el usuario salga del programa
    historial = Historial() #Se crea una instancia donde se guardaran las acciones
    while True:#Muestra las opciones en pantalla
        print("---MENU---")
        print("1. Escribir")
        print("2. Borrar")
        print("3. Copiar")
        print("4. Pegar")
        print("5. Deshacer")
        print("6. Rehacer")
        print("7. Mostrar historial")
        print("8. Salir")
        #El menu se repite gracias al while infinito
        opcion = input("Seleccione una opcion: ") #Se pide la opcion al usuario

        if opcion == "1": #Si el usuario elige escribir, pide el texto y lo guarda como una accion
            texto = input("Escriba el texto a escribir: ")
            historial.agregar(Accion("escribir", texto))
        elif opcion == "2": #Lo mismo pero para borrar
            texto = input("Escriba el texto a borrar: ")
            historial.agregar(Accion("borrar", texto))
            print("Texto borrado con exito")
        elif opcion == "3": #Lo mismo pero para copiar
            texto = input("Escriba el texto a copiar: ")
            historial.agregar(Accion("copiar", texto))
            print("Texto copiado con exito")
        elif opcion == "4": #Lo mismo pero para pegar
            texto = input("Escriba el texto a pegar: ")
            historial.agregar(Accion("pegar", texto))
            print("Texto pegado con exito")
        elif opcion == "5": #Llaman al metodo deshacer del historial
            accion = historial.deshacer() #Se llama al metodo deshacer y se devuelve la accion
            if accion: #Si se pudo deshacer, se imprime la accion
                print("Deshacer: ", accion)
            else: #Si no se pudo deshacer, se imprimira un mensaje
                print("No hay acciones para deshacer")
        elif opcion == "6": #Funciona igual que deshacer, pero avanza hacia adelante en el hsitorial
            accion = historial.rehacer()
            if accion:
                print("Rehacer: ", accion)
            else:
                print("No hay acciones para rehacer")
        elif opcion == "7": #Muestra el historial
            print("Historial: ")#Gracias al metodo str en Accion, las acciones se imprimen bonitas
            for a in historial.mostrar_historial():
                print(a)
        elif opcion == "8":
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__": #Llama al menu si se ejecuta el archivo directamente
    menu()