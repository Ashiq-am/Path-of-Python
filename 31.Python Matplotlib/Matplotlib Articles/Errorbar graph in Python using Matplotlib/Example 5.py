# import require modules
import numpy as np
import matplotlib.pyplot as plt


# defining our function
x = np.arange(10)/10
y = (x + 0.1)**2

# defing our error
y_error = np.linspace(0.05, 0.2, 10)

# ploting our function and
# error bar
plt.plot(x, y)

plt.errorbar(x, y, yerr = y_error, fmt ='o')
