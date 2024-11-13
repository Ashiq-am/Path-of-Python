# import the torch and torchaudio dataset packages.
import torch
import torchaudio

# access the dataset in torchaudio package using
# datasets followed by dataset name.
# './' makes sure that the dataset is stored
# in a root directory.
# download = True ensures that the
# data gets downloaded
yesno_data = torchaudio.datasets.YESNO('./',
									download=True)

# loading the first 5 data from yesno_data
for i in range(5):
	waveform, sample_rate, labels = yesno_data[i]
	print("Waveform: {}\nSample rate: {}\nLabels: {}".format(
		waveform, sample_rate, labels))
