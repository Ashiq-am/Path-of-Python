from playsound import playsound
import time

# Path to the sound file
sound_file = 't-rex-roar.mp3'

# Number of times to play the sound
num_loops = 3

for _ in range(num_loops):
    playsound(sound_file)
    time.sleep(1)  # Pause between plays
