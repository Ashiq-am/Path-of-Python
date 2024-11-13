# Python3 code to demonstrate working of
# Filter String Tuples if String lengths equals K
# Using all() + list comprehension

# initializing list
test_list = [("ABC", "Gfg", "CS1"), ("Gfg", "Best"), ("Gfg", "WoW")]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# all checks for all lengths equals K
res = [sub for sub in test_list if all(len(ele) == K for ele in sub)]

# printing result
print("The filtered tuples : " + str(res))
