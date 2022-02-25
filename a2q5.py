def main ():
    sample = [[1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7], [1]]

    print(get_biggest(sample))


def get_biggest(sampleList):
    return max(sampleList, key=len)


if __name__ == "__main__":
    main()
