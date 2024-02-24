# OPERADORES LOGICOS

# And "y"
condicionalAnd = False and True
print(not condicionalAnd)

# Or "o"
condicionalOr = not ((1 < 2) or (23 >= 2)) 
print(condicionalOr) 

# not "contrario"
condicionalNot = not False
print(not condicionalNot)

# == "Es igual"
esigual = "Brayan" == "brayan"
print(esigual) 

# != "Diferente"
esDiferente = 12 != 12.0
print(esDiferente)

# Operadores de comparacion

# > "Mayor que"
comparadorNum = 1 > 2
print(comparadorNum)

# < "Menor que"
comparadorNum = 5 < 3
print(comparadorNum)

# >= "Menor que o igual"
comparadorNum = 5 <= 3
print(comparadorNum)

# >= " Mayor que o iugal"
comparadorNum = 5 >= 3
print(comparadorNum)


"""
Crear 2 variables numericas de cualquier tipo
y realizar las operaciones aritmeticas basicas
y almacenar ese resultado en una variable que se llame
result e imprimir en consola los resultados
(+ - / // * ** %)
"""

# Variables (2)
variable1 = int(12)
variable2 = int(23)

# Suma
result = variable1 + variable2 
print("La suma de los numeros es:",result)

# Resta
result = variable1 - variable2 
print("La resta de los numeros es:",result)

# Division
result = variable1 / variable2 
print("La division de los numeros es:",result)

# Division entera
result = variable1 // variable2
print("La division de los numeros es:",result)

# Multiplicacion 
result = variable1 * variable2 
print("La multiplicacion de los numeros es:",result)

# Exponenciacion 
result = variable1 ** variable2 
print("La exponenciacion de los numeros es:",result)

# Modulo
result = variable1 % variable2 
print(f"El modulo de los numeros es: {result}") 
