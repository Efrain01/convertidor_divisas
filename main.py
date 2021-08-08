#----------FUNCIONES----------#
def menu_divisa(divisa, peso):
    print("CONVERTIDOR DE DIVISA " + divisa + "\n")
    print("Menu de opciones:")
    print("1.- Convertir de pesos " + peso + " a dolares americanos")
    print("2.- Convertir de dolares americanos a pesos " + peso)

def cambio_divisas(peso):
    opcion = int(input("Opcion: "))
    if opcion == 1: 
        pesos = input("Cuantos pesos " + peso + " tienes: ")
        pesos = float(pesos)
        valor_dolar = float(input("Tipo de cambio: 1 dolar equivale a: "))
        dolares = pesos / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes $ " + dolares + " Dolares")
    elif(opcion == 2):
        dolares = input("Cuantos dolares americanos tienes: ")
        dolares = float(dolares)
        valor_dolar = float(input("Tipo de cambio: 1 dolar equivale a: "))
        pesos = dolares * valor_dolar
        pesos = round(pesos, 2)
        pesos = str(pesos)
        print("Tienes $ " + pesos + " Pesos " + peso + ".")
    else: 
        print("Opcion ingresada no valida, por favor verifique si respuesta, gracias ...")
#----------FIN FUNCIONES----------#


def main():
    #----------MENU----------#
    menu = """
                    CONVERTIDOR DE DIVISAS

    Menu de opciones:
    1.- Conversiones Peso mexicano - Dolar
    2.- Conversiones Peso colombiano - Dolar
    3.- Conversiones Peso argentino - Dolar
    """
    #----------FIN MENU----------#

    #----------MAIN----------#
    print(menu, end = "")
    opcion = int(input("Opcion: "))

    if opcion == 1: 
        menu_divisa("MEXICANA", "mexicanos")
        cambio_divisas("mexicanos")
        
    elif opcion == 2: 
        menu_divisa("COLOMBIANA", "colombianos")
        cambio_divisas("colombianos")

    elif opcion == 3: 
        menu_divisa("ARGENTINA", "argentinos")
        cambio_divisas("argentinos")

    else:
        print("Opcion ingresada no valida, por favor verifique si respuesta, gracias ...")    
    #----------FIN MAIN----------#

if __name__ == '__main__':
    main()
    
