from scipy import signal
import matplotlib.pyplot as plot
import numpy as np
# %matplotlib inline

# Plot the square wave
t = np.linspace(0, 1, 1000, endpoint=True)
plot.plot(t, signal.square(2 * np.pi * 5 * t))

# Change the x, y axis label to "Brush Script MT" font style.
plot.xlabel("Time (Seconds)", fontname="Brush Script MT", fontsize=18)
plot.ylabel("Amplitude", fontname="Brush Script MT", fontsize=18)

plot.show()
