import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)
y1 = np.power(x,2)
y2 = np.power(x,3)

fig, axs = plt.subplots(2,1)

axs[0].plot(x,y1,c='r',label = '_nolegend_')
axs[1].plot(x,y2,c='g',label = 'x^3')

axs[0].legend(loc='upper left')
axs[1].legend(loc='upper left')


plt.show()
