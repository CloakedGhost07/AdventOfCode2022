import re
from pprint import pprint


class Rucksack:
    def __init__(self, contents: str):
        middleIndex = int(len(contents) / 2)
        self.left = set([s for s in contents.strip()[:middleIndex]])
        self.right = set([s for s in contents.strip()[middleIndex:]])

    def get_common_item(self):
        print(self.left.intersection(self.right))
        return self.left.intersection(self.right).pop()

    @staticmethod
    def get_item_val(item: str):
        # print(item)
        if item.isupper():
            return ord(item) - 64 + 26
        elif item.islower():
            return ord(item) - 96
        return 0

    def play(self):
        return Rucksack.get_item_val(self.get_common_item())


class Group:
    def __init__(self, rucksacks):
        self.sets = []
        for rucksack in rucksacks:
            self.sets.append(set(rucksack.strip()))

    def get_common_item(self):
        commons = set()
        return self.sets[0].intersection(self.sets[1]).intersection(self.sets[2]).pop()

    def play(self):
        return Rucksack.get_item_val(self.get_common_item())


if __name__ == "__main__":
    score = 0
    with open("data") as f:
        lines = f.readlines()
        for x in range(3, len(lines) + 1, 3):
            group = Group(lines[x - 3 : x])
            score += group.play()

    print(score)
