# Week 06 Prove
from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun ():
    

    singular_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
       noun = get_noun(1)
       assert noun in singular_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):
       noun = get_noun(2)
       assert noun in plural_nouns

def test_get_verb():

    # Past Tense verbs
    past_tense_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb= get_verb(1, "past")

        assert verb in past_tense_verbs
    
    # Present Tense singular verbs
    singular_present_tense_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb= get_verb(1, "present")
        assert verb in singular_present_tense_verbs

    # Present Tense plural verbs
    plural_present_tense_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        verb= get_verb(2, "present")
        assert verb in plural_present_tense_verbs

    # Future Tense verbs
    future_tense_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        verb= get_verb(1, "future")
        assert verb in future_tense_verbs

def test_get_prepositions ():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        preposition= get_preposition()
        assert preposition in prepositions

# TODO: #10 write def test_get_prepositional_phrase matching requirements outlined in 06 Prove Assignment
def test_get_prepositional_phrases ():
    """
    Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    singular_determiner = ["a", "one", "the"]
    plural_determiner = ["some", "many", "the"]

    singular_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Test Singular Prepositional phrases
    # TODO: #15 First attempt at testing prepositional phrase split letters not words
    for _ in range(4):
        singular_phrase = get_prepositional_phrase(1)
        singular_list = singular_phrase.split()
        assert singular_list[0] in prepositions
        assert singular_list[1] in singular_determiner
        assert singular_list[2] in singular_nouns
        

    # Test Plural Prepositional phrases
    for _ in range(4):
        plural_phrase = get_prepositional_phrase(2)
        plural_list = plural_phrase.split()
        assert plural_list[0] in prepositions
        assert plural_list[1] in plural_determiner
        assert plural_list[2] in plural_nouns

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line","-rN", __file__])