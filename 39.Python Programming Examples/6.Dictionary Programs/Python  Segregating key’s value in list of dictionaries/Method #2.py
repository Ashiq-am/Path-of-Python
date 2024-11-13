# Python3 code to demonstrate working of
# Segregating key's value in list of dictionaries
# Using zip() + map() + values()

# Initialize list
test_list = [{'gfg': 1, 'best': 2}, {'gfg': 4, 'best': 5}]

# printing original list
print("The original list : " + str(test_list))

# Using zip() + map() + values()
# Segregating key's value in list of dictionaries
res = list(zip(*map(dict.values, test_list)))

# printing result
print("Segregated values of keys are : " + str(res))
