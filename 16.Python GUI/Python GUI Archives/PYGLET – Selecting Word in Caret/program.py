# importing pyglet module
import pyglet
import pyglet.window.key

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

# creating a caret
caret = pyglet.text.caret.Caret(layout, color=(255, 255, 255))

# caret to winow push handlers
window.push_handlers(caret)

# moving caret to point
# editable mark
value = caret.move_to_point(100, 30)


# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the batch
    batch.draw()

    # caret to winow push handlers
    window.push_handlers(caret)


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == pyglet.window.key.C:
        # closing the window
        # window.close()
        pass


# image for icon
img = image = pyglet.resource.image("logo.png")

# setting image as icon
window.set_icon(img)

# selecting word which is nearest to 150, 100
caret.select_word(150, 100)

# start running the application
pyglet.app.run()
