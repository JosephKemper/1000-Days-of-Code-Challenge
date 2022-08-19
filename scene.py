# Import the functions from the Draw 2-D library
# so that they can be used in this program.
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
    x = sun_position(scene_width)
    y = sun_position(scene_height)
    draw_sun(canvas,x,y)



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

def sun_position(scene_height=None, scene_width=None):
    if scene_height != None:
        y = scene_height-(scene_height/10)*2 
        return y
    if scene_width != None:
        x = scene_width/2
        return x


def draw_sun (canvas,x,y):
    pass

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