for clase in range(1, 6):
    print("El catequizando asiste a la clase", clase)

for mes in range(1, 11):
    print("Cuota mensual", 5, "*", mes, "=", 5 * mes)

for mes in range(1, 11, 3):
    print("Cuota mensual", 5, "*", mes, "=", 5 * mes)

catequizandos = [
    {'id': 1, 'Nombre': 'María Fernanda López', 'Sacramento': 'Primera Comunión', 'estado': 'Activo'},
    {'id': 2, 'Nombre': 'Juan Pablo Torres', 'Sacramento': 'Confirmación', 'estado': 'Activo'},
    {'id': 3, 'Nombre': 'Ana Lucía Vera', 'Sacramento': 'Bautismo', 'estado': 'Activo'}
]

print("====== LISTA DE CATEQUIZANDOS =====")
for catequizando in catequizandos:
    print(f"ID: {catequizando['id']} - Nombre: {catequizando['Nombre']} ({catequizando['Sacramento']})")

catequistas = ["Rosa", "Pedro", "María"]
for catequista in catequistas:
    print("Catequista actual: ", catequista)

asistencia = {
    "María": 95,
    "Juan": 60,
    "Ana": 75,
    "Luis": 45
}

for nombre, porcentaje in asistencia.items():
    if porcentaje >= 75:
        print(nombre, "Puede recibir el sacramento")
    else:
        print(nombre, "Necesita completar la asistencia")


print("Ciclos anidados")
inscritos = ["María", "Juan", "Ana", "Luis", "Sofía", "Pedro"]
for inscrito in inscritos:
    print("Turno de :", inscrito)
    for sesion in range(1, 4):
        print("Sesión", sesion)


print("Break y continue")
for inscrito in inscritos:
    if inscrito == "Luis":
        break
    if inscrito == "Juan":
        continue
    print("Catequizando ", inscrito)