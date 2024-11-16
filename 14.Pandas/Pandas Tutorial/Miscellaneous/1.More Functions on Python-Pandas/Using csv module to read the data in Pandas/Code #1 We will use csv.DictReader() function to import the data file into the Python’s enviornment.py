# importing the csv module
import csv

# Now let's read the file named 'auto-mpg.csv'
# After reading as a dictionary convert
# it to Python's list
with open('auto-mpg.csv') as csvfile:
	mpg_data = list(csv.DictReader(csvfile))

# Let's visualize the data
# We are printing only first three elements
print(mpg_data[:3])
