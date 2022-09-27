def description():
    program_description= """
    This program shows options to convert dollars
    """
    return program_description

# menu
def menu_2():
    menu_= int(input("""Welcome to the currency converter 😃💰
    1. Pesos colombianos
    2. Pesos mexicanos
    3. Pesos argentinos
    Please! Choice an option:  """))
    
    return menu_


def run():
    print(description())
    print(menu_2())

if __name__ == "__main__":
    run()