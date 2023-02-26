using System;

class Menu
{
    public static string GetYN(){
        string choice = Console.ReadLine().ToUpper();
        while (choice != "Y" && choice != "N"){
            Console.Write("Please enter Y or N: ");
            choice = Console.ReadLine().ToUpper();
        } 
        return choice;
    }
    public static void PrintMenu(int max){
        Console.WriteLine("You can play: ");
        //only print the games the player has enough points to play
        if(max >= 1){
            Console.WriteLine("1. Coin Flip (1 point)");
        }
        if(max >= 2){
            Console.WriteLine("2. Dice Roll (2 points)");
        }
        if(max >= 3){
            Console.WriteLine("3. Card Game (5 points)");
        }
        Console.WriteLine("0. Quit while you are ahead!");
        Console.WriteLine("\nPlease enter the number for you choice: ");
    }
    static int ReadInt(int min, int max){
        string readValue;
        int readInt;
        
        readValue = Console.ReadLine();
        readInt = int.Parse(readValue);
        while(readInt < min || readInt > max){
            Console.Write($"Please enter an integer between {min} and {max}. ");
            readValue = Console.ReadLine();
            readInt = int.Parse(readValue);
        }
        return readInt;
    }
    public static void Main(string[] args)
    {
        int playerPoints = 10;
        GameRunner gr = new GameRunner();
        string filename = "scores.txt";
        string[] lines = System.IO.File.ReadAllLines(filename);
        string saveLoad;
        int index = -1;

        Console.WriteLine("Welcome to the Probability Game!");
        Console.WriteLine("Please enter your name: ");
        string playerName = Console.ReadLine();
        
        //if there are saved games, check to see if this person has one
        if (lines.Length > 0){
            index = Array.FindIndex(lines, element => element.Contains(playerName));
            if(index >= 0){
                Console.WriteLine($"Welcome back, {playerName}!");
                Console.WriteLine("Would you like to load a previously saved game? Enter Y or N");
                saveLoad = GetYN();
                if(saveLoad == "Y"){
                    string[] parts = lines[index].Split("||");
                    playerPoints= int.Parse(parts[1]);
                }
            }
        }

        //determine which game to play
        int choice = 1;
        int max;
        while(choice!=0 && playerPoints > 0 && playerPoints < 100){
            //find the highest scoring game that can be played with the points available.
            if(playerPoints >= gr.cardPoints){
                max = 3;    
            }
            else if(playerPoints >= gr.dicePoints){
                max = 2;
            }
            else{
                max = 1;
            }
            //Print the menu and get the choice
            Console.WriteLine();
            Console.WriteLine($"You have {playerPoints} points.");
            PrintMenu(max);
            choice = ReadInt(0,max);

            switch(choice){
                case 0:
                    Console.WriteLine($"You quit with {playerPoints} points.");
                    if(playerPoints > 10){
                        Console.WriteLine("Nice job!");
                    }
                    else{
                        Console.WriteLine("Better luck next time!");
                    }
                    break;
                case 1:
                    Console.WriteLine("\nCoin Game");
                    playerPoints = gr.CoinGame(playerPoints);
                    break;
                case 2:
                    Console.WriteLine("Dice Game");
                    playerPoints = gr.DiceGame(playerPoints);
                    break;
                case 3:
                    Console.WriteLine("Card Game");
                    playerPoints = gr.CardGame(playerPoints);
                    break;
            }
        }
        if(playerPoints == 0){
            Console.WriteLine("Oh no! You lost it all! Better luck next time!");
        }
        else if(playerPoints >= 100){
            Console.WriteLine("Wow! You broke the bank! Congratulations!");
        }

        //Ask if want to save.
        Console.Write("Would you like to save your name and score? Enter Y or N: ");
        saveLoad = GetYN();
        if(saveLoad == "Y"){
            //if this player has played before, rewrite their info.
            if(index >= 0){
                lines[index] = $"{playerName}||{playerPoints}";
            }
            using (StreamWriter outputFile = new StreamWriter(filename)){
                //rewrite all the old info
                foreach(string line in lines){
                    outputFile.WriteLine(line);
                }
                //If this is a new player, write the information at the end
                if(index<0){
                    outputFile.WriteLine($"{playerName}||{playerPoints}");
                }
            }   
        }

    }//end Main
}