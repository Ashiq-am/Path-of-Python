# Python3 code to demonstrate working of
# Sort dictionary by Tuple Key Product
# Using dictionary comprehension + sorted() + lambda

# initializing dictionary
test_dict = {(5, 6) : 3, (2, 3) : 9, (8, 4): 10, (6, 4): 12}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# sorted() over lambda computed product
# dictionary comprehension reassigs dictionary by order
res = {key: test_dict[key] for key in sorted(test_dict.keys(), key = lambda ele: ele[1] * ele[0])}

# printing result
print("The sorted dictionary : " + str(res))
