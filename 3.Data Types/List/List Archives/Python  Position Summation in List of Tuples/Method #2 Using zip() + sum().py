# Python3 code to demonstrate
# position summation in list of tuples
# using zip() + sum()

# initializing list
test_list = [(1, 6), (3, 4), (5, 8)]

# printing original list
print ("The original list is : " + str(test_list))

# position Summation in List of Tuples
# using zip() + sum()
res = [sum(i) for i in zip(*test_list)]

# printing summation
print ("The position summation of tuples : " + str(res))
