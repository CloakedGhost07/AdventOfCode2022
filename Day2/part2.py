import re
from pprint import pprint

move_codes = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

wins = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}

score_codes = {"Rock": 1, "Paper": 2, "Scissors": 3, "WIN": 6, "LOSE": 0, "DRAW": 3}


class RPS:
    def __init__(self, moves: str):
        self.score = 0
        self.opp_move = move_codes.get(re.search(r"^(A|B|C)", moves).group(0))
        self.outcome = move_codes.get(re.search(r"(X|Y|Z)$", moves).group(0))

    def play(self):
        self.my_move = RPS.get_move_on_outcome(self.opp_move, self.outcome)
        return score_codes.get(self.my_move) + score_codes.get(self.outcome)

    def __repr__(self):
        return f"{self.opp_move=} {self.my_move=}"

    @staticmethod
    def get_move_on_outcome(opponent: str, outcome: str):
        if outcome == "DRAW":
            return opponent
        if outcome == "WIN":
            return wins.get(opponent)
        if outcome == "LOSE":
            for key, val in wins.items():
                if opponent == val:
                    return key

    @staticmethod
    def win_draw_lose(opponent: str, player: str):
        if opponent == player:
            return "DRAW"
        elif (
            (opponent == "Rock" and player == "Paper")
            or (opponent == "Scissors" and player == "Rock")
            or (opponent == "Paper" and player == "Scissors")
        ):
            return "WIN"
        elif (
            (player == "Rock" and opponent == "Paper")
            or (player == "Scissors" and opponent == "Rock")
            or (player == "Paper" and opponent == "Scissors")
        ):
            return "LOSE"


if __name__ == "__main__":
    score = 0
    with open("data") as f:
        for line in f.readlines():
            game = RPS(line)
            score += game.play()
    print(score)
