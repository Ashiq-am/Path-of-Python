# import the necessary python packages
import numpy as np
import matplotlib.pyplot as plt

# odr function from scipy package
# is used to perform ODR regression
from scipy import odr
import random as r

# Create a sample feature array and a target array
feature = np.array(np.arange(1, 11))
# shuffle the created array
np.random.shuffle(feature)
# create a target array of random numbers
target = np.array([0.65, -.75, 0.90, -0.5, 0.14,
				0.84, 0.99, -0.95, 0.41, -0.28])

# Define a function (quadratic in our case)
# to fit the data with.
# odr initially assumes a linear function
def target_function(p, x):
	m, c = p
	return m*x + c

# model fitting.
odr_model = odr.Model(target_function)

# Create a Data object using sample data created.
data = odr.Data(feature, target)

# Set ODR with the model and data.
ordinal_distance_reg = odr.ODR(data, odr_model,
							beta0=[0.2, 1.])

# Run the regression.
out = ordinal_distance_reg.run()

# print the results
out.pprint()
