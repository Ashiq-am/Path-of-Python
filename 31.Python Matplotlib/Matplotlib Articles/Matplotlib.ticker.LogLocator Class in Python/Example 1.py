import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, LogLocator

x = [1, 2, 3, 4, 5, 6,
	7, 8, 9, 10, 11, 12]

y = [0.32, 0.30, 0.28, 0.26,
	0.24, 0.22, 0.20, 0.18,
	0.16, 0.14, 0.12, 0.10]

fig = plt.figure()
ax1 = fig.add_subplot(111)

x_major = MultipleLocator(4)
x_minor = MultipleLocator(1)

ax1.xaxis.set_major_locator(x_major)
ax1.xaxis.set_minor_locator(x_minor)
ax1.set_yscale("log")

y_major = LogLocator(base = 10)
y_minor = LogLocator(base = 10, subs =[1.1, 1.2, 1.3])

ax1.yaxis.set_major_locator(y_major)
ax1.yaxis.set_minor_locator(y_minor)

ax1.plot(x, y)

plt.show()
