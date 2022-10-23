#Used for time.sleep function. 
#Slows the program down and avoide the user feeling rushed. 
import time

def reading_pause ():
    print ()
    time.sleep (1)
    input ("Press any key to continue ...")
    print ()



#Want a better name for the intro. 
#Will likely need to complete the program first to know what I want to call it. 
print ("Welcome to the Adventure Game!")

#Deliberate space and pause for aesthetic purposes. 
time.sleep(1)
print ()

#Setting Expectactions for player
print ("To get started we need to collect a bit of info from you.")
print ("This will be used in the game to customize the experience.")
time.sleep(1)
print ()

#Getting player name       
player_name = input ("Please enter your desired character name: ")
time.sleep(1)
print ()

#While loop used to force one of the two programmed options. 
#Plan to customize pronouns based on player gender in dialog in game. 
#Had to learn how to use the while loop. 
#Sample scripte online has an ";" after the break 
# that did not stop the script from working but did mess with the if statement afterwards. 
#I spent a few hours trying to figure that bug out. 
#Initially, the code presented a syntex error that pointed to the print statement in the first line that used a pronoun. 
#The error tried to say that the formating of the print statement was wrong. 
while True:
    try:
        player_gender = input ("Please select a gender for your character. MALE or FEMALE: ")
        if player_gender.lower () == "male" or player_gender.lower () == "female":
            print ("Information entered successfully...")
            print ()
            break
        else:
            print ("Gender should either be entered as either MALE or FEMALE.")
    except:
        continue


#Procesing animation
time.sleep(1)
print ()
time.sleep(1)
print ()
time.sleep(1)
print ()
time.sleep(1)
print ()

#Confirmation for player letting them know what the computer got from them. 
#Ideally, I would like to put in an option to reenter if they are not happy. 
#Will need to figure out how to do that. 
print (f"In this game your character is named {player_name.capitalize()} and is a {player_gender.lower()}.")
reading_pause ()

#Setting player expectations
print ("When you are given a choice, the two most obvious choices will be listed in all caps in the dialog before the choice is given and in the question asking for your choice.")
reading_pause ()

print ("However, you should remember, there may be more choices available than what is most obvious, and they may not even be mentioned.")
reading_pause ()

print ("Then again, maybe the only choices are the obvious ones. Are you brave enough to find out ...")
reading_pause ()

#Pronouns for useage in dialog. 
#Goal was to just reference the variable 
# and let the computer use the player gender to chose the variable

if  player_gender.lower () == "male":
    he_she = "he"
    him_her = "him"
    boy_girl = "boy"
    male_female = "male"
    men_women = "men"
    man_woman = "man"
    love_interest = "girl"
    opposite_male_female = "female"
    opposite_men_women = "women"
    opposite_he_she = "she"
    opposite_his_her = "her"
    opposite_him_her = "her"
    enemy_leader = "Lady"

elif player_gender.lower () == "female":
    he_she = "she"
    him_her = "her"
    boy_girl = "girl"
    male_female = "female"
    men_women = "women"
    man_woman = "woman"
    love_interest = "guy"
    opposite_male_female = "male"
    opposite_men_women = "men"
    opposite_male_female = "male"
    opposite_he_she = "he"
    opposite_his_her = "his"
    opposite_him_her = "him"
    enemy_leader = "Lord"

#Notifying the player that the game is begning. 
print ("Let the game begin!")

#Processing Animation
time.sleep(1)
print ()
time.sleep(1)
print ()
time.sleep(1)
print ()


#Deliberately chose to slow down the speed of the text
#Wanted to give user a chance to read and enjoy the text of the game
print ('"Today is going to be great!" You think to yourself.')
time.sleep(2)
print ()

print ("I got the day off.")
time.sleep(2)
print ()

print ("My friends and I have an amazing weekend planned.")
time.sleep(2)
print ()

print (f"I might even see that really cute {love_interest} again.")
time.sleep(2)
print ()

print (f"Who knows! Maybe I'll even ask {opposite_him_her} on a date.")
time.sleep(2)
print ()

print ("Nothing could possibly ruin this day!")
print ()
time.sleep(1)
input ("Press any key to continue ...")
print ()


print ("In the middle of your preparations to get ready for your weekend you hear an unfamiliar voice shouting just outside your house.")
reading_pause ()

print (f'"{player_name.capitalize ()} should be inside, get {him_her} now. The High {enemy_leader} wants {him_her} alive and in one piece."')
reading_pause ()

print (f"As you look out the window you see a dozen strangely dressed {men_women} carrying large swords angrily moving towards your home.")
reading_pause ()

print ("""You're at your dad's old house, miles out of town. 
Even if they went 80 it would take the police 30 minutes to get out here.""")
reading_pause ()

print (""" "Police can't help me." You think to yourself. "I need to think of other options." """)
reading_pause ()

print ("""I could try to HIDE and hope they don't find me, 
or I could try to ESCAPE out the window and make a break for it. 
The forest is not far, 
I could hide in there forever.""")
reading_pause ()

#First player choice. 
print ("What do you want to do... ")
first_choice = input ("HIDE in the closet or try to ESCAPE out the window? ")
if first_choice.lower () == "hide":
    player_choice = 1

elif first_choice.lower () == "escape":
    player_choice = 2

elif first_choice.lower () == "fight":
    player_choice = 3

else:
    player_choice = 4

if player_choice == 1:
    print ("""You quickly duck in the closet and hide, 
    but as they continue to search the house determined to find you, 
    your nerves start to get the better of you.""")
    reading_pause ()

    print ("You hear several people moving closer to the closet door.")
    reading_pause ()

    print ("""When the door opens, 
    you see six large men, 
    dressed in blood red robes with masks covering their faces, 
    and giant swords pointing towards you.""")
    reading_pause ()
    
    print ("""They quickly restrain you, 
    put a thick black cloth hood over your face as you find yourself losing consciousness.""")
    reading_pause ()


elif player_choice == 2: 
    print ("""You carefully look out the back window, 
    making sure not to be seen, 
    waiting until all of the cultists start making their way into the front door.""")
    reading_pause ()

    print ("You quickly open the window and run as fast as you can into the forest.")
    reading_pause ()

    print (f"""Just as you get to the tree line you hear someone yell behind you 
    {he_she}'s running into the forest.""")
    reading_pause ()

    print ("""The yelling and commotion behind you, 
    tells you that the whole group is chasing after you.""")
    reading_pause ()


    print ("""You duck behind a bush, 
    then notice a cave in the side of the nearby mountain 
    and quickly run for it.""")
    reading_pause ()


#First hidden choice   
elif player_choice == 3: 
    print ("""You suddenly remember your dad's old shotgun he used for bird hunting and run to grab it, 
    hoping it still works and is loaded, or at least still has ammo.""")
    reading_pause
    
    print (""""On the third attempt at remembering the password to the safe, 
    you get it open and quickly discover that there are only a few shells in the safe but no gun.""")
    reading_pause ()
    
    print ("""As the cultists burst in the door you remember your dad telling you 
    he was going to sell it for you because he knew just how much you hated guns.""")
    reading_pause ()
    
    print (f"""As much as you want to fight, 
    with six huge {men_women} all pointing the largest swords you have ever seen in your direction, 
    you decide that fighting might not be the best option, 
    especially without a weapon of your own.""")
    reading_pause ()
    
    print ("""You put your hands up to surrender, 
    and as you go to ask what this is about, 
    one of the cultists quickly puts a black cloth bag over your head and you find yourself losing consciousness.""")
    reading_pause ()


#Second hidden choice
elif player_choice == 4:
    print ("""As you look out the window, 
    you freeze in terror at the sight of seeing so many people dressed in what looked like blood died robes 
    carying what you can only figure was executioner swords.""")
    reading_pause ()

    print ("""As the cultists burst through the door, 
    you just stand there staring out the window, 
    terrified at what might be happening next.""")
    reading_pause ()

    print ("""And as they tie your hands and feet up, 
    then place a thick black cloth bag over your head, 
    you remain just as paralyzed by fear, 
    until the consciousness slips from your body.""")




#I both demoed and explained my code so far, to both my wife and my brother. 

if player_choice == 1 or player_choice == 3 or player_choice == 4:
    print ("You wake to find yourself staring up at a planet with the top of a massive mountain pointing right down at you.")
    reading_pause ()
        
    print ("""It takes a moment to work through the awe before you realize that you are tied to an alter of some kind 
    and that the cultists who captured you are chanting in a strange language you've never heard.""")
    reading_pause ()

    print ("""Your hands and feet are bound, 
    stretched to the point where it hurts. 
    Your mouth is gagged, and your head seems bound preventing you from looking around.""")
    reading_pause ()

    print (f"""Suddenly the chanting stops and a {opposite_male_female} cultist, 
    with gold inlays woven into {opposite_his_her} robe, 
    with what could easily be a sacrificial knife in {opposite_his_her} hand.""")
    reading_pause ()

    print (f"""{opposite_he_she.capitalize()} gently strokes your side with the side of the dagger 
    and {opposite_he_she} starts seems to start speaking directly to you, 
    but some strange language you've never heard before.""")
    reading_pause ()

    print (f"""{opposite_he_she.capitalize ()} suddenly stops speaking, laughs, 
    and starts moving {opposite_his_her} hands in the air, 
    a red line of pure energy following the intricate patterns {opposite_he_she} is moving {opposite_his_her} hands in. """)
    reading_pause ()

    print ("""After just a moment, the ruin starts to pulse and then slams down on your face, 
    burning with intense pain, as your ears start to buzz to a painful level. 
    The fact that you cannot move or speak only makes the feeling worse.""")
    reading_pause ()

    print ("""As the pain subsides you the cult leader turns to someone out of site and shouts angrily 
    “Why didn't that work? 
    That should have worked! {player_name} should be able to understand me now, 
    and my magics should be working their way to {his_her} heart and giving me control of {his_her} soul, 
    but it failed, and the spell was rejected. Why was it rejected? Answer me! Now!” """)
    reading_pause ()

    print ("""Just as she shouted “Now” three gunshots rang out in rapid succession. 
    The lurch on one of your hands and feet tells you 
    two of those shots likely loosened the ropes tying you to the alter. 
    You're not sure want to wait to find out. """)
    reading_pause ()

    second_choice = input("""What do you want to do? 
    Try to break free of the ropes and ESCAPE, 
    or WAIT and for whoever is shooting at the cultists, 
    hoping they might finish freeing you… """)

    if second_choice.lower () == "escape":
        player_choice = 5
    
    elif second_choice.lower () == "wait":
        player_choice = 6
    
    elif second_choice.lower () == "power":
        player_choice = 7

    else:
        player_choice = 8
