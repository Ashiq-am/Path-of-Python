# Python3 code to demonstrate working of
# Records Maxima in List of Tuples
# using zip() + map() + max()

# initialize list
test_list = [(1, 2, 3), (6, 7, 6), (1, 6, 8)]

# printing original list
print("The original list : " + str(test_list))

# Records Maxima in List of Tuples
# using zip() + map() + max()
res = list(map(max, zip(*test_list)))

# printing result
print("The Cummulative column maximum is : " + str(res))
