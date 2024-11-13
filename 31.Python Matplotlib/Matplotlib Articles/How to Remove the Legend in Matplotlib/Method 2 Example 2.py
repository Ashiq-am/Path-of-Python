import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,1000)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2,1)

axs[0].plot(x,y1,c='r',label = 'Sine')
axs[1].plot(x,y2,c='g',label = 'Cosine')

axs[0].legend(loc='upper left')
axs[1].legend(loc='upper left')

axs[1].get_legend().set_visible(False)


plt.show()
