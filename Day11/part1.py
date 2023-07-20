import re
from pprint import pprint
import json
import numpy as np
import math
from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        val = func(*args, **kwargs)
        print(
            "{} : ".format(func.__name__)
            + str(round(float(time() - start), 4))
            + "  seconds"
        )
        return val

    return wrapper


class Monkey:
    def __init__(self, startingItems: list, operation, value, testval, test: dict):
        self.items = startingItems
        self.operation: function = operation
        self.value: int = value
        self.test: dict = test
        self.testval = testval
        self.inspection = 0

    # @timer
    def turn(self, monkeys: dict):
        while len(self.items) > 0:
            item = self.items.pop(0)  # remove item from inventory
            # val = int(math.floor(self.increaseWorry(item) / 3))
            val = self.increaseWorry(item)
            check = self.checkItem(val)
            if check:
                val = val / self.testval
            throwTo = self.test.get(str(check))
            monkeys[throwTo].items.append(val)
            self.inspection += 1

    def increaseWorry(self, item: int) -> int:
        if self.operation == math.pow:
            return item * item
        return self.operation([item, self.value])

    def checkItem(self, item):
        # print(
        #     f"{item=} % {self.testval=} = {item % self.testval} {item % self.testval== 0.0}"
        # )
        return item % self.testval == 0.0

    def __repr__(self):
        return f"{self.inspection}"


@timer
def run(monkeys):
    start = time()
    for x in range(1000):
        for key, monkey in monkeys.items():
            monkey.turn(monkeys)
        if x % 100 == 0:
            print(f"Round : {x} ")
            print(str(round(float(time() - start), 4)) + "  seconds\n")
    for key, monkey in monkeys.items():
        print(key, monkey)


if __name__ == "__main__":
    monkeys = {
        "0": Monkey(
            startingItems=[79, 98],
            operation=math.prod,
            value=19,
            testval=23,
            test={"True": "2", "False": "3"},
        ),
        "1": Monkey(
            startingItems=[54, 65, 75, 74],
            operation=sum,
            value=6,
            testval=19,
            test={"True": "2", "False": "0"},
        ),
        "2": Monkey(
            startingItems=[79, 60, 97],
            operation=math.pow,
            value=1,
            testval=13,
            test={"True": "1", "False": "3"},
        ),
        "3": Monkey(
            startingItems=[74],
            operation=sum,
            value=3,
            testval=17,
            test={"True": "0", "False": "1"},
        ),
    }
    # monkeys = {
    #     "0": Monkey(
    #         startingItems=[71, 56, 50, 73],
    #         operation=math.prod,
    #         value=11,
    #         testval=13.0,
    #         test={"True": "1", "False": "7"},
    #     ),
    #     "1": Monkey(
    #         startingItems=[70, 89, 82],
    #         operation=sum,
    #         value=1,
    #         testval=7,
    #         test={"True": "3", "False": "6"},
    #     ),
    #     "2": Monkey(
    #         startingItems=[52, 95],
    #         operation=math.pow,
    #         value=11,
    #         testval=3.0,
    #         test={"True": "5", "False": "4"},
    #     ),
    #     "3": Monkey(
    #         startingItems=[94, 64, 69, 87, 70],
    #         operation=sum,
    #         value=2,
    #         testval=19,
    #         test={"True": "2", "False": "6"},
    #     ),
    #     "4": Monkey(
    #         startingItems=[98, 72, 98, 53, 97, 51],
    #         operation=sum,
    #         value=6,
    #         testval=5,
    #         test={"True": "0", "False": "5"},
    #     ),
    #     "5": Monkey(
    #         startingItems=[79],
    #         operation=sum,
    #         value=7,
    #         testval=2,
    #         test={"True": "7", "False": "0"},
    #     ),
    #     "6": Monkey(
    #         startingItems=[77, 55, 63, 93, 66, 90, 88, 71],
    #         operation=math.prod,
    #         value=7,
    #         testval=11,
    #         test={"True": "2", "False": "4"},
    #     ),
    #     "7": Monkey(
    #         startingItems=[54, 97, 87, 70, 59, 82, 59],
    #         operation=sum,
    #         value=8,
    #         testval=17,
    #         test={"True": "1", "False": "3"},
    #     ),
    # }
    run(monkeys)
