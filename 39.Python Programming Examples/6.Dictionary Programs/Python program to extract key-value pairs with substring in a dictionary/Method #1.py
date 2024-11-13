# Python3 code to demonstrate working of
# Dictionaries with Substring values
# Using list comprehension

# initializing lists
test_list = [{"Gfg": "4", "best": "1"},
			{"Gfg": "good for CS", "best": "8"},
			{"Gfg": "good CS content", "best": "10"}]

# printing original list
print("The original list : " + str(test_list))

# initializing K key
K = "Gfg"

# initializing target value
sub_str = "CS"

# list comprehension to extract values with
# substring values using in operator
res = [val for val in test_list if sub_str in val[K]]

# printing result
print("Dictionaries with particular substring values : " + str(res))
