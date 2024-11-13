# import necessary packages
import matplotlib.pyplot as plt

# list of weights
weights = [30, 50, 45, 80, 76, 55,
		45, 47, 50, 65]

# plotting labelled histogram
plt.hist(weights, bins=5, edgecolor='black')
plt.xlabel('weight')
plt.ylabel('Person count')
plt.show()
