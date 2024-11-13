# Python3 code to demonstrate working of
# Convert Dictionary Value list to Dictionary List
# Using list comprehension + zip()

# initializing list
test_list = [{'Gfg' : [5, 6, 5]}, {'is' : [10, 2, 3]}, {'best' : [4, 3, 1]}]

# printing original list
print("The original list is : " + str(test_list))

# Convert Dictionary Value list to Dictionary List
# Using list comprehension + zip()
keys = [list(sub.keys())[0] for sub in test_list]
vals = zip(*[val for sub in test_list for val in sub.values()])
res = [dict(zip(keys, val)) for val in vals]

# printing result
print("Records after conversion : " + str(res))
