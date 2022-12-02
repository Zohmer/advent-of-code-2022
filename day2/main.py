from inspect import cleandoc


def puzzle1(inputList: list):
    score = 0
    for e in inputList:
        score += calcScore(e[0], e[1])
    return score


def puzzle2(inputList: list):
    optimalMove = [
        {
            "A": "Z",
            "B": "X",
            "C": "Y"
        },
        {
            "A": "X",
            "B": "Y",
            "C": "Z"
        },
        {
            "A": "Y",
            "B": "Z",
            "C": "X"
        },
    ]
    score = 0
    for e in inputList:
        if e[1] == "X":
            score += calcScore(e[0], optimalMove[0][e[0]])
        elif e[1] == "Y":
            score += calcScore(e[0], optimalMove[1][e[0]])
        else:
            score += calcScore(e[0], optimalMove[2][e[0]])
    return score


def calcScore(oMove: str, pMove: str):
    pointVals = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    if (
        (pMove == "X" and oMove == "C")
        or (pMove == "Y" and oMove == "A")
        or (pMove == "Z" and oMove == "B")
    ):
        return 6 + pointVals[pMove]
    elif (
        (pMove == "X" and oMove == "A")
        or (pMove == "Y" and oMove == "B")
        or (pMove == "Z" and oMove == "C")
    ):
        return 3 + pointVals[pMove]
    else:
        return pointVals[pMove]


def main():
    TEST = False

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                            A Y
                            B X
                            C Z
                        """)

    data = data.split("\n")
    data = [e.split(" ") for e in data]

    print(puzzle1(data))
    print(puzzle2(data))


if __name__ == "__main__":
    main()
