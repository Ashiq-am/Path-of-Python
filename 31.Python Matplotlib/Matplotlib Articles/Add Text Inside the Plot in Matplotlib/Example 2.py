import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.01)
y = x**2

plt.xlabel("X-axis", fontsize = 15)
plt.ylabel("Y-axis",fontsize = 15)

#Adding text inside a rectangular box by using the keyword 'bbox'
plt.text(-5, 60, 'Parabola $Y = x^2$', fontsize = 22,
		bbox = dict(facecolor = 'red', alpha = 0.5))

plt.plot(x, y, c = 'g')

plt.show()
