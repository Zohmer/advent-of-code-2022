from inspect import cleandoc


def puzzle1(initState: list, moves: list):
    for e in initState:
        if e[0] == '1':
            pos = e[0].split("  ")
            crateIndex = initState.index(e) - 1
            crates = [[] for item in pos]
            break

    while crateIndex >= 0:
        for i in range(len(initState[crateIndex])):
            if initState[crateIndex][i] == '[':
                crates


def puzzle2(inputList: list):
    pass


def main():
    TEST = True

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                                [D]    
                            [N] [C]    
                            [Z] [M] [P]
                            1   2   3 

                            move 1 from 2 to 1
                            move 3 from 1 to 3
                            move 2 from 2 to 1
                            move 1 from 1 to 2
                        """)

    data = data.split("\n")
    initialState = data[:data.index("")]
    moves = data[data.index("")+1:]

    puzzle1(initialState, moves)


if __name__ == "__main__":
    main()
