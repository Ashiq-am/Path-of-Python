# Python3 code to demonstrate working of
# Type conversion of dictionary items
# Using loop

# Initialize dictionary
test_dict = {'1': ['4', '5'], '4': ['6', '7'], '10': ['8']}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using loop
# Type conversion of dictionary items
res = {}
for key, value in test_dict.items():
    res[int(key)] = [int(item) for item in value]

# printing result
print("Dictionary after type conversion : " + str(res))
