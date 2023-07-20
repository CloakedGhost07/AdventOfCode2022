import re
from pprint import pprint
import json


class FileSystem:
    def __init__(self, terminalOutput: list):
        self.terminalOutput = terminalOutput
        self.fileSystem = {"/": {}}
        self.currentDir = ["/"]
        self.homeDir = "/"
        self.pointer = self.fileSystem["/"]
        self.buildDirs()

    def buildDirs(self):
        output = self.terminalOutput.pop(0)
        while output:
            try:
                self.runCommand(output)
                output = self.terminalOutput.pop(0)
            except:
                print(f"{output=}")
                return

    def runCommand(self, command):
        if "$" in command:
            if "cd" in command:
                if "/" in command:
                    self.currentDir = ["/"]
                    self.pointer = self.fileSystem["/"]
                elif ".." in command:
                    self.currentDir.pop()
                    self.pointer = self.fileSystem
                    for dir in self.currentDir:
                        if not self.pointer.get(dir):
                            self.pointer[dir] = {}
                        self.pointer = self.pointer.get(dir)
                else:
                    dir = re.search(r"[A-Za-z]+$", command).group(0)
                    self.currentDir += [dir]
                    self.pointer = self.fileSystem
                    for dir in self.currentDir:
                        self.pointer = self.pointer.get(dir)
            if "ls" in command:
                return
        else:
            self.addFiles(command)

    def addFiles(self, file):
        if re.match(r"^[\d]+ ([a-zA-Z]+.|)[A-Za-z]+$", file):
            fileName = re.search(r" ([a-zA-Z]+.|)[A-Za-z]+$", file).group(0).lstrip()
            fileSize = int(re.search(r"^[\d]+", file).group(0))
            self.pointer[fileName] = fileSize
        elif re.match(r"dir [a-zA-Z]+$", file):
            fileName = re.search(r"[A-Za-z]+$", file).group(0)
            pprint(self.fileSystem)
            self.pointer[fileName] = {}

    def getDirDict(self):
        return self.fileSystem


folderSizes = {}
fileSizes = {}


class Holder:
    lessthan100k = 0


def calculateSizeOfDir(files: dict, path="") -> int:
    size = 0
    for file, contents in files.items():
        this_path = path + f"[{file}]-"
        if isinstance(contents, dict):
            contentSize = calculateSizeOfDir(contents, this_path)
            if not folderSizes.get(this_path):
                folderSizes[this_path] = 0
            folderSizes[this_path] += contentSize
            size += contentSize
        if isinstance(contents, int):
            size += contents
    return size


if __name__ == "__main__":
    score = 0
    with open("data") as f:
        lines = f.readlines()
    fileSystem = FileSystem(lines)
    dirDict = fileSystem.getDirDict()
    with open("output.json", "w") as f:
        json.dump(dirDict, f, indent=2)
    rootSize = calculateSizeOfDir(dirDict)
    pprint(folderSizes)
    with open("output2.json", "w") as f:
        json.dump(folderSizes, f, indent=2)
    bigEnoughToDelete = []
    for file, size in folderSizes.items():
        if size <= 100000:
            Holder.lessthan100k += size
    print(f"{Holder.lessthan100k=}")
