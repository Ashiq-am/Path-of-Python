# Python 3 code to demonstrate
# working of pop()

# initializing dictionary
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair.
pop_first = test_dict.pop("Nikhil")

# Printing the value associated to popped key
print("Value associated to poppped key is : " + str(pop_first))

# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))
