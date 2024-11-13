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
text = "Welcome to GeeksforGeeks"

# batch object
batch = pyglet.graphics.Batch()

# creating document
document = pyglet.text.document.FormattedDocument(text)

# setting style to the document
document.set_style(0, len(document.text), dict(font_name='Arial', font_size=16, color=(255, 255, 255, 255)))

# creating a incremental text layout
layout = pyglet.text.layout.IncrementalTextLayout(document, 400, 50, batch=batch)

# creating a caret
caret = pyglet.text.caret.Caret(layout, color=(255, 255, 255))


# caret to winow push handlers
# window.push_handlers(caret)

# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the batch
    batch.draw()

    # window push handlers
    window.push_handlers(caret)


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == pyglet.window.key.C:
        # closing the window
        window.close()


# image for icon
img = image = pyglet.resource.image("logo.png")

# setting image as icon
window.set_icon(img)

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
text = "Welcome to GeeksforGeeks"

# batch object
batch = pyglet.graphics.Batch()

# creating document
document = pyglet.text.document.FormattedDocument(text)

# setting style to the document
document.set_style(0, len(document.text), dict(font_name='Arial', font_size=16, color=(255, 255, 255, 255)))

# creating a incremental text layout
layout = pyglet.text.layout.IncrementalTextLayout(document, 400, 50, batch=batch)

# creating a caret
caret = pyglet.text.caret.Caret(layout, color=(255, 255, 255))

# caret to winow push handlers
window.push_handlers(caret)

caret.move_to_point(100, 100)


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

# deleting caret object
caret.delete()

# start running the application
pyglet.app.run()


