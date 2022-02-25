def main():
    sample = ['Red', 'Green', 'Blue', 'White', 'Black']
    print(reverse_string(sample))
    

def reverse_string (sampleList):
    return list(map(lambda string: "".join(reversed(string)), sampleList))


if __name__ == "__main__":
    main()
