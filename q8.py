from random import randint, seed


def main():
    for roll in range(5):
        print("Roll #{0}: {1}".format(roll + 1, roll_weighted_die()))


def roll_weighted_die():
    seed(1)
    return randint(1, 6)


if __name__ == "__main__":
    main()

