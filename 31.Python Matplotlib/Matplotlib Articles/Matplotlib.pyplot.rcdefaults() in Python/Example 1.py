# implementation of the matplotlib function
import matplotlib.pyplot as plt

plt.subplot(211)
plt.rc('font', weight ='bold')
plt.rc('xtick.major', size = 5, pad = 7)
plt.rc('xtick', labelsize = 15)
plt.plot([1, 2, 3])

plt.text(0.4, 3.5, 'matplotlib.pyplot.rcdefaults() Example')

plt.rcdefaults()
plt.subplot(212)
plt.plot([1, 2, 3])
plt.grid(True)

plt.show()
