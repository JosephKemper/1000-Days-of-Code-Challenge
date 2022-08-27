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

    draw_oval(canvas, 50, 450, 200, 350, width=1, outline="black", fill="white")
    draw_oval(canvas, 100, 400, 250, 300, width=1, outline="black", fill="white")
    draw_grid (canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_grid (canvas, width, height, interval, color = "blue"):
    label_y = 15
    for x in range (interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text (canvas, x, label_y, f"{x}",fill=color)
    
    label_x = 15
    for y in range (interval, width, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text (canvas, label_x, y, f"{y}",fill=color)

main()