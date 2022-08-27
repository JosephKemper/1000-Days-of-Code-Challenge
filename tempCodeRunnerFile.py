def draw_grid (canvas, width, height, interval, color = "blue"):
    label_y = 15
    for x in range (interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text (canvas, x, label_y, f"{x}",fill=color)
    
    label_x = 15
    for y in range (interval, width, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text (canvas, label_x, y, f"{y}",fill=color)
