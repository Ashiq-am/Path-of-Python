import matplotlib.pyplot as plt
import numpy as np


a = np.linspace(0,2*3.14,50)
b = np.sin(a)

plt.fill_between(a, b, 0,
				where = (a > 2) & (a <= 3),
				color = 'g')
plt.plot(a,b)
