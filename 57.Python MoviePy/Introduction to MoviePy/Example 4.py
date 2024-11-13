import moviepy.editor

'''
Grabbing The video's from storage
syntax:
variable_holding_video_name= moviepy.editor.VideoFileCLip("{{Filename}}.{{extension}}")

'''
clip_1= moviepy.editor.VideoFileClip("Video_1.mp4")
clip_2= moviepy.editor.VideoFileClip("Video_2.mp4")

'''
TO join the video's i.e. concatenate the videos'
use function concatenate_videoclips(list_of_clips_to_mearged)
syntax:
variable_to_hold_mearged_video= moviepy.editor.concatenate_videclips([video_1,Video_2,. . .])
'''
Mearged_video=moviepy.editor.concatenate_videoclips([clip_1,clip_2])

# Saving File as output.mp4 in same folder
# libx264 is encoding lib for creating video stream(H.264)
Mearged_video.write_videofile("Output.mp4",codec='libx264')

print("Done")
