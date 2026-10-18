# Drone Movement Bug
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