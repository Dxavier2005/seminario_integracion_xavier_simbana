print("CRUD DE LISTAS EN PYTHON")
sacramentos = [
    {"id": 1, "nombre": "Juan Pérez", "sacramento": "Bautismo", "estado": "Activo"},
    {"id": 2, "nombre": "María González", "sacramento": "Confirmación", "estado": "Activo"},
    {"id": 3, "nombre": "Pedro Sánchez", "sacramento": "Eucaristía", "estado": "Activo"},
]
id_publico = 4
def create():
    id = 4
    print("Registrar estudiante")
    nombre = input("Nombre estudiante: ")
    sacramento = input("Sacramento: ")
    estado = input("Estado (Activo, Retirado, Finalizado)")
    nuevo_sacramento = {
        "id": id_publico,
        "nombre": nombre,
        "sacramento": sacramento,
        "estado": estado
    }
    sacramentos.append(nuevo_sacramento)
    print("Creado")

def read():
    print("Lista de estudiantes")
    for sacramento in sacramentos:
        print(f"{sacramento["id"]} - nombre : {sacramento["nombre"]}")

def update():
    print("Actualizar estudiante")
    id_update = int(input("id a modificar: "))
    for sacramento in sacramentos:
        if (sacramento[id]==id_update):
            sacramento["nombre"] = input("Nuevo nombre")
            sacramento["sacramento"] = input("Nuevo sacramento")
            sacramento["estado"] = input("Nuevo estado")
            print("Actualizado")

def delete():
    print("Eliminar estudiante")
    id_delete = int(input("id a borrar"))
    for sacramento in sacramentos:
        if (sacramento[id]==id_delete):
            sacramentos.remove(sacramento)
            print("Estudiante eliminado")
def menu():
    while True:
        print("Control de Curso Sacramentos en la Iglesia Católica")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        option = input("Seleccione 1 al 5")
        if option=="1":
            create()
        elif option=="2":
            read()
        elif option=="3":
            update()
        elif option=="4":
            delete()
        elif option=="5":
            print("Cerrando sistema")
            break
        else:
            print("Intente nueva opcion")

if __name__ == "__main__":
    menu()