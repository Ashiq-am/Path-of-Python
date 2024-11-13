import moviepy.editor as me

# Grabbing file
vid= me.VideoFileClip("Video_1.mp4")

print(str(vid.duration))
