import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
x = [20, 70, 105, 220, 385, 590, 859]
y = [10, 20, 30, 40, 50, 60, 70]
fig, ax = plt.subplots(1, 1)
ax.plot(x, y)
space = 80
ax.xaxis.set_major_locator(ticker.MultipleLocator(space))
plt.show()
