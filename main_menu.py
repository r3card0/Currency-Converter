def description():
    program_description= """
    This program shows options to convert to dollar to pesos or to pesos to dollars
    """
    return program_description

# menu
def main_menu():
    try:
        menu: int = int(input("""Welcome to the currency converter 😃💰
        1. Dollars to pesos
        2. Pesos to dollars
    
        Please! Choose an option:  """))
    
        return menu

    except ValueError:
        return 'Please, enter an integer number'

def select_option():
    menu = main_menu()
    try:
        if menu == 1:
            return 'Convert dollars to pesos'
        elif menu == 2:
            return 'Convert pesos to dollars'
        else:
            return 'Choose a correct option'
    except ValueError:
        return 'Please, enter an integer number'


def run():
    print(description())
    print(select_option())

if __name__ == "__main__":
    run()