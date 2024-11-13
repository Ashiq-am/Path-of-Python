# Pythom code to demonstrate the
# difference between pvariance()
# and variance()

# importing statistocs module
import statistics

# Population tree and extract
# a sample from it
tree = (1.1, 1.22, .23, .55, .67, 2.33, 2.81,
        1.54, 1.2, 0.2, 0.1, 1.22, 1.61)

# Sample extract from population tree
sample = (1.22, .23, .55, .67, 2.33,
          2.81, 1.54, 1.2, 0.2)

# Print sample variance and as
# well as population variance
print("Variance of whole popuation is %s"
      % (statistics.pvariance(tree)))

print("Variance of sample from population is %s "
      % (statistics.variance(sample)))

# Print the difference in both population
# variance and sample variance
print("\n")

print("Difference in Population variance"
      "and Sample variance is % s"
      % (abs(statistics.pvariance(tree)
             - statistics.variance(sample))))
