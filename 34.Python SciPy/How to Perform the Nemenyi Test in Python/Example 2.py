# Importing library
from scipy import stats

# Data groups
data_group1 = [44, 56, 53, 46, 53,
			46, 42, 47, 46, 45]
data_group2 = [35, 46, 38, 47, 37,
			38, 44, 46, 44, 35]
data_group3 = [32, 42, 54, 43, 32,
			32, 43, 36, 8, 29]

# Conduct the Friedman Test
stats.friedmanchisquare(data_group1, data_group2, data_group3)
