import re
from pprint import pprint


class Containers:
    def __init__(self, lines):
        self.stacks = []
        for line in lines:
            stack = list(line.strip())
            stack.reverse()
            self.stacks.append(stack)

    def __repr__(self):
        string = ""
        for stack in self.stacks:
            string += str(stack[-1])
        return string

    def remove_crate(self, stack: int):
        try:
            return self.stacks[stack - 1].pop()
        except:
            return None

    def add_crate(self, stack: int, crates: str):
        self.stacks[stack - 1].extend(crates)


def do_move(move: str, container: Containers):
    moves = re.findall(r"[\d]+", move)
    # print(moves)
    how_many = int(moves[0])
    from_stack = int(moves[1])
    to_stack = int(moves[2])
    crates = []
    for _ in range(how_many):
        crates.append(container.remove_crate(from_stack))
    crates.reverse()
    container.add_crate(to_stack, crates)


if __name__ == "__main__":
    score = 0
    with open("data2") as f:
        lines = f.readlines()
        containers = Containers(lines[10:])
    # print(containers)
    with open("data") as f:
        for line in f.readlines():
            do_move(line, containers)
            # break
    print(containers)
