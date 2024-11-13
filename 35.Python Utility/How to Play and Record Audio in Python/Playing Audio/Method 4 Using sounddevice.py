# Import libraries
import sounddevice as sd
import soundfile as sf

# Extract data and sampling rate from file
array, smp_rt = sf.read(path_of_file, dtype = 'float32')

# start the playback
sd.play(array, smp_rt)

# Wait until file is done playing
status = sd.wait()

# stop the sound
sd.stop()
