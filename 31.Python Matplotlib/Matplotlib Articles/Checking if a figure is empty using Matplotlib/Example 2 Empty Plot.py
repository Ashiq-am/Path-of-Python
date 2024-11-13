import matplotlib.pyplot as plt

# Define a function to check if a figure is empty
def is_empty(figure):
	contained_artists = figure.get_children()
	return len(contained_artists) <= 1

# Create a Matplotlib figure
fig = plt.figure()

# Check if the plot is empty and print the result
if is_empty(fig):
	print('Plot is Empty')
else:
	print('Plot is not empty')
