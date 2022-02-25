import random

subdivision = {}


def main():
    for i in range(25):
        subdivision[str(i)] = random.randint(0, 500)

    while True:
        show_menu()


def show_menu():
    menu = "Main menu\n" \
           "----------------------\n" \
           "1) New Subdivision\n" \
           "2) Update Subdivision\n" \
           "3) Display Data\n" \
           "4) Get Size\n" \
           "0) Exit\n" \
           "----------------------\n" \

    print(menu)
    parse_input(input("Option: "))


def parse_input(option):
    if option == "1":
        sd = input("Subdivision: ")
        trees = input("Total trees: ")
        update_info(sd, trees)
    elif option == "2":
        sd = input("Subdivision: ")
        trees = input("Total trees: ")
        update_info(sd, trees, True)
    elif option == "3":
        print_data(subdivision)
    elif option == "4":
        print(get_size())
    elif option == "0":
        exit(0)


def update_info(id, trees, update=False):
    if update:
        if id in subdivision.keys():
            subdivision[id] = trees
        else:
            print("\nSubdivision not found.")
            input()
    else:
        if id in subdivision.keys():
            if input("Subdivision exists. Do you wish to overwrite? (y/n): ") == 'n':
                return

        subdivision[id] = trees


def print_data(subdivisions):
    for sd in subdivisions:
        print("Subdivision: {0}, Trees: {1}".format(sd, subdivisions[sd]))

    input()


def get_size():
    return "Total size is {0}\n".format(len(subdivision))


if __name__ == "__main__":
    main()
