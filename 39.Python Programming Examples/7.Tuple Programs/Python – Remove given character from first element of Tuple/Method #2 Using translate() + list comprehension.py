# Python3 code to demonstrate working of
# Remove K character from first element of Tuple
# Using translate() + list comprehension

# initializing list
test_list = [("GF ! g !", 5), ("! i ! s", 4), ("best !!", 10)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "!"

# translation after conversion to ascii number
res = [(sub[0].translate({ord(K): None}), sub[1]) for sub in test_list]

# printing result
print("The filtered tuples : " + str(res))
