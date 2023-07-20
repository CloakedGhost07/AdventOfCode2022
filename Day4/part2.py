import re
from pprint import pprint


def parse_pairs(data: str):
    firstset = data.split(",")[0].strip().split("-")
    secondset = data.split(",")[1].replace(",", "").strip().split("-")
    a, b = firstset
    x, y = secondset
    a = int(a)
    b = int(b)
    x = int(x)
    y = int(y)
    for first in range(a, b + 1):
        if first in range(x, y + 1):
            return True
    return False


if __name__ == "__main__":
    score = 0
    with open("data") as f:
        for line in f.readlines():
            if parse_pairs(line):
                score += 1

    print(score)
