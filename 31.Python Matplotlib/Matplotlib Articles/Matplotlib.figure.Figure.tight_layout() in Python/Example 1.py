import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import EngFormatter


prng = np.random.RandomState(19680801)

xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size = 100)) * np.log10(xs)**2

plt.xscale('log')
fig = plt.figure()

ax = fig.subplots()

formatter0 = EngFormatter(unit ='Hz')
ax.plot(xs, ys)
ax.set_xlabel('Frequency')

fig.tight_layout()

fig.suptitle("""matplotlib.figure.Figure.tight_layout() 
function Example\n\n""", fontweight ="bold")

fig.show()
