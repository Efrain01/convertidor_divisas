print("CONVERTIDOR DE DIVISAS\n")
print("Menu de opciones:\n")
print("1.- Convertir de pesos mexicanos a dolares americanos\n")
print("2.- Convertir de dolares americanos a pesos mexicanos\n")
opcion = int(input("Opcion: "))

pesos = input("Cuantos pesos mexicanos tienes: ")
pesos = float(pesos)
valor_dolar = 20.04
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " Dolares")
