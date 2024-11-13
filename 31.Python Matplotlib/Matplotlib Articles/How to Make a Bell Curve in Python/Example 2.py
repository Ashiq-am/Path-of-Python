# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# A custom function to calculate
# probability distribution function
def pdf(x):
	mean = np.mean(x)
	std = np.std(x)
	y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
	return y_out

# To generate an array of x-values
x = np.arange(-2, 2, 0.1)

# To generate an array of
# y-values using corresponding x-values
y = pdf(x)

# To fill in values under the bell-curve
x_fill = np.arange(-2, 2, 0.1)
y_fill = pdf(x_fill)

# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6))
plt.plot(x, y, color = 'black',
		linestyle = 'dashed')

plt.scatter(x, y, marker = 'o',
			s = 25, color = 'red')

plt.fill_between(x_fill, y_fill, 0,
				alpha = 0.2, color = 'blue')
plt.show()
