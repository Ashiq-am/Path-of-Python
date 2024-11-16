# Function to select the sales of
# Coca Cola and Sprite
def show_sales(x):
	if x == 'Sprite' or x == 'Coca Cola':
		return True
	else:
		return False

# Call the function and select the values
selected_cities = sr.select(show_sales, axis = 0)

# Print the returned Series object
print(selected_cities)
