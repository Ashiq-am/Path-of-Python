# Python program showing
# using of normal function
def Key(x):
	return x%2
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sort = sorted(nums, key = Key)
print(sort)
