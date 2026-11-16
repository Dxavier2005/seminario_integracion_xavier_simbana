print("CONDICIONALES IF")
print("Condicionales Simple")
dinero=10
if dinero>=5:
    print("Homero puede comprar una rosquilla")

print("programa finalizó")


creditos = float(input("Ingrese los créditos disponibles: "))
precio_repuesto = float(input("Ingrese repuesto"))

if (creditos >= precio_repuesto):
    print("compra autorizada")

else:
    print("creditos insuficientes")
    print("Buscar soluciones o trueque")


print("Condicional If - elif - else")
print("Condicional Condiciones Anidadas")
combustible =float(input("combustible de la nave: "))

if (combustible >= 75):
    print("optimo")
elif (combustible >= 50):
    print("Suficiente")
elif (combustible >= 20):
    print("Bajo")
else:
    print("Critico")
    print("localiza base mas cercana")



    piloto = input("Ingrese el nombre del piloto: ")
    motor_funciona = input("el motor funciona (si/no): ")
    combustible = input("Combustible disponible")

    if (motor_funciona == "si"):
        print("Motor verificado")
        if  combustible >= 50:
            print("Combustible suficiente")
            print("articipacion Autorizada")
        else:
            print("Debe recargar combustible")
    else:
        print("No puede participar")
        print("El moptor necesita mantenimiento")

