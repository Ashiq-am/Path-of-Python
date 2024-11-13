# Python3 code to demonstrate
# checking for first digit in elements
# using list comprehension + map()

# initializing list
test_list = [45, 4, 428829, 432]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + map()
# checking for first digit in elements
res = len(set(sub[0] for sub in map(str, test_list))) == 1

# print result
print("Does each element start with same digit ? " + str(res))
