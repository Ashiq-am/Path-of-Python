import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift

window = np.blackman(51)

plt.plot(window)
plt.title("Blackman window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()
