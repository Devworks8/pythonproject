from itertools import groupby
from operator import itemgetter
from collections import OrderedDict


def main():
    sample = ["c", "ask", "be", "apple", "a", "ball", "come", "badminton", "b"]

    print(alphabetically_sorted(sample))


def alphabetically_sorted(sampleList):
    groups = {}
    for k, v in groupby(sampleList, key=itemgetter(0)):
        groups.setdefault(k, []).extend(v)

    od = OrderedDict(sorted(groups.items()))
    output = ""
    for item in od.values():
        for value in sorted(item, key=len):
            output = output + value + "\n"

        output = output + "\n"

    return output


if __name__ == "__main__":
    main()
