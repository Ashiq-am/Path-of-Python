import matplotlib.pyplot as plt
import numpy as np
from pylab import *

x = np.linspace(0, (2*np.pi), endpoint = True)

xlim(x.min(), x.max())

xticks([0, np.pi/2, np.pi, (3*np.pi/2), (2*np.pi)],
	[r'$0$', r'$+\pi/2$', r'$+\pi$', r'$3/2\pi$', r'$2\pi$'])

ylim(-1, 0, 1)
yticks([-1, 0, +1],
	[r'$-1$', r'$0$', r'$+1$'])

plt.plot(x, np.sin(x), label = "sin(x)")
plt.plot(x, np.cos(x), label = "cos(x)")

plt.title('Trignometric Functions', fontsize = 22)

plt.xlabel('Angles', fontsize = 18)
plt.ylabel('Values', fontsize = 18)

plt.legend(loc = 'upper center')

plt.rc('legend', fontsize = 16)

#plt.grid()
plt.tight_layout()

plt.show()
