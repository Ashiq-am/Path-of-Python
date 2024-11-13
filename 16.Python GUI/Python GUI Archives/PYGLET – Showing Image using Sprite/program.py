# importing pyglet module
import pyglet
import pyglet.window.key as key

# width of window
width = 500

# height of window
height = 500

# caption i.e title of the window
title = "Geeksforgeeks"

# creating a window
window = pyglet.window.Window(width, height, title)

# text
text = "Welcome to GeeksforGeeks"

# creating label with following proeprties
# font = cooper
# position = 250, 150
# anchor position = center
label = pyglet.text.Label(text,
                          font_name='Cooper',
                          font_size=16,
                          x=250,
                          y=150,
                          anchor_x='center',
                          anchor_y='center')

# loading geeksforgeeks image
image = pyglet.image.load('gfg.png')

# creating sprite object
# it is instance of an image displayed on-screen
gfg_img = pyglet.sprite.Sprite(image, x=200, y=230)


# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the label
    label.draw()

    # draw the image on screen
    gfg_img.draw()


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == key.C:
        # printng the message
        print("Key : C is pressed")


# image for icon
img = image = pyglet.resource.image("gfg.png")

# getting mouse button string
value = pyglet.window.mouse.buttons_string(2 | 5)

# setting image as icon
window.set_icon(img)

# start running the application
pyglet.app.run()
