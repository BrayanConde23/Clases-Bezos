lista = ["Brayan", 17, False, "Masculino", [7,10,23]]
print(lista[0])
print(lista[3])
lista[3] = 3044671830
print(lista[3])

#INSERT.
lista.insert(0, 1020223692)
print(lista[0])

#APPEND
lista.append("Casa")
print(lista)

#EXTEND
lista2 = ["Hola", "Chao"]
lista.extend(lista2)
print(lista)

#DEL
print(lista)
del lista[3]
print(lista)

#REMOVE
lista.remove(17)
print(lista)

#CLEAR
lista.clear()
print(lista) 


#POP
eliminado = lista.pop(1)
print(lista)
print(eliminado)

#LEN (FUNCION)
print(len(lista))

#: (FUNCION)
print(lista)
print(lista[0:2])

#SORT
lista3 = [2.3, 3, 4.5, 1, 1.5, 2, 3.5, 5.5, 4]
print(lista3)
lista3.sort()
print(lista3)

lista = [1,2.3,"Hola",True]

entero = 100
flotante = 12.3
texto = "Adios"
boleano = False
listainterna = ["Estoy dentro", True]

lista2 = [entero,flotante,texto,boleano,listainterna]
#print(lista2)

#print(lista2[9])
#print(lista2[1:4])
#print(lista[-1])
#print(lista[-4])
#lista[-1] = 123456789
#print(lista)
#lista[0:4] = [12]
#print(lista)
#lista[:] =[]
#print(lista)
