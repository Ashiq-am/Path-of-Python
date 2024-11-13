import numpy as np
import matplotlib.pyplot as plt


time = np.arange(0, 1, 0.1)
amp = np.sin(time)

plt.plot(time, amp)
plt.title("Signal 1")

plt.show()
