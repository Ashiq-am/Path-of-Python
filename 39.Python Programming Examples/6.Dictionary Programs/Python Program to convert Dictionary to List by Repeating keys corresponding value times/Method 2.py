# initializing dictionary
test_dict = {'g': 2, 'f': 3, 'g': 1, 'b': 4, 'e': 1, 's': 4, 't': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# nested list comprehension to solve problem
res = [key for key, val in test_dict.items() for _ in range(val)]

# printing result
print("The constructed list : " + str(res))
