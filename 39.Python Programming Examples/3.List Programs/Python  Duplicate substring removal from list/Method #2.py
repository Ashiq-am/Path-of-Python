# Python3 code to demonstrate
# removing duplicate substrings
# using {} + split() + list comprehension

# initializing list
test_list = [ 'aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']

# printing original list
print("The original list : " + str(test_list))

# using {} + split() + list comprehension
# removing duplicate substrings
res = list({i for sub in test_list for i in sub.split('-')})

# print result
print("The list after duplicate removal : " + str(res))
