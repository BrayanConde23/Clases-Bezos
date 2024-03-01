lista = [7,10,9]

print(lista)
print(len(lista))
print("Con lista[-1]:",lista[-1])
print("Con ultima posicion lista[-6]:",lista[-3])

for i in range(2,-1,-1):
    print(lista[i])
    lista.append(lista[i])
range(3,41,3)
range(40,2,-3)

# Practica.
listaNormal = [3,-2,1,-1,0,4]
#listaNormal.reverse()
listaInvertida = []

for posiciones in range(len(listaNormal)-1, -1 ,-1):
    listaInvertida.append(listaNormal[posiciones])

print(listaNormal)
print(listaInvertida)

#FUNCIONES.

#Sin argumentos:
def saludar():
    print("Benjamin Navarro hdp")

saludar()
#Con argumentos:
def saludoPersonalizado(nombre):
    print(f"Bienvenidos a los juegos del hambre {nombre}")

nombreuser = input("Digite su nombre: ")
saludoPersonalizado(nombreuser)
saludoPersonalizado("Brayan")
saludoPersonalizado(911) 

#Con retornos:
def esPar(numero):
    if numero % 2==0:
        return f"El numero {numero} es par"

print(esPar(911))

def esImpar():
    numero = int(input("Ey, dime un numero: "))
    if not (numero % 2==0):
        print (f"El numero {numero} es impar")

    else:
        print (f"El numero {numero} es par")

esImpar()

#CREAR UNA FUNCION QUE DIGA SI ES MAYOR DE EDAD.
#DEBE RECIBIR LA EDAD DEL USUARIO COMO PARAMETRO.
#SI ES MAYOR = "ERES MAYOR DE EDAD".
def edad():
    numero = int(input("Digite su edad: "))
    if numero >=18:
        print ("Eres mayor de edad")

edad()

def mayorEdad(edad):
    if edad >=18:
        print ("Eres mayor de edad")
    
edad = int(input("Ingresa tu edad: "))
mayorEdad(edad)
