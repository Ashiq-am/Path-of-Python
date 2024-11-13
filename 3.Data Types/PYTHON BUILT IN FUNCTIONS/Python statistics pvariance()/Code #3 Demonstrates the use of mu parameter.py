# Python code to demonstrate the use
# of 'mu' parameter on pvariance()

# importing statistics module
import statistics

# Apparently, the Python interpreter doesn't
# even check whether the value entered for mu
# is the actual mean of data-set or not.
# Thus providing incorrect value would
# lead to impossible answers

# Creating a population tree of the
# age of kids in a locality
tree = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
		12, 12, 12, 12, 13, 1, 2, 12, 2, 2,
			2, 3, 4, 5, 5, 5, 5, 6, 6, 6)

# Finding the mean of population tree
m = statistics.mean(tree)

# Using the mu parameter
# while using pvariance()
print("Population Variance is % s"
	%(statistics.pvariance(tree, mu = m)))
