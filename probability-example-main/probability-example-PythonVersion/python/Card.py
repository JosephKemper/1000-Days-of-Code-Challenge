
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def display(self, padding=" "):
        return f"{self.suit}{padding}{self.value}"

    def display_reverse(self, padding=" "):
        return f"{self.value}{padding}{self.suit}"

