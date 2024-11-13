# Python3 code to demonstrate
# Segregating by Suffix
# Using filter() + endwith() + lambda

# initializing list
test_list = ['apple', 'oranges', 'mango', 'grapes']

# initializing end Suffix
end_letter = 's'

# printing original list
print("The original list : " + str(test_list))

# using filter() + endwith() + lambda
# Segregating by Suffix
with_s = list(filter(lambda x: x.endswith(end_letter), test_list))
without_s = list(filter(lambda x: not x.endswith(end_letter), test_list))

# print result
print("The list without suffix s : " + str(without_s))
print("The list with suffix s : " + str(with_s))
