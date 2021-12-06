#crear una variable que se llame "pesos"
pesos = input("¿Cuántos pesos colombianos tienes?:  ")
pesos = float(pesos)
#crear variable "valor_dolar", con el valor de 3875. Este
#valor es la equivalencia en 1 dolar USD
valor_dolar = 3875
#hacer la operacion en base a los dolares que tenemos
#y se crea la variable dolares, que contendrá la operacion
dolares = pesos / valor_dolar
#convertir los dolares a un valor de texto, para imprimirlo en consola
dolares =str(dolares)
print("Tienes $" + dolares + " dolares")