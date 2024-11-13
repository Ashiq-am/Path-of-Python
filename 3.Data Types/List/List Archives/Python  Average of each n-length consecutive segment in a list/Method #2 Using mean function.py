# Python code to find average of each consecutive segment

# Importing
from statistics import mean
from itertools import islice

# List initialisation
Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
		12, 13, 14, 15, 16, 17, 18, 19, 20]

# Finding average of each consecutive segment
zip_list = zip(*(islice(Input, i, None) for i in range(5)))
Output = list(map(mean, zip_list))

# printing output
print(Output)
