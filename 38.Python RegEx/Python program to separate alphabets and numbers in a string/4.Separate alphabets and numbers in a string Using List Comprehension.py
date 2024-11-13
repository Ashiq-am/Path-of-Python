# Take input string from the user
string = "abcd11gdf15hnnn678hh4"

# Use list comprehension to separate alphabets and numbers
alphabets_list = [char for char in string if char.isalpha()]
numbers_list = [char for char in string if char.isdigit()]

# Join the lists with a space separator
alphabets = ' '.join(alphabets_list)
numbers = ' '.join(numbers_list)

# Print the result
print("Alphabets and numbers in the string are:", alphabets, numbers)
