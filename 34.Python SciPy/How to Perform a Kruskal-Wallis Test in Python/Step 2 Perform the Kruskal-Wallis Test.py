# Import libraries
from scipy import stats

# Defining data groups
data_group1 = [7, 9, 12, 15, 21]
data_group2 = [5, 8, 14, 13, 25]
data_group3 = [6, 8, 8, 9, 5]

# Conduct the Kruskal-Wallis Test
result = stats.kruskal(data_group1, data_group2, data_group3)

# Print the result
print(result)
