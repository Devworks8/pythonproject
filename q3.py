def main():
    principle = 10000.0
    cpy = 12.0
    interest = 0.08
    total_years = get_years()

    print("The total amount compounded over {0} year(s) is {1:.2f}".format(total_years,
                                                                           calculate_compound_interest(principle=principle,
                                                                                                       cpy=cpy,
                                                                                                       interest=interest,
                                                                                                       total_years=total_years)))


def calculate_compound_interest(principle, cpy, interest, total_years):
    return principle * (1 + interest / cpy)**(cpy * total_years)


def get_years():
    user_input = ""
    while not isinstance(user_input, int):
        try:
            user_input = int(input("Compound for how many years?: "))
        except ValueError:
            user_input = ""

    return user_input


if __name__ == "__main__":
    main()

