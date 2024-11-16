import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift

window = np.kaiser(51, 14)

plt.plot(window)
plt.title("Kaiser window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()
