# Python 3 code to demonstrate
# working of pop() without key

# initializing dictionary
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair
# provided default
pop_ele = test_dict.pop('Manjeet', 4)

# Printing the value associated to popped key
# Prints 4
print("Value associated to poppped key is : " + str(pop_ele))

# using pop to return and remove key-value pair
# not provided default
pop_ele = test_dict.pop('Manjeet')

# Printing the value associated to popped key
# KeyError
print("Value associated to poppped key is : " + str(pop_ele))
