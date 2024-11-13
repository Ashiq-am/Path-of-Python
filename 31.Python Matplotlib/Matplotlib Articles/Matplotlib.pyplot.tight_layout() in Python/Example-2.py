import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter

prng = np.random.RandomState(19680801)

xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size = 100)) * np.log10(xs)**2

plt.xscale('log')

formatter0 = EngFormatter(unit ='Hz')
plt.plot(xs, ys)
plt.xlabel('Frequency')

plt.title('matplotlib.pyplot.tight_layout() Example')
plt.tight_layout()
plt.show()
