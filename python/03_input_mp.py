print("Incluir datos con input")
nombre = input("¿Cuál es tu nombre? ")
print("¡Hola", nombre, "!")
print("Bienvenido al Sistema de Control de Cursos de Sacramentos.")
print("Hasta luego " + nombre)



cantidad = int(input("¿Cuántos catequizandos hay inscritos? "))
total = cantidad + 5
print("Catequizandos totales: ", total)

print(" Conversiones ")
print("===== CAJA DE LA PARROQUIA ===================")
nombre_catequizando = input("Nombre del catequizando: ")
cuota = float(input("Cuota mensual del curso: "))
cantidad = int(input("Cantidad de meses a pagar: "))
total = cantidad * cuota
print("El total a pagar es: ", total)
print("Total a pagar (round): ", round(total, 2))
print(f"Total a pagar (f): {total:.2f}")