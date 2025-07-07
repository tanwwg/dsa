class GameEntry:
    def __init__(self, name, score):
        self.score = score
        self.name = name

    def __repr__(self):
        return f"{self.name} {self.score}"


class ScoreBoard:
    def __init__(self, n):
        self.n = n
        self.board = []

    def add(self, entry):
        self.board = sorted(self.board + [entry], key = lambda e: e.score, reverse=True)[0:self.n]

    def __repr__(self):
        return str(self.board)

s = ScoreBoard(3)
s.add(GameEntry("A", 1))
s.add(GameEntry("B", 10))
s.add(GameEntry("C", 100))
s.add(GameEntry("D", 1000))

print(s)

