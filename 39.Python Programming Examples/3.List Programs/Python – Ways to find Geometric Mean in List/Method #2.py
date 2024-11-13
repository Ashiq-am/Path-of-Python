# Python3 code to demonstrate working of
# Geometric Mean of List
# using statistics.geometric_mean()
import statistics

# initialize list
test_list = [6, 7, 3, 9, 10, 15]

# printing original list
print("The original list is : " + str(test_list))

# Geometric Mean of List
# using statistics.geometric_mean()
res = statistics.geometric_mean(test_list, 1)

# printing result
print("The geometric mean of list is : " + str(res))
