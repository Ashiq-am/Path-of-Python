# Python3 code to demonstrate working of
# Even values update in dictionary
# Using update() + dictionary comprehension

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using update() + dictionary comprehension
# Even values update in dictionary
test_dict.update((x, y * 3) for x, y in test_dict.items() if y % 2 == 0)

# printing result
print("The dictionary after triple even key's value : " + str(test_dict))
