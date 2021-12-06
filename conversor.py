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
pesos = input("¿Cuántos pesos mexicanos tienes?:  ")
pesos = float(pesos)
valor_dolar = 21.20 
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares =str(dolares)
print("Tienes $" + dolares + " dolares")

