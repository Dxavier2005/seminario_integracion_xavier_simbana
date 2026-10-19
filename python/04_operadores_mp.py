print("OPERADORES")
print("OPERADORES ARITMÉTICOS")

print("+ Suma:", 5, "+", 3, "=", 5 + 3)
print("- Resta:", 5, "-", 3, "=", 5 - 3)
print("* Multiplicación:", 5, "*", 3, "=", 5 * 3)
print("/ División:", 15, "/", 3, "=", 15 / 3)
print("// División entera:", 10, "//", 3, "=", 10 // 3)
print("% Módulo (residuo):", 10, "%", 3, "=", 10 % 3)
print("** Potencia:", 5, "**", 3, "=", 5 ** 3)
print("// División entera:", 5, "//", 3, "=", 5 // 3)



print("Tabla de multiplicar del 5")
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)


print("Operadores de comparación")
print("== Igual a:", 5, "==", 5, "=", 5 == 5)
print("== Igual a:", 5, "==", 4, "=", 5 == 4)
print("!= Distinto de:", 5, "!=", 3, "=", 5 != 3)
print("!= Distinto de:", 5, "!=", 5, "=", 5 != 5)
print("> Mayor que:", 10, ">", 8, "=", 10 > 8)
print("> Mayor que:", 10, ">", 18, "=", 10 > 18)
print("< Menor que:", 10, "<", 18, "=", 10 < 18)
print("< Menor que:", 10, "<", 8, "=", 10 < 8)
print(">= Mayor o igual que:", 10, ">=", 8, "=", 10 >= 8)
print(">= Mayor o igual que:", 10, ">=", 18, "=", 10 >= 18)
print("<= Menor o igual que:", 5, "<=", 3, "=", 5 <= 3)




print("OPERADORES LÓGICOS")
print("Operador and : (5==5) and (4>3) =", (5 == 5) and (4 > 3))
print("Operador and : (5==5) and (4>8) =", (5 == 5) and (4 > 8))
print("Operador or : (5==5) or (4>8) =", (5 == 5) or (4 > 8))
print("Operador or : (5==6) or (4>8) =", (5 == 6) or (4 > 8))
print("Operador not : not (5==6) =", not (5 == 6))
print("Operador not : not (5==5) =", not (5 == 5))


pago_al_dia = True
curso_abierto = True

puede_inscribirse = pago_al_dia and curso_abierto
print("¿Puede inscribirse?", puede_inscribirse)

tiene_beca = True
pago_al_dia = False
exoneracion_aprobada = tiene_beca or pago_al_dia
print("¿Exoneración de cuota aprobada?", exoneracion_aprobada)