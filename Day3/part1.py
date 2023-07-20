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
        if item.isupper():
            return ord(item) - 64 + 26
        else:
            return ord(item) - 96

    def play(self):
        return Rucksack.get_item_val(self.get_common_item())


if __name__ == "__main__":
    score = 0
    with open("data") as f:
        for line in f.readlines():
            rucksack = Rucksack(line)
            # print(rucksack.get_common_item())
            # print(rucksack.play())
            score += rucksack.play()

    print(score)
