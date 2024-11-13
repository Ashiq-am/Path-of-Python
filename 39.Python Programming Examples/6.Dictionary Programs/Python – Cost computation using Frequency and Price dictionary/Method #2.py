# Python3 code to demonstrate working of
# Cost computation using Frequency and Price dictionary
# Using sum() + list comprehension

# initializing dictionary
test_dict = {"Apple": 5, "Mango": 8, "Grapes": 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing Frequency dict
cost_dict = {"Apple": 3, "Mango": 4, "Grapes": 6}

# using list comprehension and sum() to provide one-liner
res = sum([cost_dict[key] * test_dict[key] for key in test_dict])

# printing result
print("The extracted summation : " + str(res))
