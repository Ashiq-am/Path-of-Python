# Python3 code to demonstrate working of
# Concatenate Ranged Values in String list
# Using list comprehension + string slicing

# initializing list
test_list = ["abGFGcs", "cdforef", "asalloi"]

# printing original list
print("The original list : " + str(test_list))

# initializing range
i, j = 2, 5

# join() used to join slices together
res = ''.join([sub[i: j] for sub in test_list])

# printing result
print("The Concatenated String : " + str(res))
