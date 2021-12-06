#crear una variable que se llame "pesos" l10
#crear variable "valor_dolar", con el valor de 3875. Este
#valor es la equivalencia en 1 dolar USD l12
#hacer la operacion en base a los dolares que tenemos
#y se crea la variable dolares, que contendrá la operacion l13
#convertir los dolares a un valor de texto, para imprimirlo en consola l15
#Reducir las decimales en el resultado
#usar el comando round, que significa redondear, la variable mas la
#cantidad de decimales que se requiera agregar l14
pesos = input("¿Cuántos pesos colombianos tienes?:  ")
pesos = float(pesos)
valor_dolar = 3875 
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares =str(dolares)
print("Tienes $" + dolares + " dolares")

