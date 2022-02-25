def main():

    gallons = user_input()
    print("{0} Gallons is {1:.2f} Liters".format(gallons, convert_g_l(gallons)))


def convert_g_l(gallons):
    return gallons * 3.785


def user_input():
    gallons = ""
    while not isinstance(gallons, int):
        try:
            gallons = int(input("Enter Total Gallons: "))
        except ValueError:
            gallons = ""

    return gallons


if __name__ == "__main__":
    main()

