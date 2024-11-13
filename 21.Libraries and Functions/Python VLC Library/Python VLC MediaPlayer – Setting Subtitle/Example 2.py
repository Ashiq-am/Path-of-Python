# importing vlc module
import vlc

# importing time module
import time

# creating vlc media player object
media_player = vlc.MediaPlayer()

# media object
media = vlc.Media("1mp4.mkv")

# setting media to the media player
media_player.set_media(media)


# setting video scale
media_player.video_set_scale(0.6)

# setting subtitle
media_player.video_set_spu(2)


# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# getting subtitle count
value = media_player.video_get_spu_count()

# printing value
print("Subtitle Count: ")
print(value)
