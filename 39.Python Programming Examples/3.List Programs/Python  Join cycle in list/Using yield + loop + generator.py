# Python3 code to demonstrate working of
# Join cycle in list
# Using yield + loop + generator

# helper function to perform this task
def cycle(test_list, val, stop = None):
	temp = dict(test_list)
	stop = stop if stop is not None else val
	while True:
		yield (val)
		val = temp.get(val, stop)
		if val == stop: break

# initializing list
test_list = [[6, 7], [9, 6], [7, 9]]

# printing original list
print("The original list is : " + str(test_list))

# Join cycle in list
# Using yield + loop + generator
# printing result
print("The cycle elements are : ")
for ele in cycle(test_list, 6):
	print(ele)
