from inspect import cleandoc


def puzzle1(inputStr: str):
    calsPerElf = []
    i = 0
    totCals = 0
    while i < len(inputStr):
        totCals += int(inputStr[i])
        i += 1
        if i >= len(inputStr):
            calsPerElf.append(totCals)
            break
        if inputStr[i] == '':
            calsPerElf.append(totCals)
            totCals = 0
            i += 1

    biggestSum = 0
    for e in calsPerElf:
        if e > biggestSum:
            biggestSum = e

    return biggestSum


def puzzle2(inputStr: str):
    calsPerElf = []
    i = 0
    totCals = 0
    while i < len(inputStr):
        totCals += int(inputStr[i])
        i += 1
        if i >= len(inputStr):
            calsPerElf.append(totCals)
            break
        if inputStr[i] == '':
            calsPerElf.append(totCals)
            totCals = 0
            i += 1
    threeBiggestSums = [0, 0, 0]
    for e in calsPerElf:
        if e > threeBiggestSums[0]:
            threeBiggestSums[0] = e
    for e in calsPerElf:
        if e > threeBiggestSums[1] and e not in threeBiggestSums:
            threeBiggestSums[1] = e
    for e in calsPerElf:
        if e > threeBiggestSums[2] and e not in threeBiggestSums:
            threeBiggestSums[2] = e
    return sum(threeBiggestSums)


def main():
    TEST = False

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                            1000
                            2000
                            3000

                            4000

                            5000
                            6000

                            7000
                            8000
                            9000

                            10000
                        """)

    data = data.split("\n")

    print(puzzle1(data))
    print(puzzle2(data))


if __name__ == "__main__":
    main()
