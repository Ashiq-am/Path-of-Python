# Python3 code to demonstrate working of
# Rows with K string in Matrix
# Using list comprehension

# initializing list
test_list = [["GFG", "best", "geeks"], ["geeks", "rock"],
			["GFG", "for", "CS"], ["Keep", "learning"]]

# printing original list
print("The original list is : ", test_list)

# initializing K
K = "GFG"

# shorthand to get result
res = [idx for idx, ele in enumerate(test_list) if K in ele]

# printing result
print("Rows with K : " + str(res))
