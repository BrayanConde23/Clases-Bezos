# 1. Escribir una función que reciba dos números como argumentos 
#y devuelva su suma.
def numeros(a,b):
    suma = a+b
    return(f"La suma de los numeros es: {suma}")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

print(numeros(a,b))

# 2. Crear una función que tome un número como argudemento
#y devuelva su cuadrado.
def numero(c):
    cuadrado = c**2
    return(f"El cuadrado del numero es: {cuadrado}")
c = int(input("Ingrese un numero: "))

print(numero(c)) 

# 3. Definir una función que tome una lista como argumento
#y devuelva la suma de todos sus elementos.
def listasuma(lista):
    total1= 0
    for elementos in lista:
        total1+= elementos
    return total1

lista = [2,4,6,8,10,12,14,16]
print(listasuma(lista))

# 4. Escribir una función que reciba una lista de números
#y devuelva el mayor de ellos.


# 5. Crear una función que tome una cadena de texto 
#y devuelva su longitud.


# 6. Definir una función que reciba una lista de números 
#y devuelva la cantidad de números pares que contiene.

