import sounddevice as sd

sd.default.samplerate = 4400
sd.default.channels = 2

myrecording = sd.rec(int(duration * fs))

# change the data type: pass a new argument in .rec() of dtype
# myrecording = sd.rec(int(duration * fs), dtype='float64')

sd.wait()
