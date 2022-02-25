def main():
    sample = ["a","vvv","aaa","car","zoo","dog","plane","BIG","small","hello"]

    print(in_list("big", sample))
    print(in_list("BIG", sample))
    

def in_list(str, sampleList):
    return str in sampleList


if __name__ == "__main__":
    main()
