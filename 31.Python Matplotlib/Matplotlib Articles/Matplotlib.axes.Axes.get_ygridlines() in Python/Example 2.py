# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

fs = 1000
t = np.linspace(0, 0.3, 301)
A = np.array([2, 8]).reshape(-1, 1)
f = np.array([150, 140]).reshape(-1, 1)
xn = (A * np.sin(2 * np.pi * f * t)).sum(axis=0)
xn += 5 * np.random.randn(*t.shape)

fig, ax = plt.subplots()

yticks = [-40, -15, 10]

ax.psd(xn, NFFT=301, Fs=fs,
       window=mlab.window_none,
       pad_to=1024,
       scale_by_freq=True)

ax.set_yticks(yticks)
ax.set_yticklabels(("Low-1", "High", "Low-2"))
ax.grid(True)

w = ax.get_ygridlines()
ax.text(150, 6, "ygridlines values : ",
        fontweight="bold")
xx = 6
for i in w:
    ax.text(150, xx - 3, str(i), fontweight="bold")
    xx -= 3

fig.suptitle('matplotlib.axes.Axes.get_ygridlines()\
function Example\n\n', fontweight="bold")
plt.show()
