# importing vlc module
import vlc
import time

# creating vlc media player object
media_player = vlc.MediaPlayer("1.mp4")

# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)
