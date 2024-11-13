# Python3 code to demonstrate working of
# Remove double quotes from dictionary keys
# Using dictionary comprehension + replace()

# initializing dictionary
test_dict = {'"Geeks"': 3, '"is" for': 5, '"g"eeks': 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# dictionary comprehension to make double quotes free
# dictionary
res = {key.replace('"', ''): val for key, val in test_dict.items()}

# printing result
print("The dictionary after removal of double quotes : " + str(res))
