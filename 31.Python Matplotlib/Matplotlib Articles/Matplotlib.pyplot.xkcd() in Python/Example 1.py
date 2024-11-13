import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 0.1)
amplitude = np.sin(time)

with plt.xkcd():
    plt.plot(time, amplitude)
    plt.title('Sine wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude = sin(time)')
    plt.axhline(y=0, color='k')

    plt.show()
