import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots()
x = [1000, 10000, 100000, 1000000]
y = [1, 2, 3, 4]

ax.plot(x, y)

# Apply the EngFormatter to the x-axis
ax.xaxis.set_major_formatter(ticker.EngFormatter(unit=''))

plt.show()
