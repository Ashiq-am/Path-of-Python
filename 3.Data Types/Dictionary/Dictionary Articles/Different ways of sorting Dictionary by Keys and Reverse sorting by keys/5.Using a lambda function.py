# Initialising a dictionary
my_dict = {'a': 23, 'g': 67, 'e': 12, 45: 90}

# Sorting dictionary using lambda function
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# Printing sorted dictionary
print("Sorted dictionary using lambda is : ", sorted_dict)
