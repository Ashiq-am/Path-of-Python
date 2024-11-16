import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y_multi = np.array([[0, 0.8, 0.9, 0.1, -0.8, -1.0], [0, 0.7, 0.85, 0.05, -0.75, -0.95]])

# Perform linear fit on each dataset separately
coefficients_multi = [np.polyfit(x, y, 1) for y in y_multi]
print("Linear Fit Coefficients for Multiple Datasets:", coefficients_multi)

xp = np.linspace(-1, 6, 100)
plt.scatter(x, y_multi[0], label='Dataset 1')
plt.scatter(x, y_multi[1], label='Dataset 2')
for coeff in coefficients_multi:
    p = np.poly1d(coeff)
    plt.plot(xp, p(xp), label=f'Fit: {coeff}')
plt.legend()
plt.show()
