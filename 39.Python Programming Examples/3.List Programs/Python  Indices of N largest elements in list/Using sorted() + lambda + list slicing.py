# Python3 code to demonstrate working of
# Indices of N largest elements in list
# using sorted() + lambda + list slicing

# initialize list
test_list = [5, 6, 10, 4, 7, 1, 19]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 4

# Indices of N largest elements in list
# using sorted() + lambda + list slicing
res = sorted(range(len(test_list)), key = lambda sub: test_list[sub])[-N:]

# printing result
print("Indices list of max N elements is : " + str(res))
