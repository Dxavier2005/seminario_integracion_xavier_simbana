class  Guerrero:
    nombre: str
    raza: str

    def __init__(self, nombre: str, raza: str):
        self.nomre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)

goku = Guerrero("Goku", "Saiyajin")
vegeta = Guerrero("Vegeta", "Saiyajin")
piccolo = Guerrero("Piccolo", "Namekusein")
Dario = Guerrero("Dario", "Humano")

