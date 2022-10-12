from main_menu import main_menu

def algo():
    menu = main_menu()
    try:
        if menu == 1:
            return 'run function dollars to pesos'
        elif menu == 2:
            return 'run function pesos to dollars'
        else:
            return 'Choose a correct option'
    except ValueError:
        return 'Please, enter an integer number'

def run():
    print(algo())

if __name__ == '__main__':
    run()