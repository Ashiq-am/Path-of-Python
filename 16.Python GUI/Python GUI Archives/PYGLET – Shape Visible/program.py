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

# properties of rectangle
# co-ordinates of rectangle
co_x = 150
co_y = 150

# width of rectangle
width = 250

# height of rectangle
height = 150

# color = green
color = (50, 225, 30)

# creating a rectangle
rec = shapes.Rectangle(co_x, co_y, width, height, color=color, batch=batch)

# changing opacity of the rect1
# opacity is visibility (0 = invisible, 255 means visible)
rec.opacity = 180

# creating another rectangle with properties
# x, y co ordinate : 50, 250
# width, height of rectangle : 300, 200
# color = red
color = (255, 25, 25)

# properties of circle
# co-ordinates of circle
circle_x = 200
circle_y = 300

# size of circle
# color = green
size_circle = 100

# creating a circle
circle = shapes.Circle(circle_x, circle_y, size_circle, color=(250, 22, 30), batch=batch)

# changing opacity of the circle1
# opacity is visibility (0 = invisible, 255 means visible)
circle.opacity = 170


# window draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the batch
    batch.draw()


# accessing visible of rectangle
value_rec = rec.visible

# printing value
print("Rectangle : ", end="")
print(value_rec)

# accessing visible of circle
value_cir = circle.visible

# printing value
print("Circle : ", end="")
print(value_cir)

# run the pyglet application
pyglet.app.run()
