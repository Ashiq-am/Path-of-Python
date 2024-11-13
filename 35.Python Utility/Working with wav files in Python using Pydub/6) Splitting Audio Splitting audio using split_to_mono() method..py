# import required libraries
from pydub import AudioSegment
from pydub.playback import play

# importing audio file
a = AudioSegment.from_file("pzm12.wav")

# Split stereo to mono
b = a.split_to_mono()
print(b)
print(b[0].channels )


b[0].export(out_f="outNow.wav",format="wav")
