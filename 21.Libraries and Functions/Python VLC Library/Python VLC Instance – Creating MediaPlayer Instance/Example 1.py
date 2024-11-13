# importing vlc module
import vlc

# importing time module
import time

# creating Instance class object
player = vlc.Instance()

# creating a new media
media = player.media_new("death_note.mkv")

# creating a media player object
media_player = player.media_player_new()

media_player.set_media(media)

# setting video scale
media_player.video_set_scale(0.6)

# start playing video
media_player.play()


# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)
