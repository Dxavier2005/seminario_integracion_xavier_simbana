"""
Manejo de cadena de caracteres
"""

nombre1 ="Juan Pérez"
print(f"Estudiante: {nombre1}")
print(f"Tipo de dato: {type(nombre1)}")
nombre2 = "María González"
print(f"Estudiante 2: {nombre2}")
print(f"Tipo de dato: {type(nombre2)}")

###### Funciones comunes de las variables String
print("Funciones comunes de Texto")
sacramento_1="Bautismo"
sacramento_2="Confirmación"


longitud_sacramento_1=len(sacramento_1)
longitud_sacramento_2=len(sacramento_2)
print("nombre sacramento 1", sacramento_1)
print("longitud sacramento 1", longitud_sacramento_1)
print("nombre sacramento 2", sacramento_2)
print("longitud sacramento 2", longitud_sacramento_2)

print ("Convertir mayúsculas y minúsculas")
mensaje = "La Iglesia Católica celebra los siete sacramentos"
mensaje_mayusculas = mensaje.upper()
mensaje_minusculas = mensaje.lower()
print("Mensaje original: ", mensaje)
print("Mensaje en mayúsculas: ", mensaje_mayusculas)
print("Mensaje en minúsculas: ", mensaje_minusculas)


print ("Reemplazo de substrings")
mensaje = "El estudiante recibirá el sacramento del bautismo"
nuevo_mensaje = mensaje.replace("bautismo", "matrimonio")
print("Mensaje original: ", mensaje)
print("Mensaje Reemplazado: ", nuevo_mensaje)

sacramentos = "Bautismo, Confirmación, Eucaristía"
print ("Sacramentos: ", sacramentos)
lista_sacramentos = sacramentos.split(",")
print(lista_sacramentos)
print("Primer sacramento: ", lista_sacramentos[0])

print("Extraer subcadenas")
mensaje = "Los sacramentos fortalecen nuestra fe"
adjetivo = mensaje[4:15]
verbo = mensaje[16:26]
print ("adjetivo es : ", adjetivo)
print ("verbo es : ", verbo)

print("Comprobación de útiles")
codigo = "SAC2026"
numero ="2026"
nombre= "Iglesia Catolica"
identificador = "CURSO01"
print(codigo.isalnum())
print(numero.isalnum())
print(nombre.isalnum())
print(identificador.isalnum())
print(identificador.isdigit())