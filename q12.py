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
            print("{0} + {1} = {2}".format(a, b, addition(a, b)))
        elif selection == "2":
            print("{0} - {1} = {2}".format(a, b, subtraction(a, b)))
        elif selection == "3":
            print("{0} * {1} = {2}".format(a, b, multiplication(a, b)))
        elif selection == "4":
            print("{0} / {1} = {2}".format(a, b, division(a, b)))


def get_values():
    a = input("Enter First Value: ")
    b = input("Enter Second Value: ")

    return a, b


def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(a) - int(b)


def multiplication(a, b):
    return int(a) * int(b)


def division(a, b):
    return int(a) / int(b)


if __name__ == "__main__":
    main()

