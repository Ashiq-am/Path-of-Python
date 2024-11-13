# initializing dictionary
test_dict = {"Gfg": 3, "is": 5, "for": 8,
			"Geeks": 10, "Best": 16}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
sub_list = [5, 4, 10, 20, 16]

# dictionary comprehension to compile logic in one dictionary
# in operator used to check value existance
res = {key: val for key, val in test_dict.items() if val in sub_list}

# printing result
print("Extracted items : " + str(res))
