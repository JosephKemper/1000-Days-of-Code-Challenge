using System;

public class Deck{

    public static readonly string []SUIT_ARRAY = {"Spade","Heart","Club","Diamond"};
    public static readonly string []VALUE_ARRAY = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
    private static Random rnd = new Random();

    private List<Card> _deck=new List<Card>();
    private List<Card> _discard=new List<Card>();

    public Deck(){
        foreach (var s in SUIT_ARRAY){
            foreach (var v in VALUE_ARRAY){
                _deck.Add(new Card(s,v));
            }
        }
        ShuffleAll();
    }

    //Implents the Fisher Yates algorithm
    //Shuffles back in the discard pile
    public void ShuffleAll(){
        if(_discard.Count > 0){
            foreach(Card t in _discard){
                _deck.Add(t);
            }
            _discard.Clear();
        }
        for (int i = _deck.Count-1; i > 0; i--){
            int randomIndex = rnd.Next(0, i + 1);
        
            var temp = _deck[i];
            _deck[i] = _deck[randomIndex];
            _deck[randomIndex] = temp;
        }
    }

    //Implements Fisher Yates
    //Shuffles only the current stack, not the discard
    public void ShuffleCurrent(){
        for (int i = _deck.Count-1; i > 0; i--){
            int randomIndex = rnd.Next(0, i + 1);
        
            var temp = _deck[i];
            _deck[i] = _deck[randomIndex];
            _deck[randomIndex] = temp;
        }
    }


    //returns the first card in the deck, removes it and puts it in _discard
    public Card DrawAndDiscard(){
        Card temp = _deck[0];
        _deck.RemoveAt(0);
        _discard.Add(temp);
        return temp;
    }

    //returns the first card in the deck and reshuffles
    public Card DrawAndReplace(){
        Card temp = _deck[0];
        ShuffleAll();
        return temp;
    }

    public int Count(){
        return _deck.Count;
    }

    //Compares two cards
    //TODO Deal with suits.
    public static Comparator Compare (Card x, Card y){
        Comparator temp;
        int xIndex = Array.IndexOf(VALUE_ARRAY, x.GetValue()); 
        int yIndex = Array.IndexOf(VALUE_ARRAY, y.GetValue()); 
        if( xIndex < yIndex){
            temp= Comparator.Less;
        }
        else if( xIndex > yIndex){
            temp= Comparator.Greater;
        }
        else{
            temp =  Comparator.Equal;
        }
        return temp;
    }
}