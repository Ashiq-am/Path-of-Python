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
text = "Welcome to GeeksforGeeks Have a nice day"

# batch object
batch = pyglet.graphics.Batch()

# creating document
document = pyglet.text.document.FormattedDocument(text)

# setting style to the document
document.set_style(0, len(document.text), dict(
    font_name='Arial', font_size=16,
    color=(255, 255, 255, 255)))

# creating a incremental text layout
layout = pyglet.text.layout.IncrementalTextLayout(
    document, 400, 350, batch=batch)

# making layout to display multiline
layout.multiline = True

# creating a caret
caret = pyglet.text.caret.Caret(layout, color=(255, 255, 255))

# caret to winow push handlers
window.push_handlers(caret)

# setting caret style
caret.set_style(dict(font_name="Arial"))


# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the batch
    batch.draw()

    # caret to winow push handlers
    window.push_handlers(caret)


# creating a key state handler
key_handler = pyglet.window.key.KeyStateHandler()


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == key.C:
        # printng the message
        print("Key : C is pressed")


# image for icon
img = image = pyglet.resource.image("gfg.png")

# getting symbol string
value = key.symbol_string(121)

# creating text from the value
text = "Symbol string for value 121 : " + str(value)

# setting this text to the document
document.text = text

# setting image as icon
window.set_icon(img)

# start running the application
pyglet.app.run()
