from inspect import cleandoc


def puzzle1(inputList: list):
    prioSum = 0
    for e in inputList:
        firstComp = e[:int(len(e)/2)]
        secondComp = e[int(len(e)/2):]

        for item in firstComp:
            if item in secondComp:
                prioSum += getItemPrio(item)
                break

    return prioSum


def puzzle2(inputList: list):
    prioSum = 0
    for i in range(0, len(inputList), 3):
        for e in inputList[i]:
            if e in inputList[i+1] and e in inputList[i+2]:
                prioSum += getItemPrio(e)
                break

    return prioSum


def getItemPrio(letter: str):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    convTable = {}

    for i in range(len(letters)):
        convTable[letters[i]] = i+1

    if letter.islower():
        return convTable[letter]
    else:
        return (convTable[letter.lower()] + 26)


def main():
    TEST = False

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                            vJrwpWtwJgWrhcsFMMfFFhFp
                            jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
                            PmmdzqPrVvPwwTWBwg
                            wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
                            ttgJtRGJQctTZtZT
                            CrZsJsPPZsGzwwsLwLmpwMDw
                        """)

    data = data.split("\n")

    print(puzzle1(data))
    print(puzzle2(data))


if __name__ == "__main__":
    main()
