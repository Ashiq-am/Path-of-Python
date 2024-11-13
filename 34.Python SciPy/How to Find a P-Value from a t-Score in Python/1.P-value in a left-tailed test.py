# Python program to find the p-value
# in a left-tailed test

# Importing the library
import scipy.stats

# Determine the p-value
scipy.stats.t.sf(abs(-.47), df=12)
