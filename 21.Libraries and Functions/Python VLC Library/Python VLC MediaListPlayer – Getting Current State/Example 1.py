# importing vlc module
import vlc

# importing time module
import time

# creating a media player object
media_player = vlc.MediaListPlayer()

# creating Instance class object
player = vlc.Instance()

# creating a new media list object
media_list = player.media_list_new()

# creating a new media
media = player.media_new("death_note.mkv")

# adding media to media list
media_list.add_media(media)

# setting media list to the media player
media_player.set_media_list(media_list)


# start playing video
media_player.play()


# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# getting media player current state
value = media_player.get_state()

# printing value
print(value)
