# Importing library
import scipy.stats as stats

# pre holds the mileage before
# applying the different engine oil
pre = [30, 31, 34, 40, 36, 35,
	34, 30, 28, 29]

# post holds the mileage after
# applying the different engine oil
post = [30, 31, 32, 38, 32, 31,
		32, 29, 28, 30]

# Performing the paired sample t-test
stats.ttest_rel(pre, post)
