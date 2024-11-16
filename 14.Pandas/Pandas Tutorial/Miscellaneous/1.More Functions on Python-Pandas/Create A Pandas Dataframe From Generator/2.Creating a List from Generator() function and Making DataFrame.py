# Generator function to create a sequence of numbers
def number_generator(n):
	for i in range(n):
		yield i

# Creating a list from the generator function
number_list = list(number_generator(5))

# Creating a DataFrame from the list
df = pd.DataFrame({'Numbers': number_list})

# Display the DataFrame
print(df)
