# Python3 code to demonstrate
# Dictionary to list of tuple conversion
# using list comprehension + tuple + items()

# initializing Dictionary
test_dict = {"Nikhil" : (22, "JIIT"), "Akshat" : (21, "JIIT")}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# using list comprehension + tuple + items()
# Dictionary to list of tuple conversion
res = [(key, i, j) for key, (i, j) in test_dict.items()]

# print result
print("The list after conversion : " + str(res))
