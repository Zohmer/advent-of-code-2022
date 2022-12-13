from inspect import cleandoc


def puzzle1(inputList: list):
    trees = seperateTrees(inputList)
    visable = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if isTreeVisable(trees, i, j):
                visable += 1
    return visable


def puzzle2(inputList: list):
    trees = seperateTrees(inputList)
    scores = []
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            score = calcScenicScore(trees, i, j)
            print(f"Row: {i} Col: {j} Score: {score}")
            scores.append(score)

    return max(scores)


def seperateTrees(inputList: list) -> list:
    trees = []
    for row in inputList:
        treeRow = [int(tree) for tree in row]
        trees.append(treeRow)
    return trees


def isTreeVisable(trees: list, treeRow, treeColumn):
    if treeColumn >= len(trees[treeRow]) - 1:
        return True
    if treeColumn <= 0:
        return True
    if treeRow >= len(trees) - 1:
        return True
    if treeRow <= 0:
        return True

    height = trees[treeRow][treeColumn]
    for i in range(treeColumn+1, len(trees[treeRow])):
        if trees[treeRow][i] >= height:
            break
        elif i >= (len(trees[treeRow]) - 1):
            return True
    for i in range(treeColumn-1, -1, -1):
        if trees[treeRow][i] >= height:
            break
        elif i <= 0:
            return True
    for i in range(treeRow+1, len(trees)):
        if trees[i][treeColumn] >= height:
            break
        elif i >= (len(trees) - 1):
            return True
    for i in range(treeRow-1, -1, -1):
        if trees[i][treeColumn] >= height:
            break
        elif i <= 0:
            return True

    return False


def calcScenicScore(trees: list, treeRow, treeColumn):
    if treeColumn >= len(trees[treeRow]) - 1:
        return 0
    if treeColumn <= 0:
        return 0
    if treeRow >= len(trees) - 1:
        return 0
    if treeRow <= 0:
        return 0

    score = []

    height = trees[treeRow][treeColumn]
    counter = 1
    for i in range(treeColumn+1, len(trees[treeRow])):
        if trees[treeRow][i] >= height:
            score.append(counter)
            break
        elif i >= (len(trees[treeRow]) - 1):
            score.append(counter)
        counter += 1
    counter = 1
    for i in range(treeColumn-1, -1, -1):
        if trees[treeRow][i] >= height:
            score.append(counter)
            break
        elif i <= 0:
            score.append(counter)
        counter += 1
    counter = 1
    for i in range(treeRow+1, len(trees)):
        if trees[i][treeColumn] >= height:
            score.append(counter)
            break
        elif i >= (len(trees) - 1):
            score.append(counter)
        counter += 1
    counter = 1
    for i in range(treeRow-1, -1, -1):
        if trees[i][treeColumn] >= height:
            score.append(counter)
            break
        elif i <= 0:
            score.append(counter)
        counter += 1

    res = 1
    for e in score:
        if not e == 0:
            res *= e
    return res


def main():
    TEST = False

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
    print(puzzle2(data))


if __name__ == "__main__":
    main()
