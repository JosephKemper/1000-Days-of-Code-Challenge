# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing, \
    draw_text


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)


    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    x = sun_position(scene_width,0)
    y = sun_position(0,scene_height)
    diameter = 50
    draw_sun(canvas,x,y,x+diameter,y+diameter)
    
    # Next steps draw mountains. 
    # Ideas for how mountains could look are at this link
    # https://byui-cse.github.io/cse111-course/lesson04/gallery/monica.png
    # I want to draw three super tall mountains in the background. 
    draw_mountain(canvas, scene_height/3.33,scene_width/2,scene_height, scene_width)
    draw_mountain(canvas, scene_height/2.5,scene_width/4,scene_height,scene_width)
    draw_mountain(canvas, scene_height/2.5,(scene_width-(scene_width/4)),scene_height,scene_width)
    
    draw_forest(canvas,scene_height,scene_width)

  


    draw_grid (canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


# Draw the sky to fill up about 2/3rds of the scene.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the background sky color"""
    draw_rectangle (canvas,0,scene_height /3, 
    scene_width, scene_height, width=0, fill= "sky blue")

# Draw the ground to fill about 1/3rd of the scene. 
def draw_ground(canvas, scene_width, scene_height):
    """Draw the background of the ground color"""
    draw_rectangle(canvas, 0,0,scene_width, scene_height/3, width=0,fill="tan4")

# Draw the sun to be about in the middle of the scene near the top. 
def sun_position(scene_width=0,scene_height=0):
    if scene_width != 0:
        x = scene_width/2
        return x
    if scene_height != 0:
        y = scene_height-(scene_height/10)*2 
        return y

# Draw mountains with snow on them
def draw_mountain(canvas, mountain_height, mountain_center, scene_height,scene_width):
    # Define the size of the mountain
    mountain_base = scene_height/3
    mountain_width = scene_width /2
    mountain_left = mountain_center - mountain_width/2
    mountain_right = mountain_center + mountain_width/2
    mountain_top = mountain_base + mountain_height

    # Define the snow cap of the mountain
    snow_top = mountain_top *1.1
    snow_width = mountain_width*0.7
    snow_base = scene_height/2
    snow_left = mountain_center - snow_width/3
    snow_right = mountain_center + snow_width/3
    
    
    # Draw snow cap of mountain
    draw_polygon(canvas,mountain_center, snow_top,
        snow_right, snow_base, snow_left, snow_base,
        outline="gray20", width=1, fill="floralWhite")


    # Draw the mountain
    draw_polygon(canvas,mountain_center, mountain_top, 
        mountain_right, mountain_base, mountain_left, mountain_base,
        outline="gray20", width=1, fill="antiqueWhite3")
    



def draw_sun (canvas,x,y,x1,y1,fill="yellow1"):
    draw_oval(canvas,x,y,x1,y1,fill="yellow")
    
def draw_tree(canvas, center_x,bottom,height):
    """Draw a single pine tree.
    Parameters
    canvas: The canvas where this function
    will draw a pine tree.
    center_x, bottom: The x and y location in pixels where
    this function will draw the bottom of a pine tree.
    height: The height in pixels of the pine tree that
    this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
       trunk_left, trunk_top, trunk_right, bottom,
       outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
        skirt_right, trunk_top,
        skirt_left, trunk_top,
        outline="gray20", width=1, fill="dark green")

def draw_row_trees(canvas,y,scene_width, scene_height):
        tree_position = int(random.randint(scene_width/50,scene_width/20))
        for i in range (35):
            chance = random.randint(1,10)
            interval = scene_width/18
            if chance >=3:
                draw_tree(canvas,tree_position,y,scene_height/10)
            tree_position += interval

def draw_forest (canvas, scene_height,scene_width):
    row_position = int(scene_height/3)
    for i in range(7):
        draw_row_trees(canvas,row_position,scene_height,scene_width)
        row_position = row_position - scene_height/20

def draw_grid (canvas, width, height, interval, color = "blue"):
    label_y = 15
    for x in range (interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text (canvas, x, label_y, f"{x}",fill=color)
    
    label_x = 15
    for y in range (interval, width, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text (canvas, label_x, y, f"{y}",fill=color)

# Added to allow portability of the functions in the program. 
if __name__ == "__main__":
# Call the main function so that
# this program will start executing.
    main()