#crear una variable que se llame "pesos" 
#crear variable "valor_dolar", con el valor de 3875. Este
#valor es la equivalencia de dolar en pesos colombianos 
#hacer la operacion en base a los dolares que tenemos
#y se crea la variable dolares, que contendrá la operacion 
#Reducir las decimales en el resultado
#usar el comando round, que significa redondear, la variable mas la
#cantidad de decimales que se requiera agregar 
#convertir los dolares a un valor de texto, para imprimirlo en consola 
## challenge: hacer que el programa realice el calculo en la moneda nacional
## precio del dolar al 6 de Dic, 2021 : 21.20
## **pesos colombianos** pesos = input("¿Cuántos pesos colombianos tienes?:  ")
##* agregar varias monedas al conversor
## crear un menu. El menu es una variable
menu = """Welcome to the currency converter 😃💰
1. Pesos colombianos
2. Pesos mexicanos
3. Pesos argentinos
Please! Choice an option:  """
option = input(menu)

if option == "1":
    pesos = input("¿Entry pesos colombianos amount:  ")
    pesos = float(pesos)
    valor_dolar = 3932.78 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares =str(dolares)
    print("You have $" + dolares + " dollars")
elif option == "2":
    pesos = input("Entry pesos mexicanos amount:  ")
    pesos = float(pesos)
    valor_dolar = 21.20 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares =str(dolares)
    print("You have $" + dolares + " dollars")
elif option == "3":
    pesos = input("Entry pesos argentinos amount:  ")
    pesos = float(pesos)
    valor_dolar = 101.25
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares =str(dolares)
    print("You have $" + dolares + " dollars")
else:
    print("Select a correct option please! ")



