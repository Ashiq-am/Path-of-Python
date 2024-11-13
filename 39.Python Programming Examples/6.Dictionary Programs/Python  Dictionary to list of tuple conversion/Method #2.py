# Python3 code to demonstrate
# Dictionary to list of tuple conversion
# using list comprehension + items() + "+" operator

# initializing Dictionary
test_dict = {"Nikhil" : (22, "JIIT"), "Akshat" : (21, "JIIT")}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# using list comprehension + items() + "+" operator
# Dictionary to list of tuple conversion
res = [(key, ) + val for key, val in test_dict.items()]

# print result
print("The list after conversion : " + str(res))
