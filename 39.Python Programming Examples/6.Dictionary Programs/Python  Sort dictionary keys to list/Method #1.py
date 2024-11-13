# Python3 code to demonstrate working of
# Sort dictionary keys to list
# Using sum() + sorted() + items() + lambda

# initializing dictionary
test_dict = {'Geeks' : 2, 'for' : 1, 'CS' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using sum() + sorted() + items() + lambda
# Sort dictionary keys to list
res = list(sum(sorted(test_dict.items(), key = lambda x:x[1]), ()))

# printing result
print("List after conversion from dictionary : " + str(res))
