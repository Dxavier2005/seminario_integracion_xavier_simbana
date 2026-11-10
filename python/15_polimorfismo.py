class  Guerrero:
    nombre: str
    _poder: str

    def __init__(self, nombre: str, poder: int):
        self.nomre = nombre
        self.raza = poder

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("poder ", self._poder)

    def establecer_poder(self, nuevo_poder: int):
        if nuevo_poder > 0:
            self._poder = nuevo_poder






goku = Guerrero("Goku", "9000")
vegeta = Guerrero("Vegeta", "6000")
piccolo = Guerrero("Piccolo", "10000")
Dario = Guerrero("Dario", "5000")

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
Dario.mostrar_info()

print (goku.nombre)
print(vegeta._poder)


