import numpy as np

# Assuming 'data.csv' contains numeric data
data = np.loadtxt('data.csv', delimiter=',')
print("Data loaded from CSV:\n", data)