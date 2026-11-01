class Catequizando:
    nombre: str
    _asistencia: int

    def __init__(self, nombre: str, asistencia: int):
        self.nombre = nombre
        self._asistencia = asistencia

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Asistencia ", self._asistencia)

    def establecer_asistencia(self, nueva_asistencia: int):
        if nueva_asistencia > 0:
            self._asistencia = nueva_asistencia






maria = Catequizando("María Fernanda López", 90)
juan = Catequizando("Juan Pablo Torres", 60)
ana = Catequizando("Ana Lucía Vera", 100)
dario = Catequizando("Dario", 50)

maria.mostrar_info()
juan.mostrar_info()
ana.mostrar_info()
dario.mostrar_info()

print(maria.nombre)
print(juan._asistencia)