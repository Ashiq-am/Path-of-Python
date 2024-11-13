# Python3 code to demonstrate working of
# Type conversion of dictionary items
# Using dictionary comprehension

# Initialize dictionary
test_dict = {'1': ['4', '5'], '4': ['6', '7'], '10': ['8']}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using dictionary comprehension
# Type conversion of dictionary items
res = {int(key): [int(i) for i in val]
       for key, val in test_dict.items()}

# printing result
print("Dictionary after type conversion : " + str(res))
