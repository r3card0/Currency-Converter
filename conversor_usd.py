dolares = input("¿Cuántos dólares USD tienes?:  ")
dolares = float(dolares)
dollar_value = 21.20
pesos_mx = round(dolares * dollar_value, 2)
pesos_mx = str(pesos_mx)
print("Tienes " + pesos_mx + " pesos mexicanos")