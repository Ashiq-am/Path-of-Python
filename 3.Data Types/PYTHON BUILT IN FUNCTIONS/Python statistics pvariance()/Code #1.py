# Pythom code to demonstrate the
# use of pvariance()

# importing statistics module
import statistics

# creating a random population list
population = (1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.9, 2.2,
			2.3, 2.4, 2.6, 2.9, 3.0, 3.4, 3.3, 3.2)


# Prints the population variance
print("Population variance is %s"
	%(statistics.pvariance(population)))
