def main():
    print("The following is using positional arguments\n")
    print("Shirt Size: {0}\nShirt Message: {1}".format(make_shirt("Large", "Hello")[0],
                                                       make_shirt("Large", "Hello")[1]))

    print("\nThe following is using keyword arguments\n")
    print("Shirt Size: {0}\nShirt Message: {1}".format(make_shirt(size="Small", message="World")[0],
                                                       make_shirt(size="Small", message="World")[1]))


def make_shirt(size, message):
    return size, message


if __name__ == "__main__":
    main()

