import GameRunner
import sys
import fileinput

GAMES = ['Coin Flip', 'Dice Roll', 'Card Game']

def print_menu(score, points):
    print("You can play:")
    for i, game in enumerate(GAMES):
        if (score >= points[i]):
            print(f"{i+1}. {game} ({points[i]} points)")
    print("0. Quit while you are ahead!")
    print("Please enter the number for your choice: ")

def main():
    player_points = 10
    runner = GameRunner.GameRunner()

    print("Welcome to the Probability Game!")
    print("Please enter your name:")
    player_name = input()

    # Attempt to load the player score
    filename = "scores.txt"
    try:
        print("Trying to open the file")
        with open(filename) as fin:
            for line in fin:
                parts = line.split('||')
                if len(parts) >= 2 and parts[0] == player_name:
                    player_points = int(parts[1]) # This could throw an exception, but assume parse works
                    break;
    except:
        print("Failed to open file.  Making a new one.")
        f = open(filename, 'a')
        f.close();

    choice = -1;
    while (choice != 0 and player_points > 0 and player_points < 100):
        points = [runner.coin_points, runner.dice_points, runner.card_points]
        print(f'\nYou have {player_points} points.')
        print_menu(player_points, points)
        try:
            choice = int(input())
            if choice < 0 or choice > len(points) or player_points < points[choice-1]:
                raise ValueError
        except:
            print("Please enter a valid choice")
            choice = -1
            continue
        if choice == 0:
            print(f"You quit with {player_points} points.")
        elif choice == 1:
            print("\nCoin Game")
            player_points = runner.play_coin_game(player_points)
        elif choice == 2:
            print("\nDice Game")
            player_points = runner.play_dice_game(player_points)
        elif choice == 3:
            print("\nCard Game")
            player_points = runner.play_card_game(player_points)
    
    if player_points == 0:
        print("Oh no! You lost it all!  Better luck next time!")
    elif  player_points >= 100:
        print("Wow!  You broke the bank!  Congratulations!")


    # Ask if the player wants to save their score to the file
    print("Would you like to save your name and score?  Enter Y or N: ")
    choice = GameRunner.GameRunner.get_y_or_n()
    updated = False
    if (choice == 'Y'):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:
            for line in lines:
                parts = line.split('||')
                if len(parts) >= 2 and parts[0] == player_name:
                    f.write(f"{player_name}||{player_points}\n")
                    updated = True
                else:
                    f.write(line)
            if not updated:
                f.write(f"{player_name}||{player_points}\n")

if __name__ == "__main__":
    main()
