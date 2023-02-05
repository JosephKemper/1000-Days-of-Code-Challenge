/*This is the template for a Die object. It is responsible for knowing the 
number of sides and which side is showing and rolling a new side. 

Sides are consecutive integers starting at 1. This could be expanded to a general
base class with specfic child IntegerDie.*/

using System;

public class Die{

    private int _numberOfSides;
    private int _sideUp; //stores the currectly showing side.
    private static Random rnd = new Random(); //static because each die does not need it's own

    //default constructor is 6
    public Die(){
        _numberOfSides = 6;
        _sideUp = Roll();
    }

    //allows for a different number of sides
    public Die (int num){
        _numberOfSides = num;
        _sideUp = Roll();
    }

    //Stores and returns new random side value
    public int Roll(){
        _sideUp = rnd.Next(1,_numberOfSides+1); //next is min inclusive, max exclusive
        return _sideUp;
    }

    //return the side value as a string
    public string Display (){
        return _sideUp.ToString();
    }

    //return the integer value of the side up
    public int GetValue(){
        return _sideUp;
    }

    //return the number of Sides
    public int GetSides(){
        return _numberOfSides;
    }

    //allow the number of sides to change as long as num > 1
    //reroll die so sideUp is within the new bounds
    //TODO would be better to throw exception if num <=1
    public void SetSides(int num){
        if (num >=1){
             _numberOfSides = num;
             Roll();
        }
    }

}