# 1. Cree un programa que ingresando un numero me diga si es mayor o menor de edad.
numero = int (input("Ingrese su edad: "))
if numero >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# 2. Cree un programa que ingresando un numero me diga si es impar o par.
numero1 = int(input("Ingrese un numero: "))
if numero1 % 2==0:
    print("Su numero es par")
else:
    print("Su numero es impar")

# 3. Cree un programa que me reciba el nombre de una persona y su nota del curso si se 
#llama "Pepito" y la nota es mayor a 3 imprima "Felicidades (nombre) aprobaste el curso".
nombre = input("Ingrese su nombre: ")
nota = float(input("Nota del curso: "))
if nombre == "Pepito" and nota >3:
    print(f"Felicidades {nombre} aprobaste el curso.")
else:
    print("No te llamas pepito y/o no aprobaste el curso") 

