"""
Manejo de c adena de caracteres
"""

nombre1 ="Qui-Gon Jin"
print(f"Jedi: {nombre1}")
print(f"Tipo de dato: {type(nombre1)}")
nombre2 = "Obi-Wan Kenobi"
print(f"Jedi 2: {nombre2}")
print(f"Tipo de dato: {type(nombre2)}")

###### Funciones comunes de las variables String
print("Funciones comunes de Texto")
droide_1="R2-D2"
droide_2="C-3PO"


longitud_droide_1=len(droide_1)
longitud_droide_2=len(droide_2)
print("nombre droide 1", droide_1)
print("longitud droide 1", longitud_droide_1)
print("nombre droide 2", droide_2)
print("longitud droide 2", longitud_droide_2)

print ("Convertir mayúsculas y minúsculas")
mensaje = "La federacion invade el Planeta Naboo"
mensaje_mayusculas = mensaje.upper()
mensaje_minusculas = mensaje.lower()
print("Mensaje original: ", mensaje)
print("Mensaje en mayúsculas: ", mensaje_mayusculas)
print("Mensaje en minúsculas: ", mensaje_minusculas)


print ("Reemplazo de substrings")
mensaje = "La nave viajara a tatooine"
nuevo_mensaje = mensaje.replace("tatooine", "Coruscant")
print("Mensaje original: ", mensaje)
print("Mensaje Reemplazado: ", nuevo_mensaje)

planetas = "Naboo, Tatooine, Kmino"
print ("Planetas: ", planetas)
lista_planetas = planetas.split(",")
print(lista_planetas)
print("Primer planeta: ", lista_planetas[0])

print("Extraer subcadenas")
mensaje = "Que la fuerza te acompañe"
adjetivo = mensaje[6:11]
verbo = mensaje[20:28]
print ("adjetivo es : ", adjetivo)
print ("verbo es : ", verbo)

print("Comprobación de útiles")
codigo = "R2D2"
numero ="2026"
nombre= "Universidad UTE"
identificador = "DROIDE1"
print(codigo.isalnum())
print(numero.isalnum())
print(nombre.isalnum())
print(identificador.isalnum())
print(identificador.isdigit())
