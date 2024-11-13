# Python code to demonstrate working of
# Consecutive elements grouping list
# using enumerate() + groupby() + generator function + lambda
import itertools

# Utility Generator Function
def groupc(test_list):
	for x, y in itertools.groupby(enumerate(test_list), lambda a, b: b - a):
		y = list(y)
		yield y[0][1], y[-1][1]

# initialize list
test_list = [1, 2, 3, 6, 7, 8, 11, 12, 13]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive elements grouping list
# using enumerate() + groupby() + generator function + lambda
res = list(groupc(test_list))

# printing result
print("Grouped list is : " + str(res))
