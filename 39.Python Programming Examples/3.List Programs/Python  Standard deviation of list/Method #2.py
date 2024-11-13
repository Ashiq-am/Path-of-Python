# Python3 code to demonstrate working of
# Standard deviation of list
# Using pstdev()
import statistics

# initializing list
test_list = [4, 5, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Standard deviation of list
# Using pstdev()
res = statistics.pstdev(test_list)

# Printing result
print("Standard deviation of sample is : " + str(res))
