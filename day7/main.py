from inspect import cleandoc


def puzzle1(inputList: list):
    fs = [{"name": "/",
           "subDirs": [],
           "files": [],
           "parent": -1,
           "type": "dir"}, ]
    path = []
    i = 0
    while i < len(inputList):
        cmd = inputList[i].split(" ")
        if cmd[1] == "cd":
            path = handleCD(path, cmd[2])
            print(path)
        elif cmd[1] == "ls":
            stdout, i = getStdout(inputList, i)
            fs = handleLS(fs, path, stdout)
            print(fs)
            continue
        i += 1

    return fs


def puzzle2(inputList: list):
    pass


def getStdout(inputList: list, index: int):
    stdout = []
    for i in range(index+1, len(inputList), 1):
        if inputList[i].split(' ')[0] == "$":
            newIndex = i
            break
        stdout.append(inputList[i])

    return (stdout, newIndex)


def handleCD(path: list, dir: str) -> list:
    if dir == "/":
        return ['/']
    elif dir == "..":
        path.pop()
        return path
    elif dir == ".":
        return path
    else:
        path.append(dir)
        return path


def handleLS(fs: list, path: list, stdout: list) -> list:
    newFS = fs
    for item in stdout:
        info, name = item.split(" ")
        if info == "dir":
            path.append(name)
            newFS = addDir(newFS, path)
        else:
            newFS = addFile(newFS, path, name, info)
        print(newFS)

    return newFS


def addDir(fs: list, path: list) -> list:
    parentID = getItemID(fs, path[-2])
    dir = {"name": path[-1],
           "subDirs": [],
           "files": [],
           "parent": parentID,
           "type": "dir"}
    newFS = fs
    newFS[parentID]["subDirs"].append(len(newFS))
    return newFS.append(dir)


def addFile(fs: list, path: list, name: str, fileSize: int) -> list:
    parentID = getItemID(fs, path[-1])
    file = {"name": name,
            "size": fileSize,
            "parent": parentID,
            "type": "file"}
    newFS = fs
    newFS[parentID]["files"].append(len(newFS))
    return newFS.append(file)


def getItemID(fs: list, name: str,
              itemType: str = "dir", parentID: int = None) -> int:
    for i in range(len(fs)):
        if (
            fs[i]["name"] == name
            and fs[i]["type"] == itemType
            and (fs[i]["parent"] == parentID or parentID is None)
        ):
            return i
    raise NameError


def getItemFromPath(fs: list, path: str, itemType: str) -> dict:
    parentID = getItemID(fs, path[-2])
    return getItemID(fs, path[-1], itemType, parentID)


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
