selection = ""

def main():
    show_menu()
    global selection
    while selection != "5":
        user_input()

def show_menu():
    print("Main Menu\n"
          "------------------\n"
          "1) Addition\n"
          "2) Subtraction\n"
          "3) Multiplication\n"
          "4) Division\n"
          "5) Exit\n"
          "------------------\n")

def user_input(menu=True):
    global selection

    if menu:
        selection = input("Selection: ")
        if selection == "1":
            user_input(menu=False)
        elif selection == "2":
            user_input(menu=False)
        elif selection == "3":
            user_input(menu=False)
        elif selection == "4":
            user_input(menu=False)
    else:
        a, b = get_values()
        if selection == "1":
            operation = lambda a, b: a + b
            print("{0} + {1} = {2}".format(a, b, operation(a, b)))
        elif selection == "2":
            operation = lambda a, b: a - b
            print("{0} - {1} = {2}".format(a, b, operation(a, b)))
        elif selection == "3":
            operation = lambda a, b: a * b
            print("{0} * {1} = {2}".format(a, b, operation(a, b)))
        elif selection == "4":
            operation = lambda a, b: a / b
            print("{0} / {1} = {2}".format(a, b, operation(a, b)))

def get_values():
    a = int(input("Enter First Value: "))
    b = int(input("Enter Second Value: "))

    return a, b

if __name__ == "__main__":
    main()

