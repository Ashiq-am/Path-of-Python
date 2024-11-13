# Python3 code to demonstrate
# Test rear digit match
# using list comprehension + map()

# initializing list
test_list = [45, 545, 2345, 8765]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + map()
# Test rear digit match
res = len(set(sub[-1] for sub in map(str, test_list))) == 1

# print result
print("Does each element end with same digit ? " + str(res))
