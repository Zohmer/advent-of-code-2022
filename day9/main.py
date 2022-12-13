from inspect import cleandoc


def puzzle1(inputList: list):
    pass


def puzzle2(inputList: list):
    pass


def calcTailPos(headCoords: list, tailCoords: list) -> list:
    if (
        tailCoords[0] >= headCoords[0] - 1
        and tailCoords[0] <= headCoords[0] + 1
        and tailCoords[1] >= headCoords[1] - 1
        and tailCoords[1] <= headCoords[1] + 1
    ):
        return tailCoords

    if (
        tailCoords[0] < headCoords[0] - 1
        and tailCoords[1] < headCoords[1] - 1
    ):
        tailCoords[0] += 1
        tailCoords[1] += 1
        return tailCoords
    if (
        tailCoords[0] > headCoords[0] + 1
        and tailCoords[1] > headCoords[1] + 1
    ):
        tailCoords[0] -= 1
        tailCoords[1] -= 1
        return tailCoords
    if (
        tailCoords[0] < headCoords[0] - 1
        and tailCoords[1] > headCoords[1] + 1
    ):
        tailCoords[0] += 1
        tailCoords[1] -= 1
        return tailCoords
    if (
        tailCoords[0] > headCoords[0] + 1
        and tailCoords[1] < headCoords[1] - 1
    ):
        tailCoords[0] -= 1
        tailCoords[1] += 1
        return tailCoords

    if tailCoords[0] < headCoords[0] - 1:
        tailCoords[0] += 1
        return tailCoords
    if tailCoords[0] > headCoords[0] + 1:
        tailCoords[0] -= 1
        return tailCoords
    if tailCoords[1] < headCoords[1] - 1:
        tailCoords[1] += 1
        return tailCoords
    if tailCoords[1] > headCoords[1] + 1:
        tailCoords[1] -= 1
        return tailCoords


def main():
    TEST = True

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                            R 4
                            U 4
                            L 3
                            D 1
                            R 4
                            D 1
                            L 5
                            R 2
                        """)

    data = data.split("\n")
    data = [e.split(" ") for e in data]


if __name__ == "__main__":
    main()
