/*This is the template for a GameRunner object. It is responsible for running
all of the games.*/

public class GameRunner{

    private Coin _coin = new Coin();
    public int coinPoints = 1; //how many points the coin game is worth
    private Die _die = new Die();
    public int dicePoints = 2; //how many points the dice game is worth
    public Deck _deck = new Deck();
    public int cardPoints = 5;

    //Reads input line and verfies a Y or N
    //Returns Y or N    
    private string getYN(){
        string choice = Console.ReadLine().ToUpper();
        while (choice != "Y" && choice != "N"){
            Console.Write("Please enter Y or N: ");
            choice = Console.ReadLine().ToUpper();
        } 
        return choice;
    }
    //Reads input line and verfies a >, < or =
    //Returns the symbol   
    private string getCompare(){
        string choice = Console.ReadLine();
        while (choice != ">" && choice != "<" && choice != "="){
            Console.Write("Please enter >, < or =: ");
            choice = Console.ReadLine();
        } 
        return choice;
    }


    //Flips a coin. 
    //Player guess if next is same or different
    //Flips a coin.
    //Awards or sutracts points if player was correct or not.
    //Allows repeated playing, unles player does not have enough points.
    public int CoinGame(int points){
        string playAgain = "Y";
        while (playAgain != "N"){
            Console.WriteLine("\nFlipping coin!");
            bool firstFlip = _coin.Flip();
            Console.WriteLine(_coin.Display());
            Console.Write("Do you think the next coin flip will be the same? Y or N: ");
            string bet = getYN();
            Console.WriteLine("\nFlipping again!");
            bool secondFlip = _coin.Flip();
            Console.WriteLine(_coin.Display());
            if(bet == "Y"){
                if(firstFlip == secondFlip){
                    points += coinPoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= coinPoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            else{
                if(firstFlip != secondFlip){
                    points += coinPoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= coinPoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }

            if(points < coinPoints){
                playAgain = "N";
                Console.WriteLine("Sorry. You don't have enough points to keep playing.");
            }
            else{
                Console.Write("\nWould you like to play again? Y or N: ");
                playAgain = getYN();
            }
        }
        return points;
    }//end CoinGame

    //Roll die.
    //Allows user to guess if new roll higher or lower.
    //Roll die.
    //Awards or subtracts points if user is correct or not.
    //Allows for repetition if player ahs enough points.
    //TODO: variable points depending on probability of correct guess?
    public int DiceGame (int points){
        string playAgain = "Y";
        while (playAgain != "N"){
            Console.WriteLine("\nRolling die!");
            int firstRoll = _die.Roll();
            Console.WriteLine(_die.Display());
            Console.WriteLine("Do you think the next roll will be Higher(>), Lower(<) or the Same(=)?");
            Console.Write("Enter >, < or =? ");
            string bet = getCompare();
            Console.WriteLine("\nRolling again!");
            int secondRoll = _die.Roll();
            Console.WriteLine(_die.Display());
            //Check if the user won
            if(bet == ">"){
                if(secondRoll > firstRoll){
                    points += dicePoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= dicePoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            else if (bet == "<"){
                if(secondRoll < firstRoll){
                    points += dicePoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= dicePoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            else{
                if(secondRoll == firstRoll){
                    points += dicePoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= dicePoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            //Check if playing again
            if(points < dicePoints){
                playAgain = "N";
                Console.WriteLine("Sorry. You don't have enough points to keep playing.");
            }
            else{
                Console.Write("\nWould you like to play again? Y or N: ");
                playAgain = getYN();
            }
        }
        return points;
    }//end DiceGame
    
    public int CardGame (int points){
        string playAgain = "Y";
        _deck.ShuffleAll();
        while (playAgain != "N"){
            Console.WriteLine("\nDealing card");
            Card firstCard = _deck.DrawAndDiscard();
            Console.WriteLine(firstCard.DisplayReverse(" of "));
            Card secondCard = _deck.DrawAndDiscard();
            Console.WriteLine("Do you think the next card will be Higher(>), Lower(<) or the Same(=)?");
            Console.Write("Enter >, < or =? ");
            string bet = getCompare();
            Console.WriteLine("\nNext Card!");
            Console.WriteLine(secondCard.DisplayReverse(" of "));
            //Check if the user won
            if(bet == ">"){
                if(Deck.Compare(secondCard,firstCard) == Comparator.Greater){
                    points += cardPoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= cardPoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            else if (bet == "<"){
                if(Deck.Compare(secondCard,firstCard) == Comparator.Less){
                    points += cardPoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= cardPoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            else{
                if(Deck.Compare(secondCard,firstCard) == Comparator.Equal){
                    points += cardPoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= cardPoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            //Check if playing again
            if(points < cardPoints){
                playAgain = "N";
                Console.WriteLine("Sorry. You don't have enough points to keep playing.");
            }
            else{
                Console.Write("\nWould you like to play again? Y or N: ");
                playAgain = getYN();
            }
        }
        return points;
    }//end CardGame
}
