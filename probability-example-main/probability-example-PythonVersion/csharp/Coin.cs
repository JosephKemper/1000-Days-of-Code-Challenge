/*This is the template for a Coin object. It is resposible to knowing if heads is showing,
flipping the coin and displaying the value.*/

using System;

public class Coin{

    private bool _headsUp;  //whether heads is showing, or tails
    private static Random rnd = new Random(); //static because each coin does not need it's own
    
    public Coin(){
        this.Flip();
    }

    //returns and stores
    //new random head or tail
    public bool Flip(){
        _headsUp = (rnd.Next(0,2)>0); //converts the int to a bool    
        return _headsUp;
    } 

    //returns HEADS or TAILS
    public string Display(){
        if (_headsUp){
            return "HEADS";
        }
        else
            return "TAILS";
    }
}