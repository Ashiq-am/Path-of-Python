# Python program to sort dictionary
# by value using itemgetter() function

# Importing OrderedDict
import operator

# Initialize a dictionary
my_dict = {'a': 23,
		'g': 67,
		'e': 12,
		45: 90}

# Sorting dictionary
sorted_dict = sorted(my_dict.items(), key = operator.itemgetter(1))

# Printing sorted dictionary
print("Sorted dictionary is :")
print(sorted_dict)
