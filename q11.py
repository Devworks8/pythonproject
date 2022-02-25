def main():
    print("{0} is in {1}".format(describe_city("North Bay")[0], describe_city("North Bay")[1]))

    print("{0} is in {1}".format(describe_city("New York", "United States")[0],
                                 describe_city("New York","United States")[1]))

    print("{0} is in {1}".format(describe_city("Paris", "France")[0], describe_city("Paris", "France")[1]))


def describe_city(city, country="Canada"):
    return city, country


if __name__ == "__main__":
    main()

