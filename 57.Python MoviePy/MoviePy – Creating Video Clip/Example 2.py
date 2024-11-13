# importing matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# importing movie py libraries
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# numpy array
x = np.linspace(-4, 4, 100)

# matplot subplot
fig, ax = plt.subplots()

duration = 2


# method to get frames
def make_frame(t):
    # clear
    ax.clear()

    # plotting line
    ax.plot(x, np.cos(x + 4 * np.pi / duration * t), lw=3)
    ax.set_ylim(-1.5, 2.5)

    # returning mumpy image
    return mplfig_to_npimage(fig)


# creating Video Clip
clip = VideoClip(make_frame, duration=3)

# displaying clip
clip.ipython_display(fps=20, loop=True, autoplay=True)
