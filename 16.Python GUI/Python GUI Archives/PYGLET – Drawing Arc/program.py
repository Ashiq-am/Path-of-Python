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
arc_x = 250
arc_y = 250

# size of arch
size_arc = 100

# segments
segments = 5

# angle
angle = 20

# color = green
color = (50, 225, 30)

# creating a arc
arc1 = shapes.Arc(arc_x, arc_y, size_arc, segments, angle, color, batch=batch)

# changing opacity of the arc1
# opacity is visibility (0 = invisible, 255 means visible)
arc1.opacity = 250

# creating another circle with other properties
# new position = circle1_position - 50
# new size = previous radius -20
# new color = red
color = (255, 30, 30)

# increse segments
segments = 10

# decreasing angle
angle = 7

# creating another arc
arc2 = shapes.Arc(arc_x - 50, arc_y - 50, size_arc - 20, segments, angle, color, batch=batch)

# changing opacity of the arce2
arc2.opacity = 255


# window draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the batch
    batch.draw()


# run the pyglet application
pyglet.app.run()
