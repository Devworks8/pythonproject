from itertools import groupby


def main():
    sample = [1,1,1,2,3,4,4,5,5,5,6,7,8,9,9,9]
    print(pack_consecutive_dups(sample))


def pack_consecutive_dups(sampleList):
    return [list(value) for key, value in groupby(sampleList)]


if __name__ == "__main__":
    main()
