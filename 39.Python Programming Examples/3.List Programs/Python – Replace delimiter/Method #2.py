# Python3 code to demonstrate working of
# Replace delimiter
# Using list comprehension + replace()

# initializing list
test_list = ["a, t", "g, f, g", "w, e", "d, o"]

# printing original list
print("The original list is : " + str(test_list))

# initializing replace delimiter
repl_delim = '#'

# Replace delimiter
# iterating inside comprehension, performing replace using replace()
res = [sub.replace(', ', repl_delim) for sub in test_list]

# printing result
print("Replaced List : " + str(res))
