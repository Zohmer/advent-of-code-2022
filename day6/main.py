from inspect import cleandoc


def puzzle1(inputList: list):
    marker = []
    for index in range(len(inputList)):
        marker.append(inputList[index])
        if len(marker) > 4:
            marker.pop(0)
        if len(marker) < 4:
            continue
        foundCtr = 0
        for e in marker:
            for i in range(len(marker)):
                if marker[i] == e:
                    foundCtr += 1

        if foundCtr == 4:
            return index+1


def puzzle2(inputList: list):
    marker = []
    for index in range(len(inputList)):
        marker.append(inputList[index])
        if len(marker) > 14:
            marker.pop(0)
        if len(marker) < 14:
            continue
        foundCtr = 0
        for e in marker:
            for i in range(len(marker)):
                if marker[i] == e:
                    foundCtr += 1

        if foundCtr == 14:
            return index+1


def main():
    TEST = False

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""")

    print(puzzle1(data))
    print(puzzle2(data))


if __name__ == "__main__":
    main()
