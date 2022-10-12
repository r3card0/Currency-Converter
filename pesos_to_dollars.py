def pesos_to_dollars():
    try:
        pesos_enter = float(input('Please enter the amount of pesos: '))
        # dollars = pesos_enter / pesos
        pesos = float(20.15)
        dollars = round(pesos_enter / pesos,2)
        return dollars
    
    except ValueError:
        return 'Please enter a numerical value'

def run():
    print(pesos_to_dollars())


if __name__ == '__main__':
    run()