from inspect import cleandoc


def puzzle1(inputStr: str):
    pass


def puzzle2(inputStr: str):
    pass


def main():
    TEST = True

    if not TEST:
        inputFile = open("./input.txt", "r")
        data = inputFile.read()
        inputFile.close()
    else:
        data = cleandoc("""
                            test data goes here
                        """)

    data = data.split("\n")


if __name__ == "__main__":
    main()
