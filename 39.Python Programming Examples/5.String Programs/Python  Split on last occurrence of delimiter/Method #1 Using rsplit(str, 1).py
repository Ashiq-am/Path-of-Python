# Python3 code to demonstrate
# Split on last occurrence of delimiter
# using rsplit()

# initializing string
test_string = "gfg, is, good, better, and best"

# printing original string
print("The original string : " + str(test_string))

# using rsplit()
# Split on last occurrence of delimiter
res = test_string.rsplit(', ', 1)

# print result
print("The splitted list at the last comma : " + str(res))
