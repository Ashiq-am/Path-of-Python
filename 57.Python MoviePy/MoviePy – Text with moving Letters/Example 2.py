# importing Numpy
import numpy as np

# importing moviepy module
from moviepy.editor import *

from moviepy.video.tools.segmenting import findObjects

# screen size
screensize = (1080, 720)

# creating a text clip of color red, font is Arial and size is 80
txtClip = TextClip('GeeksforGeeks', color='red', font="Arial",
                   kerning=5, fontsize=80)

# creating a composite video of given size
cvc = CompositeVideoClip([txtClip.set_pos('center')],
                         size=screensize)

# helper function
rotMatrix = lambda a: np.array([[np.cos(a), np.sin(a)],
                                [-np.sin(a), np.cos(a)]])


# method for effect 3
def effect3(screenpos, i, nletters):
    v = np.array([-1, 0])

    d = lambda t: max(0, 3 - 3 * t)

    # retruning the function
    return lambda t: screenpos - 400 * v * d(t - 0.2 * i)


# method for effect 4
def effect4(screenpos, i, nletters):
    # damping
    d = lambda t: max(0, t)

    # angle of the movement
    a = i * np.pi / nletters

    v = rotMatrix(a).dot([-1, 0])

    if i % 2: v[1] = -v[1]

    # returing the function
    return lambda t: screenpos + 400 * d(t - 0.1 * i) * rotMatrix(-0.2 * d(t) * a).dot(v)


# a list of ImageClips
letters = findObjects(cvc)


# method to move letters
def moveLetters(letters, funcpos):
    return [letter.set_pos(funcpos(letter.screenpos, i, len(letters)))
            for i, letter in enumerate(letters)]


# adding clips with specific effect
clips = [CompositeVideoClip(moveLetters(letters, funcpos),
                            size=screensize).subclip(0, 5)
         for funcpos in [effect3, effect4]]

# comping all the clips
final_clip = concatenate_videoclips(clips)

# setting fps of the final clip
final_clip.fps = 24

# showing video clip
final_clip.ipython_display()
