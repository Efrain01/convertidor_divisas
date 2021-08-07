print("CONVERTIDOR DE DIVISAS\n")
print("Menu de opciones:\n")
print("1.- Convertir de pesos mexicanos a dolares americanos\n")
print("2.- Convertir de dolares americanos a pesos mexicanos\n")
opcion = int(input("Opcion: "))
if opcion == 1: 
    pesos = input("Cuantos pesos mexicanos tienes: ")
    pesos = float(pesos)
    valor_dolar = float(input("Tipo de cambio: 1 dolar equivale a: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif(opcion == 2):
    dolares = input("Cuantos dolares americanos tienes: ")
    dolares = float(dolares)
    valor_dolar = float(input("Tipo de cambio: 1 dolar equivale a: "))
    pesos = dolares * valor_dolar
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " Pesos mexicanos")
else: 
    print("Opcion ingresada no valida, por favor verifique si respuesta, gracias ...")



    