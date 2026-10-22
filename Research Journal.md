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