def main():
    string = "student"
    sample = [1,2,3,4]

    print(insert_into(string, sample))


def insert_into(string, sampleList):
    output = []
    for value in sampleList:
        output.append(string + str(value))

    return output


if __name__ == "__main__":
    main()
