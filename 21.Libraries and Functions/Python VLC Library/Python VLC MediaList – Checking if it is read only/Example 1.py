# importing vlc module
import vlc

# importing time module
import time

# creating a media player object
media_player = vlc.MediaListPlayer()

# creating Instance class object
player = vlc.Instance()

# creating a media list object
media_list = vlc.MediaList()

# creating a new media
media1 = player.media_new("death_note.mkv")

# adding media to media list
media_list.add_media(media1)

# creating a new media
media2 = player.media_new("1.mp4")

# adding another media
media_list.add_media(media2)


# setting media list to the media player
media_player.set_media_list(media_list)


# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# checking if the media list is read only
value = media_list.is_readonly()

# printing value
print(value)
