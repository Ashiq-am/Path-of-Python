import matplotlib.pyplot as plt
import matplotlib.ticker


plt.plot([-1.5, 0, 1.5], [1, 3, 2])
ax = plt.gca()

func = lambda x, pos: str(x).rstrip('0').rstrip('.')

ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(0.25))
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(func))

plt.show()
