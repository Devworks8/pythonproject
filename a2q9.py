def main():
    sample = [3, 10 ,4 ,7 ,5 ,7 ,8 ,3 ,3 ,4 ,5 ,9 ,3 ,4 ,9 ,8 ,5]
    print(remove_first_four_even(sample))

def remove_first_four_even(sampleList):
    totalIterations = 4
    iteration = 1
    output = []

    for item in sampleList:
        if iteration > totalIterations or not item % 2 == 0:
            output.append(item)
        else:
            iteration = iteration + 1

    return output

if __name__ == "__main__":
    main()
