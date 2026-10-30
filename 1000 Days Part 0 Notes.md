# Saturday, 17 October, 2026
## Drone Movement Bug
What was happening with the first attempt of getting the lane grid set up was a two fold problem. 
1. The box collider system was overly complex and introduced problems with physics causing the colliders to be offset. 
2. The drone was being moved to exactly where the collider was at. 
Point 2 is why the lane grid seemed to disappear. The drone was being moved to the middle of the lane grid instead of keeping the lane grid in front of the drone. 
This means that whatever solution I create will need to have two things:
1. An in game (invisible) object for the player to tap/click on
2. A second point for where the player drone (i.e. the camera) to move to. 
Thus the problem I have right now, is the script moves the drone to the object I am clicking on, and that is creating the problem. I will also need to get whatever I am trying to click on set up properly. 
From further research, I think that using a UI button element will work the best for what the player clicks on. I just need to research strategies to figure out where the player moves to, which will need to be far enough behind the lane grid to keep it visible. 
## Possible solution to bug:
Add an empty game object to the structure that makes up the lane, and mark it as the place the drone moves to. Position it far enough back from the lane, to leave the lane visible to the player. 

# Monday, 19 October 2026
## UI Setup notes
While looking at the initial set up for the UI following AI instructions, I don't think it is heading in the right dirction. I got two buttons in and found a problem. The following along with a few screenshots is what I fed the AI
Either I'm doing something wrong, not quite got everything done, or we're heading in the wrong direction. Not all lanes will be visible on the play area at the same time. The buttons are supposed to be the lanes, and that means that if sized properly, it should be possible to not even see some of the buttons (lanes) if you were in the right lane. For example, if you were in lane 7, (once I have everything set up properly) you should not be able to see any of the top lanes (lanes 1, 2, and 3) or any of the right lanes (lanes 3, 6, and 9). 
From the initial buttons I created they are going to be all on screen, and all stuck at the top. 
The ideal for this game is that you click on the actual physical lane you want to move to and then click on it again and that will let you fire.
For this purpose I turned the original lane grid created (which I previously temporarily disabled) back on to detail the goal. Those blue lines visible in the play area, show what the player would see. Ideally, where you see the two red lines at, will be the whole play area, and the lanes will extend well beyond the visible play area. This means a few things:
1. We have the Canvas the wrong size. 
2. We need to put something to ensure that the buttons can actually go beyond the edge of the screen. 
To reiterate, there are not supposed to be separate visible buttons that you click on. The lanes themselves that the player will fly through are supposed to be the buttons. These will have the player ship moving through them along with various drops and obstacles.  
Thinking about this further, I've been previously making the lanes square and thinking about how to take up a huge amount of screen real-estate with UI layers, but if I make the lanes rectangular, then that can get the same thing accomplished by making it so that when held in Profile mode, and in a corner, you do not see the lanes on the opposite sides. 
I think I got the AI on the same page with me. 
Now, I just need to figure out how to let Unity let me get the UI bigger than the screen size and how to get it set up properly. 
From fidgeting with the button size I think I need to adjust some other settings. 
Right now, I'm set to scale with screen size, and no matter how I adjust the screen match mode, I can't get the buttons to go beyond the screen size. I'm guessing that is because of the Scale with Screen Size option. 
There are two other options in that same UI Scale Mode dropdown and I'm guessing it's one of those. 
Looking at the options on the other two, it seems to have far too many factors to figure out through trial and error. I certainly could but a little research can speed things up a lot. So, time to do some research. 

## Button Alignment Research
Decided on Constant Pixel size for LaneGrid. When placing buttons found that the only place they ever go is below the others. Need to research how to adjust button placement. Also, it does not seem to let me move them. 

# Tuesday, 20 October, 2026
## Customizing Buttons
I started to get the Buttons customized in appearance. First thing I deleted all but the first button, and then got I got the button to be transparent. I then got rid of the text from it. 
To make the button invisible, I had to open the color selections option and then under RGB color options turn the A to 0. Now, I need to figure out how to add an edge to the buttons. 
Deleted all but the base button. 
Learned about the Fill center option in the image options of the button. Left it as the default size for the edge as that was about the size I wanted for the edge. Got the colors set to what I wanted them to be. 
Recreated all 9 buttons from the template button. 

# Wednesday, 21 October, 2026
## Refactoring CameraLaneMover
Started working on refactoring the CameraLaneMover class. 
Stopping to think about it, I think part of the problem I'm having is the name of the class itself. 
PlayerController makes a lot more sense. It's job is to carry out the actions the player trys to handle. 
Those actions will be movement and firing. 
The movement and firing will both respond based on the same button. 
...
I need to get more clarity about this. 
...
So, what are the details to the problem?
9 lanes marked by lane sized buttons
Clicking a button should first move you to that lane. 
If you are in that lane, then pressing that same button again will fire the gun. 
In game components
9 buttons
9 LaneMarkers
The 9 buttons are part of the UI canvas
The 9 LaneMakers are empty game objects positioned to be roughly in the middle of the lanes(marked by the visible edges of the lane sized button)
...
When you press the button I want the camera to move over the button without going over the edge of the play area. 
## Camera Bug
The Camera has somehow become locked in position in place centered on the first button. 

# Thursday, 22 October, 2026
Let's start with the high level details of my class PlayerController
It takes in a click from any of the 9 buttons
checks if the player is in the lane that button represents
if not, it moves them to that lane. 
If so, it fires the gun. 
I think I want the current lane handled by a variable. 
I will want to ensure that firing of the gun is able to tracked by the class I will build later to handle collectables and such. 

Problem
9 buttons, 9 spots to move. 
I need to map each button to it's respective spot. 
I need to find a way to get the camera to stop at the edge of the play area when on an edge. 
I need to find a way to check for legal moves. Technically, the size of the buttons means that they will only ever be able to select a legal move. So, for now, I will just skip this, and just get the rest of the game working. 
I think for now, I will also skip on worrying about having the camera stop at the edge of the map. 

Summary
PlayerController
Upon button click
checks to see currentLane == Button pressed
if yes, then it fires the gun. 
If no, it moves the camera to the position for the button pressed. 
When it fires the gun, a future class needs to be able to track the firing of the gun for ammo tracking purposes. 
Requirements. This class will need to have the ability to map 9 buttons to 9 different locations represented by in game objects. I want this to be done in Unity manually. 

# Friday, 23 October, 2026

I need to get clear about what I need with the buttons. I need to get way clear. That is my problem with getting them created. I am not clear enough with what I want. So, I will start with the end experience and move backwards. I think I might describe from the character's experience first. 

Game Details
Being built in Unity 6
Mobile first via web development goal WebGL
3D infinite runner
Game consists of 9 lanes of travel arranged in a 3x3 grid. 

Inferno Jockey= An independent contractor paid to go to the molten world of Krneal to tag, harvest, and deliver Kytherium to one of the major refineries who turn it into useable materials. Kytherium is a natural super conductor. 

In game perspective of what happens in a run. 
Inferno Jockey flies into orbit around Krneal. 
Moves over to drone control station of his/her ship. 
Presses the launch button for the drone. 
looks at display screen. 
The ship's computer divides the refinery equipment on Krneal into a 3x3 grid of 9 lanes via an onscreen HUD using the recommended patterns given by the refineries. 
The video size from the drone is intentionally small for multiple reasons. 
1. It keeps the heat lower in both the drone and the ship. 
2. The drone is one time use only so keeping costs lower is good. 
3. Interference from Krneal's atmosphere prevents any higher resolution video streams. 

You get enough of a video to see one full lane and a portion of any surrounding lanes. 
To move to a lane, you simply need to tap on any visible portion of that lane on the display. 
If you are already in the lane, you can fire the gun on the drone by tapping on the lane you are currently in. 

Unrelated Lore
Even with the special cooling tech that the ship has by the end of a run, it is not uncommon for the temperature in the ship to get to 150 Degrees F. Experienced Inferno Jockeys will purchase special cooling suits and then will stay in orbit until the temperature gets in excess of 300 degrees. Legend has it that the best Inferno Jockey flew his one drone long enough that it got superheated and then turned to slag midair all while battling 500 degree temperatures in his ship. 
If you get in a bar where Inferno Jockeys are bragging, you will quickly realize that every last one of them try for that same ideal. They brag about how hot the drone got before it crashed, and how hot their ship got during the run. 


UI needs (for initial build)
Main Menu (initial build)
One Launch button on a computer looking terminal screen. 
An Exit button. 
Future updates will expand this to include things like missions and upgrades. 

The Launch button launches the game. 
Exit button, exits the game. 

In Game UI needs
A visible grid that looks like a projection that a computer might display over a low resolution screen marking the lanes. 
9 invisible buttons that are clickable/tappable
When pressed the buttons will first center the camera on the center of the button, and then, if they are already in the lane for the button in question, a second press will fire the gun. 

For clarity, if the player is centered over lane 1, they will see all of lane 1, and parts of lanes 2, 4, and 5, and will be able to click on any of the visible lanes to move to them. The rest of the lanes would not be visible. If they then clicked on lane 5 (the center lane) that would put them in the only point where they could see parts of all lanes. In lane 5, they would see all of lane 5 and parts of all of the other lanes. 

# Saturday, 24 October, 2026
I think I'm going to go way simpler for my game design. Instead of 9 invisible buttons, I will try to add 9 visible buttons below the view area. From there, I can upgrade the game later on. 

# Wednesday, 28 October, 2026
A Serious win for my new framework today. I was on top of my game enough today, that I had a few hours to work on my programming and finally made some progress on my game. I now have working buttons for the first time since I started working on the game. They are not working exactly the way I want them to, but they are working. 
The solution I needed was to put the Render Mode for the Canvas to World Space, and then put it as a child under the camera. From there, I formally decided that the camera and lane grid will not move, but the obstacles will move towards the camera while it moves around the x and y axis. I also had to adjust the scale and size in the Rect Transform area to get everything finally looking right. I was so happy when I got it working in the slightest. 

# Thursday, 29 October, 2026
Goal for the day is to confirm I got the buttons working properly and to get the camera position properly. As this is meant to be a simple and ugly game, if I cannot get the camera position just right, then that is fin. As long as I can get it 70% right, then I'm fine. 
So, right now, it almost seems random for how the buttons move. The AI seems to think it's connected with the offset, but I think it's a bit more than that. Time to find out. 
Button Change patterns
Starting Lane = 7
Clicking on the 7 button moves to lane 1. 
Clicking on the 1 buttong moves to lane 7
Clicking on the 4 button moves to lane 4
Clicking on the 5 button moves to lane 5. 

So, the whole thing is inverted. Clicking on the top row buttons take you to the mirror position button the bottom. 
Why?