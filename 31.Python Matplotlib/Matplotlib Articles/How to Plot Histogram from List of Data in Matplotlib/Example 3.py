# import necessary packages
import matplotlib.pyplot as plt

# list of weights
weights = [30, 50, 45, 80, 76, 55,
		45, 47, 50, 65]

# list of bins
bins = [30, 40, 50, 60]

# plotting labelled histogram
plt.hist(weights, bins=bins, edgecolor='black')
plt.xlabel('weight')
plt.ylabel('Person count')
plt.show()
