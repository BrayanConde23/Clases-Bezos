# Imprimir una lista del 1 - 10.
print (list(range(1,11)))

# Calcular la suma de los números del 1 al 100.
for numero in range(1,100):
    print(f"La suma de 1 + {numero} es {numero+1}")

# Generar una tabla de multiplicar para un número dado.
tablanum = input("Ingrese el numero de la tabla que desea: ")
for numero2 in range(1,11):
    print(f"{tablanum}x{numero2} = {int(tablanum)*numero2}")

# Con el ciclo while realizar un menu para un cajero electrónico que con
#un saldo inicial dado puedan realizar las operaciones de mostrar saldo,
#retirar saldo y consignar a tu propia cuenta.
saldoIni = 150000
opcion = 0

while(opcion != 4):
    opcion = int(input(f"""Seleccione la opcion a ejecutar teniendo en cuenta que {saldoIni} es tu saldo actual:
                       1 Consultar saldo
                       2 Depositar
                       3 Retirar
                       4 Salir
                       :"""))

    if opcion == 1:
        print(f"Su saldo es: {saldoIni}" )
    if opcion == 2:
        depositar = float(input("Ingrese el valor a depositar: "))
        saldoIni = saldoIni + depositar
        print(f"Su saldo es: {saldoIni}")
    if opcion == 3:
        retirar = float(input(f"Ingrese el valor que desea retirar: "))
        saldoFinal = saldoIni - retirar
        if(saldoIni<retirar):
            print("Saldo insuficiente")
        else:
            print(f"Su nuevo saldo es: {saldoFinal}")

    break


if opcion == 4:
    print("Gracias por usar nuestros servicios")

