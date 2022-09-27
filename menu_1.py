def description():
    program_description= """
    This program shows options to convert to dollar to pesos or to pesos to dollars
    """
    return program_description

# menu
def menu_1():
    menu_= int(input("""Welcome to the currency converter 😃💰
    1. Dollars to pesos
    2. Pesos to dollars
    
    Please! Choose an option:  """))
    
    return menu_


def run():
    print(description())
    print(menu_1())

if __name__ == "__main__":
    run()