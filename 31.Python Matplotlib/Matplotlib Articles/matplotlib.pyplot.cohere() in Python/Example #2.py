# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))
nse2 = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode ='same')*dt
cnse2 = np.convolve(nse2, r, mode ='same')*dt

s1 = 1.5 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = np.cos(np.pi * t) + cnse2 + np.sin(2 * np.pi * 10 * t)

fig, [ax1, ax2] = plt.subplots(2, 1)
ax1.set_title('matplotlib.pyplot.cohere() Example\n',
					fontsize = 14, fontweight ='bold')

ax1.plot(t, s1, t, s2)
ax1.set_xlim(0, 5)
ax1.set_xlabel('time')
ax1.set_ylabel('s1 and s2')
ax1.grid(True)

ax2.cohere(s1, s2, 256, 1./dt)
ax2.set_ylabel('coherence')
plt.show()
