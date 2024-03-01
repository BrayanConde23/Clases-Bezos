# 1. Calculadora Básica: Diseñar un diagrama de flujo para una calculadora básica que 
#pueda realizar operaciones de suma, resta, multiplicación y división 
#con dos números dados por el usuario.
numero1 = float(input("Digite un numero: "))
numero2 = float(input("Digite otro numero: "))

suma = numero1 + numero2
print(f"La suma de los dos numeros es {suma}.")

resta = numero1 - numero2
print (f"La resta de los numeros es {resta}.")

multiplicacion = numero1 * numero2
print (f"La multiplicacion de los numeros es {multiplicacion}.")

division = numero1 / numero2
print (f"La division de los numeros es {division}.")

# 2. Conversión de Temperatura: Crear un diagrama de flujo que convierta la temperatura de
#Celsius a Fahrenheit y viceversa, según la elección del usuario. 
#Grados centígrados = (grados Fahrenheit − 32) × 5/9.
celsius = float(input("Ingrese los grados Celsius: "))
fahrenheit = float(input("Ingrese los grados Fahrenheit: "))

convCelsius = (celsius * 1.8) + 32

convFahrenheit = (fahrenheit - 32) * 0.555

eleccion = print(input("""¿Que conversion quiere hacer:
                       1 Celsius
                       2 Fahrenheit
                       : """))

if eleccion == 1:
    print(f"{celsius} grados Celsius son {convCelsius} grados Fahrenheit.")
else:
    print(f"{fahrenheit} grados Fahrenheit son {convFahrenheit} grados Celsius.")


# 3. Verificación de Edad: Desarrollar un diagrama de flujo que determine si una persona
#es mayor de edad (18 años o más) basándose en la edad ingresada por el usuario.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Eres menor de edad.") 

# 4. Cálculo de Promedio: Diseñar un diagrama de flujo que calcule el promedio de 
#tres números (a,b,c) proporcionados por el usuario. Promedio = (a + b + c) / 3.
numeros = float(input("""Ingrese un numero:
Ingrese otro numero: 
Ingrese un ultimo numero: 
"""))