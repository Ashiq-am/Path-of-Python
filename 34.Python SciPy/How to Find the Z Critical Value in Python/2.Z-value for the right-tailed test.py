# Python program to find the
# z-value in a two-tailed test

# Importing the library
import scipy.stats

# Determine the z-critical value
scipy.stats.norm.ppf(1-.01)
