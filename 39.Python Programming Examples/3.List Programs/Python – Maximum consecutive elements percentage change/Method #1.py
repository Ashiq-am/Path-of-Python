# Python3 code to demonstrate working of
# Maximum consecutive elements percentage change
# Using zip() + loop

# initializing list
test_list = [4, 6, 7, 4, 2, 6, 2, 8]

# printing original list
print("The original list is : " + str(test_list))

# Maximum consecutive elements percentage change
# Using zip() + loop
res = 0
for x, y in zip(test_list, test_list[1:]):
	res = max((abs(x - y) / x) * 100, res)

# printing result
print("The maximum percentage change : " + str(res))
