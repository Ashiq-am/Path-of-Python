# Python3 code to demonstrate
# Prefix Separation
# Using filter() + startswith() + lambda

# initializing list
test_list = ['sapple', 'orange', 'smango', 'grape']

# initializing start Prefix
start_letter = 's'

# printing original list
print("The original list : " + str(test_list))

# using filter() + startswith() + lambda
# Prefix Separation
with_s = list(filter(lambda x: x.startswith(start_letter), test_list))
without_s = list(filter(lambda x: not x.startswith(start_letter), test_list))

# print result
print("The list without prefix s : " + str(without_s))
print("The list with prefix s : " + str(with_s))
