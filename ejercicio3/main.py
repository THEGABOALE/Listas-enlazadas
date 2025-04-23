"""
Problema#3
Una clínica recibe pacientes en orden de llegada. Cada paciente debe ser ingresado al sistema
con los siguientes datos: nombre completo, edad, síntoma principal y prioridad (de 1 a 5). El
sistema debe permitir insertar nuevos pacientes, recorrer la lista para mostrar el orden de
atención, y eliminar a un paciente una vez atendido.
"""

from paciente import Paciente
from clinica import Clinica

clinica = Clinica()

while True:
    print("\n\nSistema para la clínica\n")
    print("1. Agregar paciente")
    print("2. Mostrar pacientes")
    print("3. Atender paciente")
    print("4. Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Valor no contemplado. Intente de nuevo.")
        continue

    match opcion:
        case 1:
            nombre = input("\nIngrese el nombre del paciente: ")
            edad = int(input("Ingrese la edad del paciente: "))
            sintoma = input("Ingrese el síntoma principal del paciente: ")
            prioridad = int(input("Ingrese la prioridad del paciente (1-5): "))
            paciente = Paciente(nombre, edad, sintoma, prioridad)
            clinica.agregarPaciente(paciente)
        case 2:
            clinica.mostrarPacientes()
        case 3:
            clinica.atenderPaciente()
        case 4:
            break
        case default:
            print("Opción no válida. Intente de nuevo.")
