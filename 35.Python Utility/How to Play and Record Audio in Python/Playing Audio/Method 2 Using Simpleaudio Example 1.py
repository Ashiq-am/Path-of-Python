# import library
import simpleaudio as sa

# to check all the functions in succession
# to verify the installation
import simpleaudio.functionchecks as fc

fc.run_all()

# Path to file
f_name = 'myfile.wav'

# create WaveObject instances
# directly from WAV files on disk
wave_obj = sa.WaveObject.from_wave_file(f_name)

# Audio playback
play = wave_obj.play()

# To stop after playing the whole audio
play.wait_done()
play.stop()
