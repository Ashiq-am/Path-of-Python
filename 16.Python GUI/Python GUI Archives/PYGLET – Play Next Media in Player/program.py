# importing pyglet module
import pyglet

# width of window
width = 800

# height of window
height = 500

# caption i.e title of the window
title = "Geeksforgeeks"

# creating a window
window = pyglet.window.Window(width, height, title)

# video path
vidPath = "gfg.mp4"

# creating a media player object
player = pyglet.media.Player()

# creating a source object
source = pyglet.media.StreamingSource()

# load the media from the source
MediaLoad = pyglet.media.load(vidPath)

# add this media in the queue
player.queue(MediaLoad)

# loading a new media
media = pyglet.media.load("media.mp4")

# add this media in the queue
player.queue(media)

# play the video
player.play()


# on draw event
@window.event
def on_draw():
    # clea the window
    window.clear()

    # if player sorce exist
    # and video format exist
    if player.source and player.source.video_format:
        # get the texture of video and
        # make surface to display on the screen
        player.get_texture().blit(0, 0)


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "p" get press
    if symbol == pyglet.window.key.P:
        # pause the video
        player.pause()

        # printing message
        print("Video is paused")

    # key "r" get press
    if symbol == pyglet.window.key.R:
        # resume the video
        player.play()

        # printing message
        print("Video is resumed")


# play the next source
player.next_source()

# run the pyglet application
pyglet.app.run()
