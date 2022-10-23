# Made sure there were at least three levels of choices. 
# Showed the program to both my brother and my wife. Explained it to both and let both play with it. 
# Not all paths have been fully expanded. I pushed myself to my limits on this project. 

# Lessons I learned while creating this program. 
# 1. I learned how to define and use functions
# 2. I learned how to make and use while loops to force a user into selecting from a preselected option
# 3. I learned how to force the program to stop running at a certain point
# 4. I learned how to pause the program and wait for a response from the user

# Things I would do better next time
# 1. I would focus less on trying to tell a wonderful story, and more on programming. 
# I think I could have gotten a lot farther if I had. Yes, I met or exceeded all the requirements. 
# I just feel I could have done more if I would have shifted focus a bit. 
# 2. I would write all the dialog in a word processor and then copy it into notepad, and then to visual studio code program. 
# That would let me have the advantage of a spell and grammar check while still not having odd copy paste errors
# One I consistently ran into was one that did not like how apostrophes translated over when copying text. 
# 3. I would use some kind of whiteboard program to map out the different options for the story
# Then I would take and map out the functions and variables I want to use in the program. 
# From there, I would take and put it all together. 
# I think that would make for a better more cohesive experience. 

# For use in sleep functions 
import time



# Built to give the user the option to read at their own pace. 
def reading_pause ():
    print ()
    time.sleep (1)
    input ("Press enter to continue ...")
    print ()




print ("Welcome to the Adventure Game!")


time.sleep(1)
print ()

#Setting Expectations for player
print ("To get started we need to collect a bit of info from you.")
print ("This will be used in the game to customize the experience.")
time.sleep(1)
print ()

#Getting player name       
player_name = input ("Please enter your desired character name: ")
time.sleep(1)
print ()

# Built to force the player to only choose one of the presented options, as in this case it would ruin the story if I did not force the choice. 
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
print ("When you are given a choice, the two most obvious choices will be listed in all caps")
reading_pause ()

print ("However, you should remember, there may be more choices available than what is most obvious, and they may not even be mentioned.")
reading_pause ()

print ("Then again, maybe the only choices are the obvious ones. Are you brave enough to find out ...")
reading_pause ()

#Pronouns for usage in dialog. 
#Goal was to just reference the variable 
# and let the computer use the player gender to choose the variable

if  player_gender.lower () == "male":
    he_she = "he"
    him_her = "him"
    his_her = "his"
    boy_girl = "boy"
    brother_sister = "brother"
    son_daughter = "son"
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
    his_her = "her"
    boy_girl = "girl"
    brother_sister = "sister"
    son_daughter = "daughter"
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

# Scenes were built with inention of both simplifying the code and with making it reusable in later expansion of code. 
def intro_scene ():
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
    reading_pause ()


    print ("In the middle of your preparations to get ready for your weekend, you hear an unfamiliar voice shouting just outside your house.")
    reading_pause ()

    print (f'"{player_name.capitalize ()} should be inside, get {him_her} now. The High {enemy_leader} wants {him_her} alive and in one piece."')
    reading_pause ()

    print (f"As you look out the window, you see a dozen strangely dressed {men_women} carrying large swords angrily moving towards your home.")
    reading_pause ()

    print ("""You're at your dad's old cabin, miles out of town. 
Even if they went 80, it would take the police 30 minutes to get out here, 
and you're not sure if you can get signal anyway.""")
    reading_pause ()

    print (""""Police can't help me." You think to yourself. "I need to think of other options." """)
    reading_pause ()

    print ("""I could try to HIDE and hope they don't find me, 
or I could try to ESCAPE out the window and make a break for it. 
The forest is not far, 
I could hide in there forever.""")
    reading_pause ()



def closet_scene ():
    print ("""You quickly duck in the closet and hide, 
but as they continue to search the house determined to find you, 
your nerves start to get the better of you.""")
    reading_pause ()

    print ("You hear several people moving closer to the closet door.")
    reading_pause ()

    print (f"""When the door opens, 
you see six large {opposite_men_women}, 
dressed in blood red robes with masks covering their faces, 
and giant swords pointing towards you.""")
    reading_pause ()
    
    print ("""They quickly restrain you, 
put a thick black cloth hood over your face as you find yourself losing consciousness.""")
    reading_pause ()  



def window_escape_scene ():
    print ("""You carefully look out the back window, 
making sure not to be seen, 
waiting until all of the cultists start making their way into the front door. 
You quickly open the window and run as fast as you can into the forest.""")
    reading_pause ()

    print (f"""Just as you get to the tree line you hear someone yell behind you 
{he_she}'s running into the forest. The yelling and loud footsteps behind you, 
tells you that the whole group is chasing after you and drives you to run faster. 
You duck behind a bush, then notice a cave in the side of the nearby mountain 
and quickly run for it.""")
    reading_pause ()

    print ("""As you sprint to the cave, 
a giant sword flies so close to your head that it nicks your ear. 
You almost feel as though the force of the wind from the sword flying by you might have knocked you over, 
but the force of trees exploding into little pieces of shrapnel in front of you after the sword tore through it 
and the tree in front of it certainly did knock you over, and seeing the sword fly back over your face, 
barely missing your nose as you tumble to the ground makes you grateful you only hit your head on a rock.""")
    reading_pause ()

    print ("""As you quickly struggle to your feet, 
feeling a little disoriented from the explosion, 
you don't stop to listen to the argument between two of the cultists not far behind you. 
You just run. You run for your life. 
You run with all the energy of two trees exploding into little pieces of shrapnel that are still covering much of your body.""")    
    reading_pause ()

    print ("""As you duck into the cave, you stop in horror to find it barely goes back 6 feet. 
With the sun behind the mountain that 6 feet is certainly dark, 
but the pain from hundreds of pieces of wood embedded into your flesh testifies that what you thought you knew cannot be true. 
Hundreds of points of terrible pain and the memory of a giant sword flying back over your face, 
returning as though on command to its wielder, leaves you with a perfect conviction, 
that there is a lot you do not know about the world. There is a lot even science does not know about the world. """)
    reading_pause ()

    print ("""You stand there, back pressed firmly against the rock, 
in perfect silence for what feels like an eternity, wrapped in a gem, and gifted back to you. 
Waiting. Listening. Feeling. But there's more. So much more. 
Part of you wants to just melt into the rock and hope these freaks never find you. 
Part of you wants to grab the nearby branch, left over from one of the exploding trees, 
and see how many of them you can take out. Part of you wants to fall to your knees and cry, 
but you know there is no time for that right now.""")
    reading_pause ()
  



def going_for_gun_scene ():
    print ("""You suddenly remember your dad's old shotgun he used for bird hunting and run to grab it, 
hoping it still works and is loaded, or at least still has ammo.""")
    reading_pause ()
    
    print (""""On the third attempt at remembering the password to the safe, 
you get it open and quickly discover that there are only a few shells in the safe but no gun.""")
    reading_pause ()
    
    print ("""As the cultists burst in the door, you remember your dad telling you 
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









def intro_panic_scene ():
    print ("""As you look out the window, 
you freeze in terror at the sight of seeing so many people dressed in what looked like blood died robes 
carrying what you can only figure was executioner swords.""")
    reading_pause ()

    print ("""As the cultists burst through the door, 
you just stand there staring out the window, 
terrified at what might be happening next.""")
    reading_pause ()

    print ("""And as they tie your hands and feet up, 
then place a thick black cloth bag over your head, 
you remain just as paralyzed by fear, 
until the consciousness slips from your body.""")
    reading_pause ()



def altar_scene ():
    print ("You wake to find yourself staring up at a planet with the top of a massive mountain pointing right down at you.")
    reading_pause ()
        
    print ("""It takes a moment to work through the awe before you realize that you are tied to an altar of some kind 
and that the cultists who captured you are chanting in a strange language you've never heard.""")
    reading_pause ()

    print ("""Your hands and feet are bound, 
stretched to the point where it hurts. 
Your mouth is gagged, and your head seems bound preventing you from looking around.""")
    reading_pause ()

    print (f"""Suddenly the chanting stops and a {opposite_male_female} cultist, 
with gold inlays woven into {opposite_his_her} robe, 
with what could easily be a sacrificial knife in {opposite_his_her} hand...""")
    reading_pause ()

    print (f"""...{opposite_he_she.capitalize()} gently strokes your side with the side of the dagger 
and {opposite_he_she} seems to start speaking directly to you, 
but some strange language you've never heard before.""")
    reading_pause ()

    print (f"""{opposite_he_she.capitalize ()} suddenly stops speaking, laughs, 
and starts moving {opposite_his_her} hands in the air, 
a red line of pure energy following the intricate patterns {opposite_he_she} is moving {opposite_his_her} hands in. """)
    reading_pause ()

    print (f"""After just a moment, the rune {opposite_he_she} traced into the air starts to pulse and then slams down on your face, 
burning with intense pain, as your ears start to buzz to a painful level. 
The fact that you cannot move or speak only makes the feeling worse.""")
    reading_pause ()

    print (f"""As the pain subsides, the cult leader turns to someone out of site and shouts angrily 
“Why didn't that work?!?!
That should have worked! 
{player_name} should be able to understand me now, 
and my spell should be working its way to {his_her} heart and giving me control of {his_her} soul, 
but it failed, and the spell was rejected. 
Why was it rejected?!?! 
Answer me! 
Answer me Now!” """)
    reading_pause ()

    print ("""Just as she shouted “Now” three gunshots rang out in rapid succession. 
The lurch on one of your hands and feet tells you 
two of those shots likely loosened the ropes tying you to the altar. 
You're not sure you want to wait to find out. """)
    reading_pause ()

    





#Notifying the player that the game is beginning. 
print ("Let the game begin!")

#Processing Animation
time.sleep(1)
print ()
time.sleep(1)
print ()
time.sleep(1)
print ()


# The escape option leads to the path with the most choices
intro_scene ()

print ("What do you want to do... ")
first_choice = input ("HIDE in the closet or try to ESCAPE out the window? ")
if first_choice.lower () == "hide":
    intro_scene_choice = 1

elif first_choice.lower () == "escape":
    intro_scene_choice = 2

elif first_choice.lower () == "fight":
    intro_scene_choice = 3

else:
    intro_scene_choice = 4



if intro_scene_choice == 1:
    closet_scene ()

elif intro_scene_choice == 2: 
    window_escape_scene ()

elif intro_scene_choice == 3: 
    going_for_gun_scene ()

elif intro_scene_choice == 4:
    intro_panic_scene ()

# The fight option leads to the path with the most choices
if intro_scene_choice == 2:
    window_escape_scene_choice = input ("""What do you want to do:
Embrace the weird and try to MERGE into the rock,
or pick up the BRANCH and try to fight? """)
    
    if window_escape_scene_choice.lower () == "merge":
        print ("""You've seen enough weird stuff in the last few minutes what's the worst that could happen? 
You focus on the rock you have your back pressed against, hoping to merge into it, as suddenly you fall backwards … 
into a different … cave … 
as a group of creatures that look like they might be a cross between a mushroom, a frog, and a person, 
turn towards you, pick up their weapons and start moving in your direction.""")
        reading_pause ()

        print ("To be continued ...")
        exit ()
    
    elif window_escape_scene_choice.lower ()== "branch":
        print ("""As you look at the branch, and then at the splinters still covering your body, 
you realize that even if you make it out of this, you are going to miss your chance at the weekend of a lifetime, 
and that your life will likely never be the same again, 
and, as you think about that, rage enters your heart and you pick up the branch, charge towards the cultists, 
and swing with all the rage of a thousand splinters now soaking your best outfit in blood. 
You swing with all the rage of two trees exploding right in front of them. 
But no matter how hard you swing, the cultists easily take you down, 
place a thick black cloth bag over your face as you lose consciousness.""")

        intro_scene_choice = 1
    
    elif window_escape_scene_choice.lower () == "surrender":
        print (f""" “You're covered in your own blood. 
The nearest neighbor is 20 miles away, and they are gone on vacation to Italy. 
These cultists … these creatures are strong enough they literally threw a sword 
hard enough that it shattered two trees right in front of you. 
Just give up!” You think to yourself. 
As you step out of the cave you see a cultist carrying the same sword 
with the same designs that you saw nearly chop your head off. 
{he_she.capitalize ()} smiles, walks over to you, places his hand on your head and squeezes.
Just before you black out, you hear the bones in your skull cracking.""")
        reading_pause ()

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

        print (f"Who knows? Maybe I'll even ask {opposite_him_her} on a date.")
        time.sleep(2)
        print ()

        print ("Nothing could possibly ruin this day!")
        time.sleep(2)
        print ()

        print ("In the middle of your preparations to get ready for your weekend you hear an unfamiliar voice shouting just outside your house.")
        reading_pause ()

        print ("What just happened? I just died! I was covered in splinters and blood ... my own blood ... and now I'm back here!")
        reading_pause ()

        print ("To be continued ...")
        exit ()

    
    else:
        print (f""" “You're covered in your own blood. 
The nearest neighbor is 20 miles away, and they are gone on vacation to Italy. 
These cultists … these creatures are strong enough they literally threw a sword 
hard enough that it shattered two trees right in front of you. 
Just give up!” You think to yourself. 
As you step out of the cave you see a cultist carrying the same sword 
with the same designs that you saw nearly chop your head off. 
{he_she.capitalize ()} smiles, walks over to you, places his hand on your head and squeezes.
Just before you black out, you hear the bones in your skull cracking.
As you feel the taste of oblivion lapping up your soul.""")
        reading_pause ()
        
        print ("To be continued ...")
        exit ()




# All choices here lead to the end the program. 
if intro_scene_choice == 1 or intro_scene_choice == 3 or intro_scene_choice == 4:
    altar_scene ()
    
    altar_scene_choice = input("""What do you want to do? 
Try to break free of the ropes and ESCAPE, 
or WAIT and for whoever is shooting at the cultists, 
hoping they might finish freeing you… """)
    if altar_scene_choice.lower () == "escape":
        altar_scene_choice = 1
    
    elif altar_scene_choice.lower () == "wait":
        altar_scene_choice = 2
    else:
        altar_scene_choice = 2




if altar_scene_choice == 1:
    print ("""As fighting erupts around the altar you are tied to, you start to struggle, 
desperately hoping that the bullets weakened the ropes enough to let you escape. 
You can still barely move, pulled so tight that even breathing is hard, 
but you keep struggling. 
You feel a drip of what you're certain is blood, 
dripping down your wrist from trying to break free of the ropes that hold you bound, 
but you keep struggling.""")
    reading_pause ()

    print ("""Just as you break your arm free, 
you notice that the mountain top that was pointing towards you 
is now almost aligned with the mountain near where you are bound, 
and that you might be able to hike … up one mountain … down another … and end … on another world … 
the fighting still raging around you, reminds you to keep struggling to get free. 
It reminds you, that your life is still very much in danger.""")
    reading_pause ()

    print ("""Despite your arm being free, 
you realize that with how tight your other three limbs are pulled, 
you can't reach your other arm to get loose, 
so you keep struggling with your leg to break free, 
while you try to figure out what is holding your head in place.""")
    reading_pause ()

    print ("""Just as you break your leg free of the rope holding it to the altar, 
you find a latch on the … clamp … holding your head in place, 
you lift the latch and get your other two limbs free. 
Looking briefly at the fighting you're not sure who is winning, 
or what the people with guns want, 
but you're pretty sure one of them is not happy to see you loose from the altar, 
and seeing the urgency the rest of them start fighting with once he made it known to his companions, 
only raises your concerns.""")
    reading_pause ()

    print ("To be continued ...")
    exit ()

elif altar_scene_choice == 2:
    print ("""As you wait, you see the top of the mountain pointing down at you 
from the other planet aligning with the mountain on the planet you are on. 
Despite how tightly you are bound to the altar, you still feel lighter 
… maybe heavier … maybe both. 
You're not really sure, 
but you think it might be related to the alignment of the two twin planets, 
and, as the two mountains finish their alignment, the sounds of fighting stop. 
You hope that someone who wants to save you won, but can only wait.""")
    reading_pause ()

    print (f"""Dread enters your heart as you see the same cultist who spoke to you before, 
walk into view. Blood partially staining some of the gold inlays on {opposite_his_her} robe. 
{opposite_he_she.capitalize ()} raises the now blood soaked dagger still in {opposite_his_her} hand
and says “No more distractions!” then plunges the dagger into {opposite_his_her} own chest. 
As {opposite_his_her} body slumps over yours, 
you again feel the same burning you felt before but this time it is more than pain … more than agony … 
it is the voice of a million innocent victims crying out in agony 
as this demon tortured them until every last ounce of self was gone. 
It is the tears of their loved ones, as they were left to watch in terror
as their former {brother_sister}'s and {son_daughter}'s show back up 
and mindlessly destroy their own families, 
while they watch helplessly, prisoners in their own bodies.""")
    reading_pause ()

    print (f"""The feeling of a star, splashing in the … liquid … that washed over your foot woke you up. 
Looking at the … sea you are lying next to, you see what looks like space held in an ocean. 
A little above you is another island floating on a separate sea of space, a nebula, 
nestled perfectly under the island, leaving just enough of its edges in view to form a sort of halo capping off the nebula. 
The ground around you is scorched to the point where it almost turned to glass, 
and off in the distance you see a timid little {boy_girl} point in your direction and then run off
as the group of at least a hundred soldiers following {him_her} ready their weapons and march in battle formation towards you.""")
    reading_pause ()

    print ("To be continued ...")
    exit ()










