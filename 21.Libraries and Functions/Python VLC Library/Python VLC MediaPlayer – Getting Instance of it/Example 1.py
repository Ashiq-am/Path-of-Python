# importing time module
import time


# creating vlc media player object
import vlc

media_player = vlc.MediaPlayer("death_note.mkv")

# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# getting instance of the media player
inst = media_player.get_instance()
print("Media player Instance : " + str(inst))
