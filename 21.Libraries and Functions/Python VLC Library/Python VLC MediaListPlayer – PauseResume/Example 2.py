# importing vlc module
import vlc

# importing time module
import time

# creating a media player object
media_player = vlc.MediaListPlayer()

# creating Instance class object
player = vlc.Instance()

# creating a new media list
media_list = player.media_list_new()

# creating a new media
media = player.media_new("1.mp4")

# adding media to media list
media_list.add_media(media)

# setting media list to the media player
media_player.set_media_list(media_list)


# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# pausing media
media_player.set_pause(1)

# wait for 4 second
# so that it remained paused for 4 seconds
time.sleep(4)
