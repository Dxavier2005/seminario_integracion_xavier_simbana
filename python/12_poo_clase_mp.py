class Catequizando:
    nombre: str
    sacramento: str

    def __init__(self, nombre: str, sacramento: str):
        self.nombre = nombre
        self.sacramento = sacramento

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Sacramento ", self.sacramento)

maria = Catequizando("María Fernanda López", "Primera Comunión")
juan = Catequizando("Juan Pablo Torres", "Confirmación")
ana = Catequizando("Ana Lucía Vera", "Bautismo")
dario = Catequizando("Dario", "Matrimonio")