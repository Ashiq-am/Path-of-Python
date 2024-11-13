import sounddevice as sd
import numpy as np

smpl_rate = 44100

my_arr = np.random.uniform(-1,1,smpl_rate)
recordd= sd.playrec(my_arr, smpl_rate, channels=2)

sd.wait()
