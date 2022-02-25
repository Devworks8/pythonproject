def main():
    sample = ['a@google.com', 'b@yahoo.ca', 'c@amazon.com']
    print(split_email(sample))


def split_email(sampleList):
    ids = []
    domains = []
    for value in sampleList:
        splitEmail = value.split('@')
        ids.append(splitEmail[0])
        domains.append(splitEmail[1])
    return [ids, domains]


if __name__ == "__main__":
    main()
