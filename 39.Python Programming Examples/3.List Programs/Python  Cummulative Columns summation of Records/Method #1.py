# Python3 code to demonstrate working of
# Cummulative Columns summation of Records
# using list comprehension + sum() + zip()

# initialize list
test_list = [(1, 2, 3), (6, 7, 6), (1, 6, 8)]

# printing original list
print("The original list : " + str(test_list))

# Cummulative Columns summation of Records
# using list comprehension + sum() + zip()
res = [sum(ele) for ele in zip(*test_list)]

# printing result
print("The Cummulative column sum is : " + str(res))
