# importing vlc module
import vlc

# importing time module
import time


# creating vlc media player object
media_player = vlc.MediaPlayer()

# media resource locator
mrl = "death_note.mkv"

# setting mrl to the media player
media_player.set_mrl(mrl)

# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# getting subtitle description
subtitle = media_player.video_get_spu_description()

# printing subtitle description
print("Subtitle Description")
print(subtitle)
