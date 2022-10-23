# The Ultimate Choose Your Own Adventure Game
import PySimpleGUI as sg


# Setting up variables as lists to allow for dynamic scene mapping
current_options = []
current_scene = []
next_scenes = []

def main ():
    sg.theme("default1")
    # All the stuff inside your window.
    char_info = character_creation()
    prior_death = False
    discovered_powers = False
    char_name = char_info[0]
    char_gender = char_info[1]

    # Maps the player choices to the variable current_scene
    current_scene = cabin_scene(char_name, char_gender, prior_death, discovered_powers)
    # Returns (story_text, player_choices, next_scenes)

    # Pulls display text from current scene to display to user
    display_text = current_scene [0]
	@@ -45,9 +44,9 @@ def main ():
        if event == sg.WIN_CLOSED or event == "Cancel": # if user closes window or clicks cancel
            break
        elif event == option_1:
            current_scene = next_scenes [0]
        elif event == option_2:
            current_scene = next_scenes [1]
    window.close()

def personalized_dialog (gender, key):
	@@ -58,7 +57,7 @@ def personalized_dialog (gender, key):
    is to allow those references to be dynamic to the character
    which the player created.
    """
    if gender == "Male":
        male = {
        "he_she" :"he", 
        "him_her" : "him",
	@@ -78,7 +77,7 @@ def personalized_dialog (gender, key):
        "enemy_leader" : "Lady"
        }
        return male.get(key)
    elif gender == "Female":
        female = {
        "he_she" : "she",
        "him_her" : "her",
	@@ -139,9 +138,9 @@ def cabin_scene(char_name, gender, prior_death,discovered_powers):
    This function is used to stage user interaction 
    for activities that happen in the cabin scene of the story.
    """

    if prior_death == False:
        story_text = f""""Today is going to be great!" You think to yourself.
I got the day off.
My friends and I have an amazing weekend planned.
I might even see that really cute {personalized_dialog(gender,"love_interest")} again.
	@@ -154,27 +153,49 @@ def cabin_scene(char_name, gender, prior_death,discovered_powers):
As you look out the window, you see a dozen strangely dressed 
{personalized_dialog(gender,"men_women")} carrying large swords angrily moving towards your home.
You're at your dad's old cabin, miles out of town. 
Even if they went 80, it would take the police an hour to get out here, 
and you're not sure if you can get cell signal anyway.
"Police can't help me." You think to yourself. "I need to think of other options."
I could try to HIDE and hope they don't find me, 
or I could try to ESCAPE out the window and make a break for it. 
The forest is not far, I could run out there forever."""
        player_choices = {
            "option_1":"HIDE",
            "option_2":"ESCAPE"}

        next_scenes = {
            "option_1":closet_scene,
            "option_2":forest_scene}

        return story_text, player_choices, next_scenes

# TODO: #75 BUG Tried to create filler scenes but it crashed when testing. 
def closet_scene(char_name, gender, prior_death,discovered_powers):
    story_text = "To Be Continued"

    player_choices = {
            "option_1":"not enabled",
            "option_2":"not enabled"}

    next_scenes = {
        "option_1":"filler_0",
        "option_2":"filler_1"}

    return story_text, player_choices, next_scenes


def forest_scene(char_name, gender, prior_death,discovered_powers):
    story_text = "To Be Continued"

    player_choices = {
            "option_1":"not enabled",
            "option_2":"not enabled"}

    next_scenes = {
        "option_1":"filler_0",
        "option_2":"filler_1"}

    return story_text, player_choices, next_scenes


if __name__ == "__main__":