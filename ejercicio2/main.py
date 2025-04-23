from listaenlazada import ListaEnlazada

def menu():
    ruta = ListaEnlazada()

    while True:
        print("\n--- Menú de Ruta de Estaciones ---")
        print("1. Agregar estación")
        print("2. Imprimir ruta")
        print("3. Calcular tiempo entre estaciones")
        print("4. Buscar estación")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la estación: ")
            try:
                tiempo = int(input("Tiempo hacia la siguiente estación (en minutos): "))
                ruta.agregar_estacion(nombre, tiempo)
                print("Estación agregada correctamente.")
            except ValueError:
                print("Tiempo inválido. Debe ser un número entero.")

        elif opcion == "2":
            ruta.imprimir_ruta()

        elif opcion == "3":
            origen = input("Nombre de la estación de origen: ")
            destino = input("Nombre de la estación de destino: ")
            tiempo = ruta.calcular_tiempo(origen, destino)
            if tiempo is not None:
                print(f"El tiempo estimado desde {origen} hasta {destino} es de {tiempo} minutos.")
            else:
                print("Estaciones no válidas o no están en el orden correcto.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre de la estación a buscar: ")
            estacion = ruta.buscar_estacion(nombre)
            if estacion:
                print(f"Estación encontrada: {estacion.nombre} con {estacion.tiempo} minutos hacia la siguiente.")
            else:
                print("Estación no encontrada.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()