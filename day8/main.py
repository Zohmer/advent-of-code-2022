from inspect import cleandoc


def puzzle1(inputList: list):
    trees =  seperateTrees(inputList)
    visable = 0


def puzzle2(inputList: list):
    pass


def seperateTrees(inputList: list) -> list:
    trees = []
    for row in inputList:
        treeRow = [int(tree) for tree in row]
        trees.append(treeRow)
    return trees


def isTreeVisable(trees: list, treeRow, treeColumn):
    pass


def main():
    TEST = True

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                            30373
                            25512
                            65332
                            33549
                            35390
                        """)

    data = data.split("\n")

    print(puzzle1(data))


if __name__ == "__main__":
    main()
