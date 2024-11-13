import librosa
file_path = "Roa-Haru.mp3"
audio, sampling_rate = librosa.load(file_path)

# display data
print(f"Audio data: {audio.shape}")
print(f"Sampling rate: {sampling_rate} Hz")
