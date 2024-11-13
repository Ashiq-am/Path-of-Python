# Python3 code to demonstrate working of
# Sort on basis of reverse Strings
# Using reverse() + sort()

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list : " + str(test_list))

# reverse() to reverse each string
res = []
for ele in test_list:
    res.append("".join(reversed(ele)))

# sorting to get required ordering
res.sort()

# reverse each element again
test_list = []
for ele in res:
    test_list.append("".join(reversed(ele)))

# printing result
print("List after sorting on reversed strings : " + str(test_list))
