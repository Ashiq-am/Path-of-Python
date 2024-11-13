# Python3 code to demonstrate working of
# Remove K character from first element of Tuple
# Using replace() + list comprehenson

# initializing list
test_list = [("GF ! g !", 5), ("! i ! s", 4), ("best !!", 10)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "!"

# replace with empty string removes the desired char.
res = [(sub[0].replace(K, ''), sub[1]) for sub in test_list]

# printing result
print("The filtered tuples : " + str(res))
