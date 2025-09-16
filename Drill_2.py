import math
from pico2d import *

def move_ractangle():
    x = 400
    y = 90
    if (x > 399):
        while (x < 800):
            clear_canvas_now()
            grass.draw(400, 30)
            character.draw_now(x, y)
            x = x + 2
            delay(0.01)

    if (x == 800):
        while (y < 599):
            clear_canvas_now()
            grass.draw(400, 30)
            character.draw_now(x, y)
            y = y + 2
            delay(0.01)

    if (y == 600):
        while (x > 0):
            clear_canvas_now()
            grass.draw(400, 30)
            character.draw_now(x, y)
            x = x - 2
            delay(0.01)

    if (x == 0):
        while (y > 90):
            clear_canvas_now()
            grass.draw(400, 30)
            character.draw_now(x, y)
            y = y - 2
            delay(0.01)

    if (x == 0 and y == 90):
        while (x < 400):
            clear_canvas_now()
            grass.draw(400, 30)
            character.draw_now(x, y)
            x = x + 2
            delay(0.01)

def move_circle():
    r = 210
    cx = 400
    cy = 300
    for i in range(270, 630 + 1, 1):
        clear_canvas_now()
        grass.draw(400, 30)
        x = cx + r * math.cos(i / 360 * 2 * math.pi)
        y = cy + r * math.sin(i / 360 * 2 * math.pi)
        character.draw_now(x, y)
        delay(0.01)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (True):
    move_ractangle()
    move_circle()