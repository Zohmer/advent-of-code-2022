from inspect import cleandoc


def puzzle1(inputList: list):
    fileSum = 0
    for cmd in inputList:
        try:
            fileSize = int(cmd.split(" ")[0])
            if fileSize <= 100000:
                fileSum += fileSize
        except ValueError:
            pass
    return fileSum


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
                            $ cd /
                            $ ls
                            dir a
                            14848514 b.txt
                            8504156 c.dat
                            dir d
                            $ cd a
                            $ ls
                            dir e
                            29116 f
                            2557 g
                            62596 h.lst
                            $ cd e
                            $ ls
                            584 i
                            $ cd ..
                            $ cd ..
                            $ cd d
                            $ ls
                            4060174 j
                            8033020 d.log
                            5626152 d.ext
                            7214296 k
                        """)

    data = data.split("\n")

    print(puzzle1(data))


if __name__ == "__main__":
    main()
