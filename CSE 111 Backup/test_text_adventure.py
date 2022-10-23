from text_adventure import personalized_dialog, cabin_scene
import pytest


def test_personalized_dialog():
    """
    Test that the personalized_dialog function correctly returns 
    the proper dialog items
    Parameters: none
    Return: nothing
    """
    key_list = (
        "he_she", 
        "him_her",
        "his_her",
        "boy_girl",
        "brother_sister",
        "son_daughter",
        "male_female",
        "men_women",
        "man_woman",
        "love_interest",
        "opposite_male_female",
        "opposite_men_women",
        "opposite_he_she",
        "opposite_his_her",
        "opposite_him_her",
        "enemy_leader")

    male_value_list = (
        "he",
        "him",
        "his",
        "boy",
        "brother",
        "son",
        "male",
        "men",
        "man",
        "girl",
        "female",
        "women",
        "she",
        "her",
        "her",
        "Lady")

    female_value_list = (
        "she",
        "her",
        "her",
        "girl",
        "sister",
        "daughter",
        "female",
        "women",
        "woman",
        "guy",
        "male",
        "men",
        "male",
        "he",
        "his",
        "him",
        "Lord")

    char_gender = "Male"
    for key in key_list:
        assert personalized_dialog(char_gender, key) in male_value_list
    
    char_gender = "Female"
    for key in key_list:
        assert personalized_dialog(char_gender, key) in female_value_list

# TODO: #79 BUG test_cabin_scene Failing
def test_cabin_scene ():
    prior_death = False
    discovered_powers = False
    char_gender = "Male"
    char_name = "John"
    male_cabin_scene = cabin_scene(char_name, char_gender, prior_death,discovered_powers) 
    # Returns (story_text, player_choices, next_scenes)
    cabin_scene_display_text = male_cabin_scene [0]
    
    male_display_text = """"Today is going to be great!" You think to yourself.
I got the day off.
My friends and I have an amazing weekend planned.
I might even see that really cute girl again.
Who knows! Maybe I'll even ask her on a date.
Nothing could possibly ruin this day!
In the middle of your preparations to get ready for your weekend,
you hear an unfamiliar voice shouting just outside your house.
"John should be inside, get him now.
The High Lady wants him alive and in one piece."
As you look out the window, you see a dozen strangely dressed
men carrying large swords angrily moving towards your home.
You're at your dad's old cabin, miles out of town.
Even if they went 80, it would take the police an hour to get out here,
and you're not sure if you can get cell signal anyway.
"Police can't help me." You think to yourself. "I need to think of other options."
I could try to HIDE and hope they don't find me,
or I could try to ESCAPE out the window and make a break for it.
The forest is not far, I could run out there forever."""
    assert cabin_scene_display_text == male_display_text


    char_gender = "Female"
    char_name = "Jane"
    female_cabin_scene = cabin_scene(char_name, char_gender, prior_death,discovered_powers) 
    # Returns (story_text, player_choices, next_scenes)
    cabin_scene_display_text = female_cabin_scene [0]
    female_display_text = """"Today is going to be great!" You think to yourself.
I got the day off.
My friends and I have an amazing weekend planned.
I might even see that really cute guy again.
Who knows! Maybe I'll even ask him on a date.
Nothing could possibly ruin this day!
In the middle of your preparations to get ready for your weekend,
you hear an unfamiliar voice shouting just outside your house.
"Jane should be inside, get her now.
The High Lord wants her alive and in one piece."
As you look out the window, you see a dozen strangely dressed
women carrying large swords angrily moving towards your home.
You're at your dad's old cabin, miles out of town.
Even if they went 80, it would take the police an hour to get out here,
and you're not sure if you can get cell signal anyway.
"Police can't help me." You think to yourself. "I need to think of other options."
I could try to HIDE and hope they don't find me,
or I could try to ESCAPE out the window and make a break for it.
The forest is not far, I could run out there forever."""
    assert cabin_scene_display_text == female_display_text
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
