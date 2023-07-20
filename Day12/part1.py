import re
from pprint import pprint
import numpy as np


class Hill:
    map: np.array
    location: tuple
    moves: int = 0
    height = "a"

    def __init__(self, data):
        map = []
        for row in data:
            map.append(list(row.strip()))
        self.map = np.array(map)
        print(self.map)
        self.location = np.where(self.map == "S")
        self.map[self.location[0], self.location[1]] = "a"
        print(self.map[self.location[0], self.location[1]])

    def find_moves(self):
        print(self.up())
        print(self.down())
        print(self.left())
        print(self.right())
        pass

    def up(self):
        return (
            ord(str(self.map[int(self.location[0]) - 1, int(self.location[1])][0]))
            <= (ord(str(self.map[self.location[0], self.location[1]][0]))) + 1
        )

    def down(self):
        return (
            ord(str(self.map[self.location[0] + 1, self.location[1]][0]))
            <= ord(str(self.map[self.location[0], self.location[1]][0])) + 1
        )

    def left(self):
        return (
            ord(str(self.map[self.location[0], self.location[1] - 1][0]))
            <= ord(str(self.map[self.location[0], self.location[1]][0])) + 1
        )

    def right(self):
        return (
            ord(str(self.map[self.location[0], self.location[1] + 1][0]))
            <= ord(str(self.map[self.location[0], self.location[1]][0])) + 1
        )


if __name__ == "__main__":
    score = 0
    with open("data") as f:
        lines = f.readlines()
    hill = Hill(lines)
    hill.find_moves()
