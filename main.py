menu = """
                CONVERTIDOR DE DIVISAS

Menu de opciones:
1.- Conversiones Peso mexicano - Dolar
2.- Conversiones Peso colombiano - Dolar
3.- Conversiones Peso argentino - Dolar
"""

menu_divisa_mexicana = """
            CONVERTIDOR DE DIVISA MEXICANA

Menu de opciones:
1.- Convertir de pesos mexicanos a dolares americanos
2.- Convertir de dolares americanos a pesos mexicanos
"""

menu_divisa_colombiana = """
            CONVERTIDOR DE DIVISA COLOMBIANA

Menu de opciones:
1.- Convertir de pesos colombianos a dolares americanos
2.- Convertir de dolares americanos a pesos colombianos
"""

menu_divisa_argentina = """
            CONVERTIDOR DE DIVISA ARGENTINA

Menu de opciones:
1.- Convertir de pesos argentinos a dolares americanos
2.- Convertir de dolares americanos a pesos argentinos
"""

print(menu, end = "")
opcion = int(input("Opcion: "))

if opcion == 1: 
    print(menu_divisa_mexicana, end = "")
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
elif opcion == 2: 
    print(menu_divisa_colombiana, end = "")
    opcion = int(input("Opcion: "))
    if opcion == 1: 
        pesos = input("Cuantos pesos colombianos tienes: ")
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
        print("Tienes $" + pesos + " Pesos colombianos")
    else: 
        print("Opcion ingresada no valida, por favor verifique si respuesta, gracias ...")
elif opcion == 3: 
    print(menu_divisa_argentina, end = "")
    opcion = int(input("Opcion: "))
    if opcion == 1: 
        pesos = input("Cuantos pesos argentinos tienes: ")
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
        print("Tienes $" + pesos + " Pesos argentinos")
    else: 
        print("Opcion ingresada no valida, por favor verifique si respuesta, gracias ...")
else:
    print("Opcion ingresada no valida, por favor verifique si respuesta, gracias ...")    