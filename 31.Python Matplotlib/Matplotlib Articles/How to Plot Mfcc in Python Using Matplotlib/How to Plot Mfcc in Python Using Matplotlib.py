import librosa
import librosa.display
import matplotlib.pyplot as plt

def plot_mfcc(audio_path):
	# Load the audio file
	y, sr = librosa.load(audio_path)

	# Extract MFCC features
	mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

	# Plot MFCCs
	plt.figure(figsize=(10, 4))
	librosa.display.specshow(mfccs, x_axis='time', cmap='viridis')
	plt.colorbar(format='%+2.0f dB')
	plt.title('MFCC')
	plt.xlabel('Time')
	plt.ylabel('MFCC Coefficient')
	plt.show()

# Example usage
audio_file_path = "path/to/your/audio/file.wav"
plot_mfcc(audio_file_path)
