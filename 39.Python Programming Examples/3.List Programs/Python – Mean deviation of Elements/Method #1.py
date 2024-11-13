# Python3 code to demonstrate working of
# Mean deviation of Elements
# Using loop + mean() + abs()
from statistics import mean

# initializing list
test_list = [7, 5, 1, 2, 10, 3]

# printing original lists
print("The original list is : " + str(test_list))

res = []

# getting mean
mean_val = mean(test_list)

for ele in test_list:

	# getting deviation
	res.append(abs(ele - mean_val))

# printing result
print("Mean deviations : " + str(res))
