import numpy as np
import matplotlib.pyplot as plt


# Signal 1
time = np.arange(0, 1, 0.1)
amp = np.sin(time)

# Signal 2
t = np.arange(5, 10, 0.25)
ampl = np.sin(t)

# Cross-spectral density
plt.csd(amp, ampl)

plt.show()
