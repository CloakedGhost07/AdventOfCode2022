import re
from pprint import pprint
import json
import numpy as np


class Ropes:
    def __init__(self, data):
        arraySize = 1000
        self.arraySize = arraySize
        self.movements = data
        self.map = np.array(
            [[False for _ in range(arraySize)] for _ in range(arraySize)]
        )
        self.head = {"x": int(arraySize / 2), "y": int(arraySize / 2)}
        self.tail = {"x": int(arraySize / 2), "y": int(arraySize / 2)}
        # self.head = {"x": 0, "y": 0}
        # self.tail = {"x": 0, "y": 0}

    def do_moves(self):
        for movement in self.movements:
            direction = re.search(r"(U|D|L|R)", movement).group(0)
            count = int(re.search(r"[\d]+$", movement).group(0))
            self.move(direction, count)
        print(self.getTouchCount())

    def move(self, direction: str, count: int):
        # print(f"moving {direction=} {count=}")
        # pprint(self.head)
        # pprint(self.tail)
        # self.draw()
        if count > 0:
            if direction == "U":
                self.head["y"] += 1
            if direction == "D":
                self.head["y"] += -1
            if direction == "L":
                self.head["x"] += -1
            if direction == "R":
                self.head["x"] += 1
            self.update_tail()
            self.map[self.tail["y"]][self.tail["x"]] = True
            self.move(direction, count - 1)
        else:
            return

    def update_tail(self):
        if (
            abs(self.head["x"] - self.tail["x"]) >= 2
            or abs(self.head["y"] - self.tail["y"]) >= 2
        ):
            if self.head["x"] == self.tail["x"]:
                self.tail_vertical(up=self.tail["y"] < self.head["y"])
            elif self.head["y"] == self.tail["y"]:
                self.tail_horizontal(right=self.tail["x"] < self.head["x"])
            else:
                self.tail_vertical(up=self.tail["y"] < self.head["y"])
                self.tail_horizontal(right=self.tail["x"] < self.head["x"])

    def tail_vertical(self, up=True):
        if up:
            self.tail["y"] += 1
        else:
            self.tail["y"] += -1

    def tail_horizontal(self, right=True):
        if right:
            self.tail["x"] += 1
        else:
            self.tail["x"] += -1

    def getTouchCount(self):
        return len(self.map[self.map == True])

    def draw(self):
        board = ""
        vertDraw = list(range(self.arraySize))
        vertDraw.reverse()
        for y in range(self.arraySize):
            line = ""
            for x in range(self.arraySize):
                if self.head["x"] == x and self.head["y"] == y:
                    line += "H"
                elif self.tail["x"] == x and self.tail["y"] == y:
                    line += "T"
                else:
                    line += "."
            board = line + "\n" + board
        print(board)


if __name__ == "__main__":
    with open("data") as f:
        data = f.readlines()
    ropes = Ropes(data)
    ropes.do_moves()
