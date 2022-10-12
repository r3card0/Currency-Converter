def description():
    program_description= """
    This program shows options to convert to dollar to pesos or to pesos to dollars
    """
    return program_description

# menu
def menu_1():
    menu: int = int(input("""Welcome to the currency converter 😃💰
    1. Dollars to pesos
    2. Pesos to dollars
    
    Please! Choose an option:  """))
    
    return menu

def select_option():
    menu = menu_1()
    if menu == 1:
        print('Convert dollars to pesos')
    elif menu == 2:
        print('Convert pesos to dollars')
    else:
        print('Choose a correct option')


def run():
    print(description())
    print(select_option())

if __name__ == "__main__":
    run()