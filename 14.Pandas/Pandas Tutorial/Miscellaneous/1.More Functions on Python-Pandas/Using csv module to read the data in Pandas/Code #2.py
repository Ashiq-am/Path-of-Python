# Let's find all the keys in the dictionary
print(mpg_data[0].keys)

# Now we would like to find out the number of
# unique values of cylinders in the car in our dataset
# We create a set containing the cylinders value
unique_cyl = set(data['cylinders'] for data in mpg_data)

# Let's print the values
print(unique_cyl)
