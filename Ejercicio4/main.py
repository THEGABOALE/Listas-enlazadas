'''Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
en ambas direcciones, simulando las acciones de Deshacer y Rehacer'''

from accion import Accion
from historial import Historial

def menu(): #Menu de opciones con un while infinito que se ejecuta hasta que el usuario salga del programa
    historial = Historial()
    while True:
        print("---MENU---")
        print("1. Escribir")
        print("2. Borrar")
        print("3. Copiar")
        print("4. Pegar")
        print("5. Deshacer")
        print("6. Rehacer")
        print("7. Mostrar historial")
        print("8. Salir")

        opcion = input("Seleccione una opcion: ")

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
        elif opcion == "4": 
            texto = input("Esctiba el texto a pegar: ")
            historial.agregar(Accion("pegar", texto))
        elif opcion == "5": #Llaman a los metodos para deshacer y rehacer
            accion = historial.deshacer()
            if accion:
                print("Deshacer: ", accion)
            else:
                print("No hay acciones para deshacer")
        elif opcion == "6":
            accion = historial.rehacer()
            if accion:
                print("Rehacer: ", accion)
            else:
                print("No hay acciones para rehacer")
        elif opcion == "7": #Muestra el historial
            print("Historial: ")
            for a in historial.mostrar_historial():
                print(a)
        elif opcion == "8":
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__": #Llama al menu si se ejecuta el archivo directamente
    menu()