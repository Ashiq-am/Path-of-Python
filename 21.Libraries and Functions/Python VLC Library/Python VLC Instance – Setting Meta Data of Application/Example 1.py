# importing vlc module
import vlc

# importing time module
import time

# creating Instance class object
player = vlc.Instance()

# setting application meta data
player.set_app_id("vlc.GFG", "1.2", "GFG")

# creating a new media list
media_list = player.media_list_new()

# creating a media player object
media_player = player.media_list_player_new()

# creating a new media
media = player.media_new("death_note.mkv")

# adding media to media list
media_list.add_media(media)

# setting media list to the mediaplayer
media_player.set_media_list(media_list)


# start playing video
media_player.play()


# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)
