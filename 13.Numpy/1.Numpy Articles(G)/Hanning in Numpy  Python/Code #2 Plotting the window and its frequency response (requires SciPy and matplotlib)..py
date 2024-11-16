import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift

window = np.hanning(51)

plt.plot(window)
plt.title("Hann window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.show()
