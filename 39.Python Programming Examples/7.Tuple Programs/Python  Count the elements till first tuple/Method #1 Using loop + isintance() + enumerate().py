# Python3 code to demonstrate working of
# Elements till first tuple
# using isinstance() + enumerate() + loop

# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Elements till first tuple
# using isinstance() + enumerate() + loop
for count, ele in enumerate(test_tup):
	if isinstance(ele, tuple):
		break

# printing result
print("Elements till the first tuple : " + str(count))
