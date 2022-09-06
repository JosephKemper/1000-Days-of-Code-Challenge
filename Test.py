from sentences import get_verb
import random
import pytest





def test_past_tense():

    for _ in range(4):
        verb= get_verb(1, "past")
        # Past Tense verbs
        past_tense_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        assert verb in past_tense_verbs

def test_present_tense_singular ():
    for _ in range(4):
        verb= get_verb(1, "present")
        # Present Tense singular verbs
        singular_present_tense_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        assert verb in singular_present_tense_verbs

def test_present_tense_plural ():
    for _ in range(4):
        verb= get_verb(2, "present")
        # Present Tense plural verbs
        plural_present_tense_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        assert verb in plural_present_tense_verbs

def test_future_tense():
    for _ in range(4):
        verb= get_verb(1, "future")
        # Future Tense verbs
        future_tense_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        assert verb in future_tense_verbs



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])