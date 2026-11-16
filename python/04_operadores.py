print("OPERADORES")
print("OPERADORES ARITMETICOS")

print("+ Suma:", 5, "+", 3, "=", 5+3)
print("- Resta:", 5, "-", 3, "=", 5-3)
print("* Multiplicación:", 5, "*", 3, "=", 5*3)
print("/ División:", 15, "/", 3, "=", 15/3)
print("// División entera:", 10, "//", 3, "=", 10//3)
print("% Módulo:", 10, "%", 3, "=", 10%3)
print("** Residuo:", 5, "**", 3, "=", 5**3)
print("// Potencia:", 5, "//", 3, "=", 5//3)



print("Tabla multiplicar del 5")
print("5 x 1 =", 5*1)
print("5 x 2 =", 5*2)   
print("5 x 3 =", 5*3)
print("5 x 4 =", 5*4)
print("5 x 5 =", 5*5)
print("5 x 6 =", 5*6)
print("5 x 7 =", 5*7)
print("5 x 8 =", 5*8)
print("5 x 9 =", 5*9)
print("5 x 10 =", 5*10)


print("Opredadores de comparación")
print("== Igualdad a:", 5, "==", 5, "=", 5==5)
print("== Igual a:", 5, "==", 4, "=", 5==4)
print("!= Iguala a:", 5, "!=", 3, "=", 5!=4)
print("!= Iguala a:", 5, "!=", 5, "=", 5!=5)
print("> Mayor que:", 10, ">", 8, "=", 10>8)
print("> Mayor que:", 10, ">", 18, "=", 10>18)
print("< Menor que:", 10, "<", 18, "=", 10<18)
print("< Menor que:", 10, "<", 18, "=", 10<18)
print(">= Mayor o igual que:", 10, ">=", 8, "=", 10>=8)
print(">= Mayor o igual que:", 10, ">=", 18, "=", 10>=8)
print("<= Menor o igual que:", 5, "<=", 3, "=", 5<=3)




print("OPERADORES LOGICOS")
print("Operadores and : (5==5) and (4>3) =", (5==5) and (4>3))
print("Operadores and : (5==5) and (4>8) =", (5==5) and (4>8))
print("Operadores or : (5==5) or (4>8) =", (5==5) or (4>8))
print("Operadores or : (5==6) or (4>8) =", (5==5) or (4>8))
print("Operadores not : not (5==6) =", not (5==6))
print("Operadores not : not (5==5) =", not (5==5))


tiene_dinero=True
tiene_abierta=True

puede_comprar = tiene_dinero and tienda_abierta
print("¿Puede comprar?", puede_comprar)

es_cliente_vip= True
tiene_dinero=False
acceso_credito= es_cliente_vip or tiene_dinero
print("¿Credito aprobado?", acceso_credito)

