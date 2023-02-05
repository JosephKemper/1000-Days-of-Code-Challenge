import random

class Coin:
    def __init__(self):
        self.flip()
        self.heads_up = False

    def flip(self):
        self.heads_up = bool(random.randrange(2))
        return self.heads_up

    def display(self):
        if (self.heads_up):
            return "HEADS"
        else:
            return "TAILS"
