import re
from pprint import pprint
import json
import numpy as np


class Forrest:
    def __init__(self, data):
        self.forrest = []
        for row in data:
            this_row = []
            row = list(row)
            for tree in row:
                try:
                    tree = int(tree)
                    this_row.append(tree)
                except:
                    pass
            self.forrest.append(this_row)

    def __repr__(self):
        representation = ""
        for row in self.forrest:
            for tree in row:
                representation += f"[{tree}]"
            representation += "\n"
        return representation

    def findVisibles(self):
        forrest = np.array(self.forrest)
        visible = np.array([[False for _ in row] for row in self.forrest])
        for r, row in enumerate(forrest):
            for t, tree in enumerate(row):
                if (
                    r == 0
                    or t == 0
                    or r == len(self.forrest) - 1
                    or t == len(self.forrest[0]) - 1
                ):
                    visible[r][t] = True
                else:
                    if (forrest[r])[:t].max() < tree:
                        visible[r][t] = True
                    if (forrest[r])[t + 1 :].max() < tree:
                        visible[r][t] = True
                    topTrees = []
                    for top in forrest[:r]:
                        topTrees.append(top[t])
                    if max(topTrees) < tree:
                        visible[r][t] = True
                    bottomTrees = []
                    for bottom in forrest[r + 1 :]:
                        bottomTrees.append(bottom[t])
                    if max(bottomTrees) < tree:
                        visible[r][t] = True
        print(len(visible[visible == True]))

    @staticmethod
    def countVisibleTrees(height: int, trees: list):
        canSee = True
        score = 0
        while canSee:
            try:
                tree = trees.pop(0)
                if tree >= height:
                    score += 1
                    canSee = False
                    break
                else:
                    score += 1
            except:
                canSee = False
                break
        return score

    def findTheBestSpot(self):
        forrest = np.array(self.forrest)
        scenicScores = np.array([[0 for _ in row] for row in self.forrest])
        for r, row in enumerate(forrest):
            for t, tree in enumerate(row):
                leftTrees = list((forrest[r])[:t])
                leftTrees.reverse()
                leftScore = Forrest.countVisibleTrees(tree, leftTrees)
                rightTrees = list((forrest[r])[t + 1 :])
                rightScore = Forrest.countVisibleTrees(tree, rightTrees)
                upperTrees = []
                for top in forrest[:r]:
                    upperTrees.append(top[t])
                upperTrees.reverse()
                upperScore = Forrest.countVisibleTrees(tree, upperTrees)
                lowerTrees = []
                for top in forrest[r + 1 :]:
                    lowerTrees.append(top[t])
                lowerScore = Forrest.countVisibleTrees(tree, lowerTrees)
                scenicScores[r][t] = rightScore * leftScore * upperScore * lowerScore
        print(scenicScores.max())


if __name__ == "__main__":
    with open("data") as f:
        data = f.readlines()
    forrest = Forrest(data)
    with open("output.txt", "w") as f:
        f.write(str(forrest))
    forrest.findTheBestSpot()
