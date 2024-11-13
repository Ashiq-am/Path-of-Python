# Python3 code to demonstrate
# Column Average in Record List
# using zip() + sum()

# initializing list
test_list = [(1, 6), (3, 4), (5, 8)]

# printing original list
print ("The original list is : " + str(test_list))

# Column Average in Record List
# using zip() + sum()
temp = [sum(i) for i in zip(*test_list)]
res = []
for ele in temp:
	res.append(ele / len(test_list))

# printing summation
print ("The position Average of tuples : " + str(res))
