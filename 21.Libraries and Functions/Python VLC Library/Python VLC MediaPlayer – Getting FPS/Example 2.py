# importing vlc module
import vlc

# importing time module
import time

# creating vlc media player object
media_player = vlc.MediaPlayer()

# media resource locator
mrl = "1.mp4"

# setting mrl to the media player
media_player.set_mrl(mrl)

# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)


# getting cursor co-ordinates
value = media_player.video_get_cursor()

# getting fps
value = media_player.get_fps()

# printing fps
print("Frame Rate per Second : ")
print(value)
