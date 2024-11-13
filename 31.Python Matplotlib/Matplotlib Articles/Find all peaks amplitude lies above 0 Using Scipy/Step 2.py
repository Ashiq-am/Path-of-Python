import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy import signal

t = np.linspace(0, 1, 500, endpoint=False)
sig = np.sin(2 * np.pi * t)
x= signal.square(2 * np.pi * 30 * t, duty=(sig + 1)/2)
peak, _ = find_peaks(x, height=0)
