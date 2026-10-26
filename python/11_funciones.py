print ("FUnciones")
print ("Autor: Dario Simbaña")

def  kamehameha():
    print("Goku concentra su energìa")
    print("!KAmehameha")

kamehameha()
kamehameha()
kamehameha()
kamehameha()

def atacar (guerrero, poder):
    print(guerrero, "realiza un ataque")

atacar("Goku")
atacar("Vegeta")
atacar("Piccolo")
atacar("Dario Simbaña")

def calcular_poder(poder, ataques):
    danio = poder + ataques
    return danio

resultados = calcular_poder(4, 26)
print ("El poder Dario Simbaña es : ", resultados)
resultado = calcular_poder(4 , 5000)
print ("EL poder de GOku es : ", resultado)

def transformar_saiyajin(nombre, poder): 
    if poder > 9000:
        print(f"Transformacion de {nombre} en Super Saiyajin exitosa")
    else:
        print(f"{nombre} necesitra aumentar el poder")

transformar_saiyajin("Dario Simbaña", 5000)
transformar_saiyajin("Gohan", 15000)




nombre_personaje: str = "Goku"
edad: int = 33
altura: float = 1.75
es_activa: bool = True

def multiplicador_poder(entrenamiento: float,edad: int)-> float:
    return entrenamiento * edad

poder: float = multiplicador_poder(15.5, 2)
print("Pder calculado: ", poder)
