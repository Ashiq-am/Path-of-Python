# Python3 code to demonstrate working of
# Sort Dictionary by key-value Summation
# Using sorted() + lambda + items()

# initializing dictionary
test_dict = {3: 5, 1: 3, 4: 6, 2: 7, 8: 1}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# sorted() to sort, lambda provides key-value addition
res = sorted(test_dict.items(), key=lambda sub: sub[0] + sub[1])

# converting to dictionary
res = {sub[0]: sub[1] for sub in res}

# printing result
print("The sorted result : " + str(res))
