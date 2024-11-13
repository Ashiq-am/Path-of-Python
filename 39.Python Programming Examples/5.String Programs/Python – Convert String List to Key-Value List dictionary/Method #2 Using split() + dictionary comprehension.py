# Python3 code to demonstrate working of
# Convert String List to Key-Value List dictionary
# Using split() + dictionary comprehension

# initializing list
test_list = ["gfg is best for geeks", "I love gfg", "CS is best subject"]

# printing string
print("The original list : " + str(test_list))

# using dictionary comprehension to solve this problem
res = {sub[0] : sub[1:] for sub in (ele.split() for ele in test_list)}

# printing results
print("The key values List dictionary : " + str(res))
