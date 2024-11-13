# Python3 code to demonstrate
# Even Front digits Test in List
# using list comprehension + map()

# initializing list
test_list = [25, 6, 828829, 432]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + map()
# Even Front digits Test in List
res = len(set((int(sub[0]) % 2) for sub in map(str, test_list))) == 1

# print result
print("Does each element start with even digit ? " + str(res))
