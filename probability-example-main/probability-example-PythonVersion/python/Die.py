import random

class Die:
    def __init__(self, num = 6):
        self.number_of_sides = num
        self.side_up = self.roll()

    def roll(self):
        self.side_up = random.randrange(self.number_of_sides) + 1
        return self.side_up

    def display(self):
        return f"{self.side_up}"

    def get_sides(self):
        return self.number_of_sides

    def set_sides(self, num):
        self.number_of_sides = num
        self.roll()
