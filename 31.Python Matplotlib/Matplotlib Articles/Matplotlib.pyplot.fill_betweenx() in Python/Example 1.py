import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,2*3.14,50)
b = np.sin(a)

plt.fill_betweenx(a, b, 0,
				where = (a > -0.5) & (a <= 1),
				color='g')

plt.plot(a, b)
