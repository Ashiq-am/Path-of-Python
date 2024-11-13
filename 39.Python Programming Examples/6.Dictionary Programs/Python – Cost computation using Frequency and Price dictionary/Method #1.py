# Python3 code to demonstrate working of
# Cost computation using Frequency and Price dictionary
# Using loop

# initializing dictionary
test_dict = {"Apple": 5, "Mango": 8, "Grapes": 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing Frequency dict
cost_dict = {"Apple": 3, "Mango": 4, "Grapes": 6}

res = 0
for key in test_dict:
    # computing summation of product
    res = res + (test_dict[key] * cost_dict[key])

# printing result
print("The extracted summation : " + str(res))
