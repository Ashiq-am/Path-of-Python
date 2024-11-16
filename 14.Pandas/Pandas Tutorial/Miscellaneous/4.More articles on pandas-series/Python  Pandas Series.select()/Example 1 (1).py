# Define a function to Select those cities whose index
# label's last character is an even integer
def city_even(city):
	# if last character is even
	if int(city[-1]) % 2 == 0:
		return True
	else:
		return False

# Call the function and select the values
selected_cities = sr.select(city_even, axis = 0)

# Print the returned Series object
print(selected_cities)
