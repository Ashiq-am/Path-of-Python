# Python3 code to demonstrate working of
# Convert Dictionaries List to Order Key Nested dictionaries
# Using loop + enumerate()

# initializing lists
test_list = [{"Gfg": 3, 4: 9}, {"is": 8, "Good": 2}, {"Best": 10, "CS": 1}]

# printing original list
print("The original list : " + str(test_list))

# using enumerate() to extract key to map with dict values
res = dict()
for idx, val in enumerate(test_list):
    res[idx] = val

# printing result
print("The constructed dictionary : " + str(res))
