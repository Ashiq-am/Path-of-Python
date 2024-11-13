# importing vlc module
import vlc

# importing time module
import time

# creating vlc media player object
media_player = vlc.MediaPlayer()

# getting instance of the media player
inst = media_player.get_instance()
print("Media player Instance : " + str(inst))
