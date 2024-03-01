# Imprimir una lista del 0- 10
lista0_10 = range(11)
print(list(lista0_10))

# Imprimir una lista del 5 - 8
lista5_8 = range(5,9)
print(list(lista5_8))

# Imprimir los multiplos de 5 del 1 al 10
multiplos5 = range(5,51,5)
print(list(multiplos5))

# Imprimir los multiplos de 8 del 1 al 10
multiplos8 = range(8,81,8)
print(list(multiplos8))

# Imprimir los pares entre 20 al 31
pares = range(20,31,2)
impares = range(21,32,2)
print(list(pares))
print(list(impares))

# Conteo regresivo de 5
conteo = range(5,-1,-1)
print(list(conteo)) 

# Conteo regresivo de -10 al -50
conteo = range(-10,-51,-10)
print(list(conteo)) 

for item in range(11):
    print(f"Yo soy el ciclo numero: {item+1}")
    if (item% 2 == 0):
        print("El valor de ciclo es par", item)
    else:
        print("Este valor es impar", item) 

# Tabla de multiplicar del 1 al 10
tablanum = input("Ingrese el numero de la tabla que desea: ")
for numero in range(1,11):
    print(f"{tablanum}x{numero} = {int(tablanum)*numero}")

# Tabla de multiplicar del 5 al 16
tablanum = input("Ingrese el numero de la tabla que desea: ")
for numero in range(5,16):
    result = int(tablanum)*numero
    print(f"{tablanum}x{numero} = {result}")
    if (result < 30):
        pass
    else:
        break
