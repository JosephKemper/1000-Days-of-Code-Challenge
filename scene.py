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
    
    
    draw_forest(canvas)

  


    draw_grid (canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.



def draw_sky(canvas, scene_width, scene_height):
    """Draw the background sky color"""
    draw_rectangle (canvas,0,scene_height /3, 
    scene_width, scene_height, width=0, fill= "sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the background of the ground color"""
    draw_rectangle(canvas, 0,0,scene_width, scene_height/3, width=0,fill="tan4")

def sun_position(scene_width=0,scene_height=0):
    if scene_width != 0:
        x = scene_width/2
        return x
    if scene_height != 0:
        y = scene_height-(scene_height/10)*2 
        return y


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

def draw_row_trees(canvas,y):
        tree_position = random.randint(10,25)
        for i in range (40):
            chance = random.randint(1,10)
            interval = 20
            if chance >=4:
                draw_tree(canvas,tree_position,y,75)
            tree_position += interval

def draw_forest (canvas, y=150):
    for i in range (7):
        draw_row_trees(canvas,y)
        y=y-25

def draw_grid (canvas, width, height, interval, color = "blue"):
    label_y = 15
    for x in range (interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text (canvas, x, label_y, f"{x}",fill=color)
    
    label_x = 15
    for y in range (interval, width, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text (canvas, label_x, y, f"{y}",fill=color)

# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()