from random import randint


def main():
    string = user_input()
    print("Random picked character: {0}".format(string[randint(0, len(string) - 1)]))


def user_input():
    return input("Enter a String: ")


if __name__ == "__main__":
    main()

