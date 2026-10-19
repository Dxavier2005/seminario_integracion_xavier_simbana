print ("Incluir datos con input")
nombre = input("¿Cuál es tu nombre? ")
print("!Hola", nombre, "!")
print("Bienvenido a SpringField.")
print("Hasta luego " +nombre)



cantidad = int(input("¿Cuántas rosquillas hay?"))
total = cantidad +5
print("Rosquillas totales: ", total)

print(" Conversaciones ")
print("===== TIENDA DE APU ===================")
nombre_cliente = input ("Nombre del cliente:")
precio = float(input("Precio de la rosquilla:"))
cantidad = int(input("Cantidad:"))
total= cantidad*precio
print("El total a pagar es: ", total) 
print("Totaol a pagar (round): ", round(total,2))
print(f"Total a pagar (f): {total:.2f}")
