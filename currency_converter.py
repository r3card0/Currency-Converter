def description():
    program_description= """
    This program makes currency convertion from pesos 
    to dollars
    """
    return program_description

# menu
def menu():
    menu_= int(input("""Welcome to the currency converter 😃💰
    1. Pesos colombianos
    2. Pesos mexicanos
    3. Pesos argentinos
    Please! Choice an option:  """))
    
    return menu_


def run():
    print(description())
    print(menu())

if __name__ == "__main__":
    run()