import Coin
import Die
import Deck

class GameRunner:
    def __init__(self):
        self.coin = Coin.Coin()
        self.die = Die.Die()
        self.deck = Deck.Deck()
        self.coin_points = 1;
        self.dice_points = 2;
        self.card_points = 5;

    def play_coin_game(self, points):
        play_again = 'Y'
        while play_again != 'N':
            first_flip = self.coin.flip()
            print("\nFlipping coin!\n"
                    f"{self.coin.display()}\n"
                    "Do you think the next flip will be the same? Y or N: ");
            choice = GameRunner.get_y_or_n()
            print("\nFlipping again!")
            second_flip = self.coin.flip()
            print(f"{self.coin.display()}")
            win = False
            if (choice == 'Y' and second_flip == first_flip):
                win = True
            elif (choice == 'N' and second_flip != first_flip):
                win = True
            
            if win:
                points += self.coin_points
                print(f"You win! You now have {points} points!")
            else:
                points -= self.coin_points
                print(f"You lose! You now have {points} points!")

            if points < self.coin_points:
                play_again = 'N'
                print("Sorry, you don't have enough points to keep playing.")
            else:
                print("\nWould you like to play again? Y or N: ")
                play_again = GameRunner.get_y_or_n()

        return points

    def play_dice_game(self, points):
        play_again = 'Y'
        while play_again != 'N':
            first_roll = self.die.roll()
            print(f"{self.die.display()}\n"
                   "Do you think the next roll will be Higher (>), Lower (<), or the same (=) ?\n"
                   "Enter >, <, or = ?")
            choice = GameRunner.get_compare()
            print("\nRolling again!")
            second_roll = self.die.roll()
            print(f"{self.die.display()}")
            win = False
            if (choice == '>' and second_roll > first_roll):
                win = True
            elif (choice == '=' and second_roll == first_roll):
                win = True
            elif (choice == '<' and second_roll < first_roll):
                win = True
            
            if win:
                points += self.dice_points
                print(f"You win! You now have {points} points!")
            else:
                points -= self.dice_points
                print(f"You lose! You now have {points} points!")

            if points < self.dice_points:
                play_again = 'N'
                print("Sorry, you don't have enough points to keep playing.")
            else:
                print("\nWould you like to play again? Y or N: ")
                play_again = GameRunner.get_y_or_n()

        return points

    def play_card_game(self, points):
        play_again = 'Y'
        self.deck.shuffle_all()
        while play_again != 'N':
            first_card = self.deck.draw_and_discard()
            second_card = self.deck.draw_and_discard()
            print("\nDealing card\n"
                    f"{first_card.display_reverse(' of ')}\n"
                    # f"{second_card.display_reverse(' of ')}\n" # Debugging
                    "Do you think the next card will be higher (>), lower (<), or the same (=) ?\n"
                    "Enter >, <, or = : ")
            choice = GameRunner.get_compare()
            print(f"Next Card!\n{second_card.display_reverse(' of ')}")
            win = False
            if (choice == '<' and Deck.Deck.compare(second_card, first_card) == Deck.Comparator.LESS):
                win = True
            elif (choice == '=' and Deck.Deck.compare(second_card, first_card) == Deck.Comparator.EQUAL):
                win = True
            elif (choice == '>' and Deck.Deck.compare(second_card, first_card) == Deck.Comparator.GREATER):
                win = True

            if win:
                points += self.card_points
                print(f"You win!  You now have {points} points!")
            else:
                points -= self.card_points
                print(f"You lose!  You now have {points} pionts!")

            if points < self.card_points:
                play_again = 'N'
                print("Sorry. You don't have enough points to keep playing.")
            else:
                print("Would you like to play again?  Y or N: ")
                play_again = GameRunner.get_y_or_n()

        return points

    def get_compare():
        choice = input()
        while choice not in ('>', '=', '<'):
            print("Please enter >, <, or =: ")
        return choice

    def get_y_or_n():
        choice = input().upper()
        while choice not in ('Y', 'N'):
            print("Please enter Y or N: ")
            choice = input().upper()
        return choice

