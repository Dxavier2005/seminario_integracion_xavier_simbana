print("Funciones")
print("Autor: Dario Simbaña")

def iniciar_clase():
    print("El catequista da la bienvenida al curso")
    print("¡Comienza la clase!")

iniciar_clase()
iniciar_clase()
iniciar_clase()
iniciar_clase()

def registrar_asistencia(catequizando, clases):
    print(catequizando, "tiene su asistencia registrada")

registrar_asistencia("María", 10)
registrar_asistencia("Juan", 8)
registrar_asistencia("Ana", 12)
registrar_asistencia("Dario Simbaña", 6)

def calcular_total_clases(clases_asistidas, clases_recuperadas):
    total = clases_asistidas + clases_recuperadas
    return total

resultados = calcular_total_clases(4, 6)
print("El total de clases de Dario Simbaña es : ", resultados)
resultado = calcular_total_clases(4, 12)
print("El total de clases de María es : ", resultado)

def verificar_sacramento(nombre, asistencia):
    if asistencia > 75:
        print(f"{nombre} cumple los requisitos para recibir el sacramento")
    else:
        print(f"{nombre} necesita aumentar su asistencia")

verificar_sacramento("Dario Simbaña", 50)
verificar_sacramento("María", 95)




nombre_catequizando: str = "María Fernanda López"
edad: int = 9
cuota: float = 4.5
curso_abierto: bool = True

def calcular_pago_total(cuota: float, meses: int) -> float:
    return cuota * meses

total: float = calcular_pago_total(4.5, 4)
print("Total a pagar calculado: ", total)