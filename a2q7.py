import random

def main():
    sample = [1, 1, 2, 3, 4, 4, 5, 1]
    print(select_random_num(sample))

def select_random_num(sampleList):
    return random.sample(sampleList, 3)

if __name__ == "__main__":
    main()
