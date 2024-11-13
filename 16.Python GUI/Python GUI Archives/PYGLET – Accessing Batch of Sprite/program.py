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

# creating a batch
batch = pyglet.graphics.Batch()

# loading geeksforgeeks image
image = pyglet.image.load('gfg.png')

# creating a list of sprites object
sprites = []

# position of images
pos_x = 10
pos_y = 230

for i in range(5):
    # temporary sprite object
    temp = pyglet.sprite.Sprite(image, pos_x, pos_y, batch=batch)

    # append the sprite object to the list
    sprites.append(temp)

    # increment the x co-orddinate
    pos_x = pos_x + 100


# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the label
    label.draw()

    # draw the batch
    batch.draw()


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == key.C:
        # printng the message
        print("Key : C is pressed")


# image for icon
img = image = pyglet.resource.image("gfg.png")

# setting image as icon
window.set_icon(img)

# getting batch of the first sprite
sprite = sprites[0]
value = sprite.batch

# setting this value to the lable
label.text = str(value)

# start running the application
pyglet.app.run()
