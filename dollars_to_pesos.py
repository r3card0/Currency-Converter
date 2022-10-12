def dollars_to_pesos():
    try:
        dollars = float(input('Enter dollars amount: '))
        # dollars * pesos = new_pesos_amount
        pesos = float(20.15)
        output = round(dollars * pesos,2)
        return output 
    
    except ValueError:
        return 'Please enter a numerical value'


def run():
    print(dollars_to_pesos())


if __name__ == '__main__':
    run()