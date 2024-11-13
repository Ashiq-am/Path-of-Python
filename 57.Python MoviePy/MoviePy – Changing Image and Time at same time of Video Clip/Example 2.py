# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting duration of the video
duration = clip.duration

def scroll(get_frame, t):
	"""
	This function returns a 'region' of the current frame.
	The position of this region depends on the time.
	"""
	frame = get_frame(t)
	frame_region = frame[int(t):int(t)+360, :]
	return frame_region

# alter time and frame
final = clip.fl( scroll )

# showing final clip
final.ipython_display()
