import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5])
plt.gca().tick_params(axis='y', which='minor', color='r', width=2, length=5)
plt.minorticks_on()
plt.show()
