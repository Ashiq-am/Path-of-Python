# Importing library

from scipy.stats import kurtosis

# Creating a dataset
dataset = [88, 85, 82, 97, 67, 77, 74, 86,
		81, 95, 77, 88, 85, 76, 81]


# Calculate the kurtosis
print(kurtosis(dataset, axis=0, bias=True))
