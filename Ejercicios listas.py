# 1. Suma de elementos: Escribe una función que tome una lista de números y 
#devuelva la suma de todos los elementos.
lista = [2,4,6,8,10,12,14,16]
suma = sum(lista)
print(f"La suma de todos los elementos es: {suma}") 

suma = 0
lista = [2,4,6,8,10,12,14,16]
for lista1 in lista:
    suma+= lista1 
print(f"La suma de todos los elementos es: {suma}")
# 2. Multiplicación de elementos: Escribe una función que tome una lista 
#de números y devuelva el producto de todos los elementos.
multi = 1
lista = [2,4,6,8,10,12,14,16]
for lista1 in lista:
    multi*= lista1 
print(f"La multiplicacion de todos los elementos es: {multi}")

# 3. Inversión de lista: Escribe una función que invierta una lista
#dada con un ciclo.
lista = [2,4,6,8,10,12,14,16]
print(f"Sin invertir: {lista}")
lista.reverse()
print(f"La inversion de la lista es: {lista}")



# 5. Promedio de elementos: Escribe una función que tome una lista de 
#números y devuelva el promedio de esos números.
promedio = 0
lista = [2,4,6,8,10,12,14,16]
for lista1 in lista:
    promedio+= lista1 
print(f"El promedio de los numeros es: {promedio}")
