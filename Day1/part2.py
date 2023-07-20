import re


class Elves:
    elves_num = 0

    def __init__(self):
        self.calories = 0
        Elves.elves_num += 1

    def add_calories(self, calories: int):
        if not isinstance(calories, int):
            calories = int(calories)
        self.calories += calories

    def get_calories(self):
        return self.calories

    def __lt__(self, other):
        return self.calories < other.calories

    def __gt__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return self.calories == other.calories

    def __repr__(self):
        return f"{self.calories=}"


if __name__ == "__main__":
    data = []
    elves = []
    with open("data") as f:
        currentElf = Elves()
        for line in f.readlines():
            if re.search(r"[\d]+", line):
                num = re.search(r"[\d]+", line).group(0)
                currentElf.add_calories(num)
            else:
                elves.append(currentElf)
                currentElf = Elves()
    elves.sort(reverse=True)
    print(elves[0])
    top3 = sum(elf.get_calories() for elf in elves[:3])
    print(top3)
