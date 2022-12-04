from inspect import cleandoc


def puzzle1(inputList: list):
    numOfOverlaps = 0
    for pair in inputList:
        fElfSections = [i for i in range(int(pair[0].split("-")[0]),
                        int(pair[0].split("-")[1]) + 1, 1)]
        sElfSections = [i for i in range(int(pair[1].split("-")[0]),
                        int(pair[1].split("-")[1]) + 1, 1)]

        contained1 = True
        for e in fElfSections:
            if e not in sElfSections:
                contained1 = False
                break

        contained2 = True
        for e in sElfSections:
            if e not in fElfSections:
                contained2 = False
                break

        if contained1 or contained2:
            numOfOverlaps += 1

    return numOfOverlaps


def puzzle2(inputList: list):
    numOfOverlaps = 0
    for pair in inputList:
        fElfSections = [i for i in range(int(pair[0].split("-")[0]),
                        int(pair[0].split("-")[1]) + 1, 1)]
        sElfSections = [i for i in range(int(pair[1].split("-")[0]),
                        int(pair[1].split("-")[1]) + 1, 1)]

        for e in fElfSections:
            if e in sElfSections:
                numOfOverlaps += 1
                break

    return numOfOverlaps


def main():
    TEST = False

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                            2-4,6-8
                            2-3,4-5
                            5-7,7-9
                            2-8,3-7
                            6-6,4-6
                            2-6,4-8
                        """)

    data = data.split("\n")
    data = [e.split(",") for e in data]

    print(puzzle1(data))
    print(puzzle2(data))


if __name__ == "__main__":
    main()
