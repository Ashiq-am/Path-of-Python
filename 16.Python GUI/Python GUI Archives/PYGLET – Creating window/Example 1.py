# importing pyglet module
import pyglet

# width of window
width = 500

# height of window
height = 500

# caption i.e title of the window
title = "Geeksforgeeks"

# creating a window
window = pyglet.window.Window(width, height, title)

# creating alabel
label = pyglet.text.Label('GeeeksforGeeks',
						font_name ='Times New Roman',
						font_size = 36,
						x = window.width//2, y = window.height//2,
						anchor_x ='center', anchor_y ='center')

# drawing label
@window.event
def on_draw():
	window.clear()
	label.draw()

# start running the application
pyglet.app.run()
