# Import necessary libraries
import matplotlib.pyplot as plt

# Define a function to check if a figure is empty
def is_empty(figure):
	contained_artists = figure.get_children()
	return len(contained_artists) <= 1

# Define data for a bar chart
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Create a Matplotlib figure
fig = plt.figure()

# Generate a bar chart
plt.bar(x, y)

# Check if the plot is empty and print the result
if is_empty(fig):
	print('Plot is Empty')
else:
	print('Plot is not empty')
