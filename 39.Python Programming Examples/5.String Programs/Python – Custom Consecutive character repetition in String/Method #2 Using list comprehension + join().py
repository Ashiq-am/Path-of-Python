# Python3 code to demonstrate working of
# Custom Consecutive character repetition in String
# Using list comprehension + join()

# initializing string
test_str = 'Geeks4Geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing dictionary
test_dict = {"G" : 3, "e" : 2, "4" : 4, "k" : 5, "s" : 3}

# using join to perform concatenation of strings
res = "".join([ele * test_dict[ele] for ele in test_str])

# printing result
print("The filtered string : " + str(res))
