my_dict = {
    'square': lambda x: x * x,
    'cube': lambda x: x * x * x
}

# Using the lambda functions (fixed way to use the dictionary)
number = 5
squared_value = my_dict['square'](number)  # squared_value will be 25
cubed_value = my_dict['cube'](number)    # cubed_value will be 125

print("Squared value:", squared_value)
print("Cubed value:", cubed_value)
