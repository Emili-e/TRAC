import pyglet
import math

from pyglet.window import Window
from pyglet.media.synthesis import Sine
from pyglet import shapes
from math import cos, sin


# Window --------------------------------------------#

# window parameters
width, height = 500, 500
title = "j'en ai marre"

# create a window and set background color (white)
window = Window(width, height, title)
pyglet.gl.glClearColor(1, 1, 1, 1)

# -------------------------------------------------- #




# Constantes --------------------------------------- #
# batch
batch = pyglet.graphics.Batch()

# line parameters
distance = 50

# color
redd = (255, 0, 0)
green = (0, 255, 0)
bluee = (0, 0, 255)
black = (255, 255, 255)
baba = (47, 38, 25)


# Drawing zigzag line function --------------------- #

def drawZigZag(x, y, dx, dy, angle, color, zigzag_list, batch=None):
    x1 = x
    y1 = y
    x2 = x + dx
    y2 = y+dy

    x3 = x2
    y3 = y2

    x4 = x2 + dx
    y4 = y

    for i in range(1, 7):
        linex = shapes.Line(x1, y1, x2, y2, width=2, color=color, batch=batch)
        linex.opacity = 250
        zigzag_list.append(linex)

        x1 = x1 + 2*dx
        x2 = x2 + 2*dx

        liney = shapes.Line(x3, y3, x4, y4, width=2, color=color, batch=batch)
        liney.opacity = 250
        zigzag_list.append(liney)

        x3 = x3 + 2*dx
        x4 = x4 + 2*dx


# Main ----------------------------------------------- #

x = 50
y = 50
angle = 70
dx = distance*cos(angle)
dy = distance*sin(angle)
zigzag_list = []


@window.event
def on_draw():
    window.clear()
    batch.draw()

color = (0, 0, 0)

if __name__ == '__main__':
    
    drawZigZag(x, y, dx, dy, angle, color, zigzag_list, batch=batch)
    # drawZigZag(x+50, y+50, dx+10, dy+10, baba, angle, zigzag_list, batch=batch)
    pyglet.app.run()