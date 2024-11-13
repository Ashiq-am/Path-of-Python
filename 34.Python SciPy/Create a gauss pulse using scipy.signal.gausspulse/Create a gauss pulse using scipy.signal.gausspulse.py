from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1, 1, 200)

i, q, e = signal.gausspulse(t, fc=3, retquad=True, retenv=True)

plt.plot(i, color='green')
plt.plot(q, color='black')
plt.plot(e, '--', color='red')

plt.title('Gauss pulse for a 3 Hz - Geeksforgeeks')
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.legend(['Inphase', 'Quadrature', 'Envelope'])

plt.show()
