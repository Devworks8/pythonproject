def main():
    print("The following is using default arguments\n")
    print("Shirt Size: {0}\nShirt Message: {1}".format(make_shirt()[0],
                                                       make_shirt()[1]))

    print("\nThe following is a Medium shirt using default message argument\n")
    print("Shirt Size: {0}\nShirt Message: {1}".format(make_shirt(size="Medium")[0],
                                                       make_shirt(size="Medium")[1]))

    print("\nThe following is a custom shirt\n")
    print("Shirt Size: {0}\nShirt Message: {1}".format(make_shirt(size="Small", message="Hello World")[0],
                                                       make_shirt(size="Small", message="Hello World")[1]))


def make_shirt(size="Large", message="I love Python"):
    return size, message


if __name__ == "__main__":
    main()

