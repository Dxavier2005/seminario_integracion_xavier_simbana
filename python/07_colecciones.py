print("Colecciones de datos")
print("Listas")
naves=["N-1", "Transporte", "Naboo"]
print("Naves:", naves)
print("Tipo :", type(naves))
print("Tuplas")
cooredenadas=(15,30,45)
print("Coordenadas:", cooredenadas)
print("Tipo :", type(cooredenadas))
print("Diccionarios")
droide={
    "nombre": "R2-D2",
    "tipo": "Astromecánico",
    "activo": True
}
print("Droide:", droide)
print("Tipo :", type(droide))
print("Conjuntos")
planetas = {
    "Naboo",
    "kmino",
    "Alderaan",
}

print("Planetas:", planetas)
print("Tipo :", type(planetas))

print("CRUD DE LISTAS EN PYTHON")
advengers =[
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitán América", "estado": "Activo"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "Activo"},

]

id_publico = 4
def create():
    global id_publico
    print("Reclutar advenger")
    nombre = input("Nombre del héroe: ")
    heroe = input(" Héroe: ")
    estado = input("estado (activo, retirado, desaparecido): ")
    nuevo_avenger = {
        "id": id_publico,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    advengers.append(nuevo_avenger)
def read():
    print("Lista de advengers")
    for avenger in advengers:
        print(f"{avenger['id']}- nombre: {avenger['nombre']} ")

def update():
    print("Actualizar advenger")
    id_update = int(input("id a modificar: "))
    for avenger in advengers:
        if avenger["id"] == id_update:
            avenger["nombre"] = input("Nuevo nombre: ")
            avenger["heroe"] = input("Nuevo héroe: ")
            avenger["estado"] = input("Nuevo estado: ")
            print("Actualizado")

def delete():
    print("Eliminar advenger")
    id_delete = int(input("id a borrar "))
    for avenger in advengers:
        if avenger["id"] == id_delete:
            advengers.remove(avenger)
            print(" Avenger Eliminado")


def menu():
    while True:
        print("Avengers")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        opcion = int(input("Seleccione 1 al 5 "))

        if opcion == 1:
            create()
        elif opcion == 2:
            read()
        elif opcion == 3:
            update()
        elif opcion == 4:
            delete()
        elif opcion == 5:
            print("Cerrando sistema")
            break
        else:
            print("Intente nueva Opción")

if __name__ == "__main__":
    menu()
