# Python program to get average of a list
# Using mean()

# importing mean()
from statistics import mean

def Average(lst):
	return mean(lst)

# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

# Printing average of the list
print("Average of the list =", round(average, 2))
