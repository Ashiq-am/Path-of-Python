# Define a list of fruits
fruits = ["Apple", "Orange", "Banana"]

# Define a list of corresponding prices for each fruit
prices = [5, 3, 2]

# Initialize an empty list to store dictionaries containing fruit information
fruit_info = []

# Iterate over each fruit in the list of fruits
for i, fruit in enumerate(fruits):
	# Append a dictionary containing the name of the fruit and its corresponding price
	fruit_info.append({"name": fruit, "price": prices[i]})

# Print the list of dictionaries containing fruit information
print(fruit_info)
