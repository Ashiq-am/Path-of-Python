# Python3 code to demonstrate working of
# Split dictionary by half
# Using items() + len() + list slicing

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2, 'CS' : 10}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using items() + len() + list slicing
# Split dictionary by half
res1 = dict(list(test_dict.items())[len(test_dict)//2:])
res2 = dict(list(test_dict.items())[:len(test_dict)//2])

# printing result
print("The first half of dictionary : " + str(res1))
print("The second half of dictionary : " + str(res2))
