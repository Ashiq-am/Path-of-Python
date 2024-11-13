# Python3 code to demonstrate working of
# Replace substring from Initial element
# Using list slicing + list comprehension

# initializing list
test_list = [5, 2, 6, 4, 7, 1, 3]

# printing original list
print("The original list : " + str(test_list))

# initializing repl_list
repl_list = [6, 10, 18]

# Replace substring from Initial element
# Extracting index
idx = test_list.index(repl_list[0])

# Slicing till index, and then adding rest of list
res = test_list[ :idx] + repl_list + test_list[idx + len(repl_list):]

# printing result
print("Substituted List : " + str(res))
