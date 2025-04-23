from paciente import Paciente

class Clinica:
    class Nodo:
        def __init__(self, paciente):
            self.paciente = paciente
            self.siguiente = None

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregarPaciente(self, paciente: Paciente):
        nuevo_nodo = self.Nodo(paciente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        print(f"Se registró a {paciente.nombre}.")

    def mostrarPacientes(self):
        if self.cabeza is None:
            print("No hay pacientes en la lista.")
            return
        print("Lista de pacientes:")
        actual = self.cabeza
        while actual:
            print(actual.paciente.imprimirInformacion())
            actual = actual.siguiente
    
    def atenderPaciente(self):
        if self.cabeza is None:
            print("No hay pacientes en la lista.")
            return
        pacienteAtendido = self.cabeza.paciente
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        print(f"Se atendió a: {pacienteAtendido.imprimirInformacion()}")