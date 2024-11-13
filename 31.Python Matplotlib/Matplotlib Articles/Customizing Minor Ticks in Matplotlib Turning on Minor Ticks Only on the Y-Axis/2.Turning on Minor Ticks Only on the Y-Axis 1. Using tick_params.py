import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5])
plt.gca().tick_params(axis='x', which='minor', bottom=False)
plt.minorticks_on()
plt.show()
