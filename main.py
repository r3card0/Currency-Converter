from main_menu import main_menu
from dollars_to_pesos import dollars_to_pesos
from pesos_to_dollars import pesos_to_dollars

def algo():
    menu = main_menu()
    try:
        if menu == 1:
            return dollars_to_pesos()
        elif menu == 2:
            return pesos_to_dollars()
        else:
            return 'Choose a correct option'
    except ValueError:
        return 'Please, enter an integer number'

def run():
    print(algo())

if __name__ == '__main__':
    run()