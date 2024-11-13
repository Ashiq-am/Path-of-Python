# Python3 code to demonstrate working of
# Replace delimiter
# Using loop + replace()

# initializing list
test_list = ["a, t", "g, f, g", "w, e", "d, o"]

# printing original list
print("The original list is : " + str(test_list))

# initializing replace delimiter
repl_delim = '#'

# Replace delimiter
res = []
for ele in test_list:
    # adding each string after replacement using replace()
    res.append(ele.replace(", ", repl_delim))

# printing result
print("Replaced List : " + str(res))
