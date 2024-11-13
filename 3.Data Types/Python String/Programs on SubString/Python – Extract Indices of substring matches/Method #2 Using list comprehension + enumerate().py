# Python3 code to demonstrate working of
# Extract Indices of substring matches
# Using list comprehension + enumerate()

# initializing list
test_list = ["Gfg is good", "for Geeks", "I love Gfg", "Its useful"]

# initializing K
K = "Gfg"

# printing original list
print("The original list : " + str(test_list))

# using list comprehension and enumerate to offer compact solution
res = [idx for idx, val in enumerate(test_list) if K in val]

# printing result
print("The indices list : " + str(res))
