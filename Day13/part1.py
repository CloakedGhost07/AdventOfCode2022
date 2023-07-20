import re
from pprint import pprint
import json


class Signal:
    pairs: list

    def __init__(self, data):
        self.pairs = []
        pair = []
        for row in data:
            row = row.strip()
            if len(row) == 0:
                self.pairs.append(pair)
                pair = []
            else:
                pair.append(row)

    def decode_pairs(self):
        for top, bottom in self.pairs:
            print(json.loads(top))

    def compare(left,right):
        


if __name__ == "__main__":
    with open("data") as f:
        lines = f.readlines()
    signal = Signal(lines)
    signal.decode_pairs()
