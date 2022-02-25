def main():

    temp = user_input()
    print("{0}F is {1:.2f}C".format(temp, convert_f_c(temp)))


def convert_f_c(temp):
    return (temp - 32) / 1.8


def user_input():
    temp = ""
    while not isinstance(temp, int):
        try:
            temp = int(input("Enter Fahrenheit Temperature: "))
        except ValueError:
            temp = ""

    return temp


if __name__ == "__main__":
    main()

