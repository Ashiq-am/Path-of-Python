# Input list of boolean elements
input_list = [True, True, False, True, False]

# Printing list
print(list(input_list))

# Converting into negation values
# Mapping them with their input
# index values
output_list = map(operator.not_, input_list)

# Printing output list
print(list(output_list))
