# importing pyglet module
import pyglet

# importing shapes from the pyglet
from pyglet import shapes

# width of window
width = 500

# height of window
height = 500

# caption i.e title of the window
title = "Geeksforgeeks"

# creating a window
window = pyglet.window.Window(width, height, title)

# creating a batch obect
batch = pyglet.graphics.Batch()

# properties of circle
# co-ordinates of circle
circle_x = 250
circle_y = 250

# size of circle
# color = green
size_circle = 100

# creating a circle
circle1 = shapes.Circle(circle_x, circle_y, size_circle, color=(50, 225, 30), batch=batch)

# changing opacity of the circle1
# opacity is visibility (0 = invisible, 255 means visible)
circle1.opacity = 250

# creating another circle with other properties
# new position = circle1_position - 50
# new size = previous radius -20
# new color = red
circle2 = shapes.Circle(circle_x - 50, circle_y - 50, size_circle - 20, color=(250, 25, 30), batch=batch)

# changing opacity of the circle2
circle2.opacity = 150


# window draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the batch
    batch.draw()


# run the pyglet application
pyglet.app.run()
