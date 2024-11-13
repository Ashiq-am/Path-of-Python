# Incorrect usage causing TypeError
result = len()  # Missing argument in len() function call
# Corrected usage
my_list = [1, 2, 3, 4, 5]
result = len(my_list)  # Correct usage with parentheses

# Incorrect usage causing TypeError
function = max  # Assigning function object to variable without calling it
max_value = function[my_list]  # Incorrect attempt to index function object
# Corrected usage
max_value = function(my_list)  # Correct usage by calling the function
