from inspect import cleandoc


def puzzle1(initState: list, moves: list):
    crates = parseInitState(initState)
    moves = parseMoves(moves)

    for move in moves:
        for crate in range(move[0]):
            mCrate = crates[move[1]-1].pop()
            crates[move[2]-1].append(mCrate)

    topCrates = ""
    for stack in crates:
        topCrates += stack[-1]

    return topCrates


def puzzle2(initState: list, moves: list):
    crates = parseInitState(initState)
    moves = parseMoves(moves)

    for move in moves:
        mCrates = crates[move[1]-1][-(move[0]):]
        mCrates.reverse()
        for crate in range(move[0]):
            crates[move[1]-1].pop()
            crates[move[2]-1].append(mCrates.pop())

    topCrates = ""
    for stack in crates:
        topCrates += stack[-1]

    return topCrates


def parseInitState(initState: list):
    for e in initState:
        if e[0] == '1' or e[1] == '1':
            pos = e.split("  ")
            crateIndex = initState.index(e) - 1
            crates = [[] for item in pos]
            break

    while crateIndex >= 0:
        pos = 0
        for i in range(1, len(initState[crateIndex]), 4):
            if initState[crateIndex][i] != ' ':
                crates[pos].append(initState[crateIndex][i])
            pos += 1
        crateIndex -= 1

    return crates


def parseMoves(moves: list):
    parsedMoves = []
    for move in moves:
        splitted = move.split()
        parsedMoves.append([])
        for i in range(1, len(splitted), 2):
            parsedMoves[-1].append(int(splitted[i]))

    return parsedMoves


def main():
    TEST = False

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

    print(puzzle1(initialState, moves))
    print(puzzle2(initialState, moves))


if __name__ == "__main__":
    main()
