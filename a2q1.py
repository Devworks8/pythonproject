def main():
    sample = [(2, 8), (2, 2), (7, 4), (1, 3), (9, 1)]

    print(incremental_sort(sample))


def incremental_sort(sampleList):
    return sorted(sampleList, key=lambda tupleElement: tupleElement[1])


if __name__ == "__main__":
    main()
