# Example 5

from draw2d import start_drawing, draw_oval, finish_drawing
import random

def main():
    scene_width = 600
    scene_height = 375

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Random Locations",
            scene_width, scene_height)

    diameter = 15
    space = 5
    interval = diameter + space

    # Draw a row of circles with
    # some of the circles missing.
    x = 100
    y = 300
    for i in range(20):
        number = random.randint(1, 5)
        if number > 1:
            draw_oval(canvas, x, y,
                    x + diameter, y + diameter, fill="yellow2")
        x += interval

    half_height = round(scene_height / 2)
    min_diam = 15
    max_diam = 30

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(100):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="mediumOrchid1")

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Call the main function so that
# this program will start executing.
main()