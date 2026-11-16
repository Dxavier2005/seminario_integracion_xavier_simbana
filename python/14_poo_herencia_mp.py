class Catequizando:
    nombre: str
    _sacramento: str

    def __init__(self, nombre: str, sacramento: str):
        self.nombre = nombre
        self._sacramento = sacramento

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Sacramento ", self._sacramento)


class CatequizandoComunion(Catequizando):
    def __init__(self, nombre: str, sacramento: str):
        super().__init__(nombre, sacramento)

    def muestra_nombre(self):
        print("Nombre: ", self.nombre)


maria = CatequizandoComunion("María Fernanda López", "Primera Comunión")
juan = CatequizandoComunion("Juan Pablo Torres", "Primera Comunión")
maria.mostrar_info()
juan.mostrar_info()
maria.muestra_nombre()
juan.muestra_nombre()

print(maria.nombre)
print(juan._sacramento)