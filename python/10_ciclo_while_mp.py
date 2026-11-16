def asistir():
    print("El catequizando está asistiendo a clase")

asistencia = 20
while asistencia < 100:
    print("El catequizando está asistiendo a clase")
    asistencia += 20

print("El catequizando alcanzó la asistencia requerida")



while asistencia > 0:
    print("El curso tiene ", asistencia, "% de asistencia registrada")

    asistencia -= 25

print("El curso quedó sin asistencia registrada")


print("Continue y Break")
semana = 0
while semana < 10:
    semana += 1
    if semana == 4:
        print("Semana 4: retiro espiritual, no hay clase")
        continue

    print("Semana ", semana, "el catequizando asiste a clase")
    if semana == 8:
        print("FIN del curso")
        break